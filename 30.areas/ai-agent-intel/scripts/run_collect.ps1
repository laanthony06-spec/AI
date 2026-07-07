$ErrorActionPreference = "Stop"
$Base = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Vault = Split-Path -Parent (Split-Path -Parent $Base)
Set-Location $Vault

$Python = "python"
$Log = Join-Path $Base "cache\last_run_task.log"
if (!(Test-Path (Join-Path $Base "cache"))) {
    New-Item -ItemType Directory -Force -Path (Join-Path $Base "cache") | Out-Null
}
$env:PYTHONIOENCODING = "utf-8"
$old = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$Output = & $Python (Join-Path $Base "scripts\collect_ai_agent_intel.py") 2>&1
$ExitCode = $LASTEXITCODE
$ErrorActionPreference = $old
$Output | Tee-Object -FilePath $Log
if ($ExitCode -ne 0) { exit $ExitCode }

