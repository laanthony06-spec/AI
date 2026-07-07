$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Script = Join-Path $ScriptDir "run_agent_knowledge_ops.ps1"
$TaskName = "Obsidian Agent Knowledge Ops Refresh"

$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$Script`""
$Trigger = New-ScheduledTaskTrigger -Daily -At 09:20
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Refresh Agent Knowledge Ops task queue, evidence index, and telemetry dashboard" -Force | Out-Null
Write-Host "Registered scheduled task: $TaskName at 09:20 daily"

