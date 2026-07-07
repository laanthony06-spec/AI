$ErrorActionPreference = "Stop"

$SystemRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Script = Join-Path $SystemRoot "scripts\run_weekly_knowledge_distill.ps1"
$TaskName = "Obsidian Raw Materials Weekly Knowledge Distill"

$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$Script`""
$Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 09:00
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Weekly distill knowledge from Obsidian raw materials into 90.processed" -Force | Out-Null
Write-Host "Registered scheduled task: $TaskName at Monday 09:00 weekly"
