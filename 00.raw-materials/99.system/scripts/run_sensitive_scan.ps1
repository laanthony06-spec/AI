$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$VaultRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..")
Set-Location $VaultRoot

python "00.raw-materials/99.system/scripts/scan_sensitive_files.py"
$exitCode = $LASTEXITCODE

# scan_sensitive_files.py returns 1 when it finds sensitive-looking items.
# For scheduled-task health, treat the generated report itself as success.
if ($exitCode -eq 0 -or $exitCode -eq 1) {
  exit 0
}

exit $exitCode
