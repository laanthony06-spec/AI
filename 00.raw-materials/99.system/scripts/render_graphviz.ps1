param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [string]$OutputDirectory
)

$ErrorActionPreference = "Stop"

$dotCommand = Get-Command dot -ErrorAction SilentlyContinue
if ($dotCommand) {
    $dotPath = $dotCommand.Source
} else {
    $dotPath = @(
        "C:\Program Files\Graphviz\bin\dot.exe",
        "C:\Program Files (x86)\Graphviz\bin\dot.exe"
    ) | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
}

if (-not $dotPath) {
    throw "Graphviz is not installed, or dot.exe is not available."
}

$resolvedInput = (Resolve-Path -LiteralPath $InputPath).Path
if ([System.IO.Path]::GetExtension($resolvedInput) -ne ".dot") {
    throw "Input must be a .dot file: $resolvedInput"
}

if ($OutputDirectory) {
    $resolvedOutputDirectory = [System.IO.Path]::GetFullPath($OutputDirectory)
    if (-not (Test-Path -LiteralPath $resolvedOutputDirectory)) {
        New-Item -ItemType Directory -Path $resolvedOutputDirectory -Force | Out-Null
    }
} else {
    $resolvedOutputDirectory = [System.IO.Path]::GetDirectoryName($resolvedInput)
}

$baseName = [System.IO.Path]::GetFileNameWithoutExtension($resolvedInput)
$svgPath = Join-Path $resolvedOutputDirectory "$baseName.svg"
$pdfPath = Join-Path $resolvedOutputDirectory "$baseName.pdf"

& $dotPath -Tsvg $resolvedInput -o $svgPath
if ($LASTEXITCODE -ne 0) {
    throw "SVG rendering failed: $resolvedInput"
}

& $dotPath -Tpdf $resolvedInput -o $pdfPath
if ($LASTEXITCODE -ne 0) {
    throw "PDF rendering failed: $resolvedInput"
}

Write-Output "Generated:"
Write-Output "  $svgPath"
Write-Output "  $pdfPath"
