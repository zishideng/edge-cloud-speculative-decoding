param(
    [string]$Mode = 'simulate',
    [string]$Config = '',
    [string]$Python = '',
    [string]$OutputRoot = 'results/suites',
    [switch]$VerboseTokens,
    [switch]$VerboseRounds,
    [string]$Profile = 'quick',
    [string]$ModelPair = '',
    [string]$ModelsYaml = '',
    [string]$DraftUrl = '',
    [string]$CloudUrl = '',
    [int]$N = 0,
    [int]$Repeats = 0,
    [int]$Gamma = 0,
    [int]$Lookahead = 5,
    [int]$MaxTokens = 0,
    [int]$RequestOffset = 0,
    [switch]$Plan
)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not $Python) {
    if (Test-Path '.venv/Scripts/python.exe') { $Python = '.venv/Scripts/python.exe' }
    elseif (Get-Command python -ErrorAction SilentlyContinue) { $Python = 'python' }
    else { Write-Error 'Python 3.10+ required. Set -Python to its executable path.'; exit 1 }
}
$ExperimentArgs = @('-m', 'experiments.suite', '--mode', $Mode, '--output-root', $OutputRoot)
$ExperimentArgs += @('--profile', $Profile, '--lookahead', $Lookahead)
if ($ModelPair) { $ExperimentArgs += @('--model-pair', $ModelPair) }
if ($ModelsYaml) { $ExperimentArgs += @('--models-yaml', $ModelsYaml) }
if ($DraftUrl) { $ExperimentArgs += @('--draft-url', $DraftUrl) }
if ($CloudUrl) { $ExperimentArgs += @('--cloud-url', $CloudUrl) }
if ($N) { $ExperimentArgs += @('--n', $N) }
if ($Repeats) { $ExperimentArgs += @('--repeats', $Repeats) }
if ($Gamma) { $ExperimentArgs += @('--gamma', $Gamma) }
if ($MaxTokens) { $ExperimentArgs += @('--max-tokens', $MaxTokens) }
$ExperimentArgs += @('--request-offset', $RequestOffset)
if ($Plan) { $ExperimentArgs += '--plan' }
if ($Config) { $ExperimentArgs += @('--config', $Config) }
if ($VerboseTokens) { $ExperimentArgs += '--verbose-tokens' }
if ($VerboseRounds) { $ExperimentArgs += '--verbose-rounds' }
& $Python @ExperimentArgs
exit $LASTEXITCODE
