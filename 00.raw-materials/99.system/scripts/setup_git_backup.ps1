param(
  [Parameter(Mandatory=$true)]
  [string]$RemoteUrl,

  [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"

$VaultRoot = Resolve-Path (Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) "..\..\..")
Set-Location $VaultRoot

$GitCmd = Get-Command git -ErrorAction SilentlyContinue
if (-not $GitCmd) {
  $CandidateGit = @(
    "C:\Program Files\Git\cmd\git.exe",
    "C:\Program Files\Git\bin\git.exe",
    "C:\Program Files (x86)\Git\cmd\git.exe",
    "$env:LOCALAPPDATA\Programs\Git\cmd\git.exe"
  ) | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1

  if (-not $CandidateGit) {
    throw "Git is not available in PATH and common install locations were not found. Please install Git for Windows first."
  }

  $Git = $CandidateGit
} else {
  $Git = $GitCmd.Source
}

if (-not (Test-Path ".git\config")) {
  if (Test-Path ".git") {
    $children = Get-ChildItem -Force ".git" -ErrorAction SilentlyContinue
    if ($children.Count -gt 0) {
      throw ".git exists but is not a normal Git repository. Please inspect it before continuing."
    }
    Remove-Item -LiteralPath ".git" -Force
  }
  & $Git init
}

& $Git branch -M $Branch

$existing = & $Git remote
if ($existing -contains "origin") {
  & $Git remote set-url origin $RemoteUrl
} else {
  & $Git remote add origin $RemoteUrl
}

& $Git add .gitignore
& $Git add 00.raw-materials/20.metadata/WebClipper模板-X推文.md
& $Git add 00.raw-materials/20.metadata/Obsidian插件安装清单.md
& $Git add 00.raw-materials/90.processed/agent-knowledge-ops/2026-06-16_AI时代Obsidian工作台搭建SOP.md
& $Git add 00.raw-materials/90.processed/agent-knowledge-ops/2026-07-07_Obsidian工作台SOP符合性检查.md
& $Git add 00.raw-materials/90.processed/agent-knowledge-ops/sensitive-scan-report.md
& $Git add 00.raw-materials/99.system/scripts/scan_sensitive_files.py
& $Git add 00.raw-materials/99.system/scripts/run_sensitive_scan.ps1
& $Git add 00.raw-materials/99.system/scripts/register_sensitive_scan_task.ps1
& $Git add 00.raw-materials/99.system/scripts/setup_git_backup.ps1
& $Git add 30.areas/agent-knowledge-ops/Dashboard.md
& $Git add 30.areas/agent-knowledge-ops/01.task-queue/远程触发语句库.md

& $Git commit -m "vault setup: SOP governance and safety baseline"

Write-Host "Git backup baseline committed."
Write-Host "Remote origin: $RemoteUrl"
Write-Host "Next step: run 'git push -u origin $Branch' after confirming credentials."
