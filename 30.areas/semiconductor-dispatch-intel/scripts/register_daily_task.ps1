$ErrorActionPreference = "Stop"
$Base = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Script = Join-Path $Base "scripts\run_collect.ps1"
$TaskName = "Obsidian Semiconductor Dispatch Intel Daily"
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$Script`""
$Trigger = New-ScheduledTaskTrigger -Daily -At 08:00
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Daily collect semiconductor dispatching intelligence into Obsidian" -Force | Out-Null
Write-Host "Registered scheduled task: $TaskName at 08:00 daily"
