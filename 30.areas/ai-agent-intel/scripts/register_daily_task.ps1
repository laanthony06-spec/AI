$ErrorActionPreference = "Stop"
$Base = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Script = Join-Path $Base "scripts\run_collect.ps1"
$TaskName = "Obsidian AI Agent Intel Daily"

$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$Script`""
$Trigger = New-ScheduledTaskTrigger -Daily -At 08:40
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Daily collect AI Agent intelligence into Obsidian" -Force | Out-Null
Write-Host "Registered scheduled task: $TaskName at 08:40 daily"

