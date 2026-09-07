"""Latency statistics, explicit estimates and batch-visible token timings."""
import math

LABELS = {
    'network_rtt_ms': '网络通信往返估算/ms', 'serialize_ms': '请求序列化/ms',
    'upload_ms': '上传分摊估算/ms', 'cloud_queue_ms': '云端应用排队/ms',
    'cloud_verify_ms': '云端验证计算/ms', 'download_ms': '下载分摊估算/ms',
    'deserialize_ms': '响应反序列化/ms', 'round_total_ms': '单轮端到端/ms',
    'draft_token_ms': '草稿单Token平均/ms', 'ttft_ms': '首Token可见延迟/ms',
    'tpot_ms': 'Token间平均延迟/ms', 'tokens_per_second': '吞吐量/token每秒'
}


def percentile(values, q):
    if not values or not 0 <= q <= 1:
        raise ValueError('Nonempty samples and quantile in [0,1] required')
    x = sorted(values)
    if any(not math.isfinite(v) for v in x):
        raise ValueError('Nonfinite latency observation')
    pos = (len(x)-1)*q
    lo = int(pos)
    return x[lo] + (x[min(lo+1,len(x)-1)]-x[lo])*(pos-lo)


def summary(values):
    if not values:
        raise ValueError('No measurements to summarize')
    return dict(mean=sum(values)/len(values), p50=percentile(values,.5),
                p95=percentile(values,.95), p99=percentile(values,.99),
                min=min(values), max=max(values), count=len(values))


def latency_breakdown(http_ms, serialize_ms, deserialize_ms, queue_ms, verify_ms, request_bytes, response_bytes):
    values = [http_ms, serialize_ms, deserialize_ms, queue_ms, verify_ms]
    if any(not math.isfinite(v) or v < 0 for v in values):
        raise ValueError('Invalid timing values')
    residual = http_ms - queue_ms - verify_ms
    net = max(0.0, residual)
    share = request_bytes/max(1, request_bytes+response_bytes)
    return dict(network_rtt_ms=net, serialize_ms=serialize_ms, deserialize_ms=deserialize_ms,
                upload_ms=net*share, download_ms=net*(1-share), cloud_queue_ms=queue_ms,
                cloud_verify_ms=verify_ms, http_round_trip_ms=http_ms,
                timing_residual_ms=residual, timing_inconsistent=residual < 0,
                network_rtt_estimated=True, upload_download_estimated=True,
                timing_note='Residual includes transport, server codec and uninstrumented scheduling; byte-proportional split is an estimate')
