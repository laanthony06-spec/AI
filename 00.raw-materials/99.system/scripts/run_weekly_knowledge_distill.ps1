$ErrorActionPreference = "Stop"

$SystemRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Base = Split-Path -Parent $SystemRoot
$Vault = Split-Path -Parent $Base
Set-Location $Vault

$Python = Join-Path $SystemRoot ".venv\Scripts\python.exe"
if (!(Test-Path $Python)) {
    python -m venv (Join-Path $SystemRoot ".venv")
    & $Python -m pip install -q rapidocr_onnxruntime pillow
}

$LogDir = Join-Path $SystemRoot "cache"
if (!(Test-Path $LogDir)) { New-Item -ItemType Directory -Force -Path $LogDir | Out-Null }
$Log = Join-Path $LogDir "weekly_knowledge_distill_task.log"

$env:PYTHONIOENCODING = "utf-8"
$old = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$Output = & $Python (Join-Path $SystemRoot "scripts\weekly_knowledge_distill.py") 2>&1
$ExitCode = $LASTEXITCODE
$ErrorActionPreference = $old
$Output | Tee-Object -FilePath $Log
if ($ExitCode -ne 0) { exit $ExitCode }
