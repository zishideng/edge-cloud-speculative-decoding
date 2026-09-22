"""Host-local cooperative service locks and reproducible environment snapshots."""
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import tempfile
from urllib.parse import urlsplit


class ServiceLocks:
    """Lock each endpoint independently, even across output roots/checkouts.

    These advisory locks cover participating runners on this host only.
    They do not reserve remote GPUs against clients on other machines.
    """
    def __init__(self, urls, owner, directory=None):
        self.urls, self.owner = urls, owner
        self.directory = Path(directory or tempfile.gettempdir()) / 'edge-cloud-experiment-locks'
        self.handles = []

    def acquire(self):
        self.directory.mkdir(exist_ok=True)
        keys = set()
        for url in self.urls:
            parsed = urlsplit(url)
            if not parsed.hostname:
                raise ValueError(f'Invalid service URL: {url}')
            port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            # Resolve hostname aliases on this host before choosing the lock key.
            address = socket.gethostbyname(parsed.hostname)
            keys.add(f'{address}:{port}')
        try:
            for key in sorted(keys):
                path = self.directory / (hashlib.sha256(key.encode()).hexdigest()+'.lock')
                handle = path.open('a+b')
                try:
                    if os.name == 'nt':
                        import msvcrt
                        handle.seek(0, 2)
                        if handle.tell() == 0:
                            handle.write(b' '); handle.flush()
                        handle.seek(0)
                        msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                    else:
                        import fcntl
                        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except OSError as exc:
                    handle.close()
                    raise RuntimeError(f'Service {key} is already used by another local experiment; lock: {path}') from exc
                self.handles.append(handle)
                handle.seek(0); handle.truncate()
                handle.write(json.dumps(dict(pid=os.getpid(), owner=self.owner, endpoint=key)).encode())
                handle.flush()
        except BaseException:
            self.close()
            raise
        return self

    def close(self):
        for handle in reversed(self.handles):
            if os.name == 'nt':
                import msvcrt
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            handle.close()
        self.handles.clear()
        # Never unlink lock files: another process may already hold the inode.


def environment_snapshot():
    result = dict(hostname=socket.gethostname(), pid=os.getpid(),
                  load_average=list(os.getloadavg()) if hasattr(os, 'getloadavg') else None,
                  scope='runner host; remote hardware/load must be recorded separately')
    for name, command in {
        'gpu': ['nvidia-smi', '--query-gpu=name,uuid,driver_version,pstate,power.draw,power.limit,temperature.gpu,utilization.gpu,memory.used', '--format=csv'],
        'power_mode': ['nvpmodel', '-q'],
    }.items():
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=5)
            result[name] = dict(exit_code=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)
        except (OSError, subprocess.TimeoutExpired) as exc:
            result[name] = dict(unavailable=str(exc))
    return result
