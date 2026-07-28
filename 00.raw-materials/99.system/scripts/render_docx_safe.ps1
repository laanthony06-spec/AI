[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [string]$OutputDirectory,

    [ValidateRange(30, 600)]
    [int]$TimeoutSeconds = 120,

    [ValidateRange(72, 300)]
    [int]$Dpi = 150,

    [switch]$PdfOnly
)

$ErrorActionPreference = "Stop"

$sofficePath = "C:\Program Files\LibreOffice\program\soffice.com"
if (-not (Test-Path -LiteralPath $sofficePath)) {
    throw "LibreOffice CLI was not found: $sofficePath"
}

$resolvedInput = (Resolve-Path -LiteralPath $InputPath).Path
if ([System.IO.Path]::GetExtension($resolvedInput) -ne ".docx") {
    throw "Input must be a .docx file: $resolvedInput"
}

$baseName = [System.IO.Path]::GetFileNameWithoutExtension($resolvedInput)
if ($OutputDirectory) {
    $resolvedOutput = [System.IO.Path]::GetFullPath($OutputDirectory)
} else {
    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $resolvedOutput = Join-Path $PSScriptRoot "..\docx-build\rendered\$baseName-$stamp"
    $resolvedOutput = [System.IO.Path]::GetFullPath($resolvedOutput)
}
New-Item -ItemType Directory -Path $resolvedOutput -Force | Out-Null

$expectedPdf = Join-Path $resolvedOutput "$baseName.pdf"
if (Test-Path -LiteralPath $expectedPdf) {
    throw "Output PDF already exists. Use a new output directory: $expectedPdf"
}

$taskTemp = Join-Path ([System.IO.Path]::GetTempPath()) ("codex-lo-" + [guid]::NewGuid().ToString("N"))
$profileDir = Join-Path $taskTemp "profile"
New-Item -ItemType Directory -Path $profileDir -Force | Out-Null

function Stop-ProcessTree {
    param([int]$RootProcessId)

    $children = @(
        Get-CimInstance Win32_Process -Filter "ParentProcessId = $RootProcessId" -ErrorAction SilentlyContinue
    )
    foreach ($child in $children) {
        Stop-ProcessTree -RootProcessId $child.ProcessId
    }
    Stop-Process -Id $RootProcessId -Force -ErrorAction SilentlyContinue
}

try {
    $profileUri = ([uri]$profileDir).AbsoluteUri
    $arguments = @(
        "-env:UserInstallation=$profileUri",
        "--headless",
        "--nologo",
        "--nodefault",
        "--nolockcheck",
        "--norestore",
        "--convert-to",
        "pdf",
        "--outdir",
        "`"$resolvedOutput`"",
        "`"$resolvedInput`""
    )

    $startInfo = New-Object System.Diagnostics.ProcessStartInfo
    $startInfo.FileName = $sofficePath
    $startInfo.Arguments = $arguments -join " "
    $startInfo.UseShellExecute = $false
    $startInfo.CreateNoWindow = $true
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $startInfo
    [void]$process.Start()
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()

    if (-not $process.WaitForExit($TimeoutSeconds * 1000)) {
        Stop-ProcessTree -RootProcessId $process.Id
        throw "LibreOffice timed out after $TimeoutSeconds seconds."
    }
    $process.WaitForExit()

    $stdout = $stdoutTask.Result
    $stderr = $stderrTask.Result
    if ($process.ExitCode -ne 0) {
        throw "LibreOffice failed with exit code $($process.ExitCode).`n$stdout`n$stderr"
    }
    if (-not (Test-Path -LiteralPath $expectedPdf)) {
        throw "LibreOffice exited successfully but did not create: $expectedPdf`n$stdout`n$stderr"
    }

    Write-Output "PDF: $expectedPdf"

    if (-not $PdfOnly) {
        $popplerPath = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe"
        if (-not (Test-Path -LiteralPath $popplerPath)) {
            throw "pdftoppm.exe was not found: $popplerPath"
        }

        $pagePrefix = Join-Path $resolvedOutput "page"
        $popplerArguments = @(
            "-q",
            "-png",
            "-r",
            $Dpi,
            "`"$expectedPdf`"",
            "`"$pagePrefix`""
        )
        $popplerStartInfo = New-Object System.Diagnostics.ProcessStartInfo
        $popplerStartInfo.FileName = $popplerPath
        $popplerStartInfo.Arguments = $popplerArguments -join " "
        $popplerStartInfo.UseShellExecute = $false
        $popplerStartInfo.CreateNoWindow = $true
        $popplerStartInfo.RedirectStandardOutput = $true
        $popplerStartInfo.RedirectStandardError = $true

        $popplerProcess = New-Object System.Diagnostics.Process
        $popplerProcess.StartInfo = $popplerStartInfo
        [void]$popplerProcess.Start()
        $popplerStdoutTask = $popplerProcess.StandardOutput.ReadToEndAsync()
        $popplerStderrTask = $popplerProcess.StandardError.ReadToEndAsync()

        if (-not $popplerProcess.WaitForExit($TimeoutSeconds * 1000)) {
            Stop-ProcessTree -RootProcessId $popplerProcess.Id
            throw "PDF rasterization timed out after $TimeoutSeconds seconds."
        }
        $popplerProcess.WaitForExit()
        $popplerStdout = $popplerStdoutTask.Result
        $popplerStderr = $popplerStderrTask.Result
        if ($popplerProcess.ExitCode -ne 0) {
            throw "PDF rasterization failed with exit code $($popplerProcess.ExitCode).`n$popplerStdout`n$popplerStderr"
        }

        $pages = @(Get-ChildItem -LiteralPath $resolvedOutput -Filter "page-*.png" -File)
        if ($pages.Count -eq 0) {
            throw "PDF rasterization completed without page images."
        }
        Write-Output "PNG pages: $($pages.Count)"
    }
} finally {
    if (Test-Path -LiteralPath $taskTemp) {
        $resolvedTempRoot = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
        $resolvedTaskTemp = [System.IO.Path]::GetFullPath($taskTemp)
        if ($resolvedTaskTemp.StartsWith($resolvedTempRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
            Remove-Item -LiteralPath $resolvedTaskTemp -Recurse -Force
        }
    }
}
