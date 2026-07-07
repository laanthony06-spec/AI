$ErrorActionPreference = "Stop"

$TaskName = "Obsidian Sensitive Scan Weekly"
$ScriptPath = Join-Path (Get-Location) "00.raw-materials\99.system\scripts\run_sensitive_scan.ps1"

$Action = New-ScheduledTaskAction `
  -Execute "powershell.exe" `
  -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$ScriptPath`""

$Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 9:30am

$Settings = New-ScheduledTaskSettingsSet `
  -AllowStartIfOnBatteries `
  -DontStopIfGoingOnBatteries `
  -StartWhenAvailable

Register-ScheduledTask `
  -TaskName $TaskName `
  -Action $Action `
  -Trigger $Trigger `
  -Settings $Settings `
  -Description "Weekly sensitive information scan for Obsidian vault." `
  -Force | Out-Null

Get-ScheduledTask -TaskName $TaskName | Select-Object TaskName, State
