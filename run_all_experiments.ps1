param(
    [string]$Mode = 'simulate',
    [string]$Config = '',
    [string]$Python = '',
    [string]$OutputRoot = 'results',
    [switch]$VerboseTokens,
    [switch]$VerboseRounds
)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not $Python) {
    if (Test-Path '.venv/Scripts/python.exe') { $Python = '.venv/Scripts/python.exe' }
    elseif (Get-Command python -ErrorAction SilentlyContinue) { $Python = 'python' }
    else { Write-Error 'Python 3.10+ required. Set -Python to its executable path.'; exit 1 }
}
$ExperimentArgs = @('-m', 'experiments.run', '--mode', $Mode, '--output-root', $OutputRoot)
if ($Config) { $ExperimentArgs += @('--config', $Config) }
if ($VerboseTokens) { $ExperimentArgs += '--verbose-tokens' }
if ($VerboseRounds) { $ExperimentArgs += '--verbose-rounds' }
& $Python @ExperimentArgs
exit $LASTEXITCODE
