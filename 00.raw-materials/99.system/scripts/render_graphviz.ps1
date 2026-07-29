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

$dotLines = Get-Content -LiteralPath $resolvedInput -Encoding UTF8
$dotText = $dotLines -join "`n"
if ($dotText -notmatch 'rankdir\s*=\s*TB') {
    throw "DOT must use rankdir=TB: $resolvedInput"
}
if ($dotText -notmatch 'splines\s*=\s*ortho') {
    throw "DOT must use splines=ortho: $resolvedInput"
}

$edgePattern = '^\s*(?:"[^"]+"|[A-Za-z_][A-Za-z0-9_]*)\s*:[nswe]\s*->\s*(?:"[^"]+"|[A-Za-z_][A-Za-z0-9_]*)\s*:[nswe]\b'
$invalidEdges = @(
    $dotLines |
        Where-Object { $_ -match '->' -and $_ -notmatch '^\s*(//|#)' -and $_ -notmatch $edgePattern }
)
if ($invalidEdges.Count -gt 0) {
    $details = $invalidEdges | ForEach-Object { "  $($_.Trim())" }
    throw "Every DOT edge must explicitly use :n/:s/:w/:e fixed ports:`n$($details -join "`n")"
}

$incomingCounts = @{}
foreach ($line in $dotLines) {
    if ($line -match '->\s*(?<target>"[^"]+"|[A-Za-z_][A-Za-z0-9_]*)\s*:[nswe]\b') {
        $target = $Matches.target
        if (-not $incomingCounts.ContainsKey($target)) {
            $incomingCounts[$target] = 0
        }
        $incomingCounts[$target]++
    }
}
$multiIncoming = @(
    $incomingCounts.GetEnumerator() |
        Where-Object { $_.Value -gt 1 } |
        Sort-Object Name
)
if ($multiIncoming.Count -gt 0) {
    $targets = $multiIncoming | ForEach-Object { "$($_.Name)=$($_.Value)" }
    Write-Warning "Multiple edges enter the same node ($($targets -join ', ')). Inspect the rendered geometry; Graphviz may spread or misplace shared entry anchors."
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
