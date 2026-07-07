$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RawRoot = Split-Path -Parent (Split-Path -Parent $ScriptDir)
$Vault = Split-Path -Parent $RawRoot
Set-Location $Vault

$Python = "python"
$Output = & $Python (Join-Path $ScriptDir "agent_knowledge_ops.py") 2>&1
$ExitCode = $LASTEXITCODE
$Output
if ($ExitCode -ne 0) { exit $ExitCode }

