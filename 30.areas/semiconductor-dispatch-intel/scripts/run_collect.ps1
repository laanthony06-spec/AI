$ErrorActionPreference = "Stop"
$Base = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Base
$Python = Join-Path $Base ".venv\Scripts\python.exe"
if (!(Test-Path $Python)) {
    python -m venv .venv
    & $Python -m pip install -r requirements.txt
}
$Log = Join-Path $Base "cache\last_run.log"
# Native tools may write warnings to stderr. Capture both streams without treating warnings as PowerShell exceptions.
$old = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$Output = & $Python scripts\collect_intel.py 2>&1
$ExitCode = $LASTEXITCODE
$ErrorActionPreference = $old
$Output | Tee-Object -FilePath $Log
if ($ExitCode -ne 0) { exit $ExitCode }
