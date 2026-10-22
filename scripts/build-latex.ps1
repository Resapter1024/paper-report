[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$TexFile,

    [string]$Engine = "xelatex",

    [ValidateSet("auto", "none", "bibtex", "biber")]
    [string]$Bibliography = "auto",

    [switch]$Strict
)

$ErrorActionPreference = "Stop"

function Resolve-ReportExecutable {
    param([Parameter(Mandatory = $true)][string]$Name)

    if (Test-Path -LiteralPath $Name) {
        return (Resolve-Path -LiteralPath $Name).Path
    }

    $command = Get-Command $Name -ErrorAction Stop
    return $command.Source
}

function Invoke-ReportCommand {
    param(
        [Parameter(Mandatory = $true)][string]$Executable,
        [Parameter(Mandatory = $true)][string[]]$Arguments,
        [Parameter(Mandatory = $true)][string]$Label
    )

    Write-Host "[$Label] $Executable $($Arguments -join ' ')"
    $standardOutputPath = [System.IO.Path]::GetTempFileName()
    $standardErrorPath = [System.IO.Path]::GetTempFileName()
    $quotedArguments = @($Arguments | ForEach-Object {
        if ($_ -match "\s") {
            '"' + $_.Replace('"', '\"') + '"'
        }
        else {
            $_
        }
    })

    try {
        $process = Start-Process -FilePath $Executable `
            -ArgumentList $quotedArguments `
            -Wait `
            -PassThru `
            -NoNewWindow `
            -RedirectStandardOutput $standardOutputPath `
            -RedirectStandardError $standardErrorPath

        $commandOutput = @(
            Get-Content -LiteralPath $standardOutputPath -ErrorAction SilentlyContinue
            Get-Content -LiteralPath $standardErrorPath -ErrorAction SilentlyContinue
        )

        if ($process.ExitCode -ne 0) {
            $commandOutput | Select-Object -Last 80 | ForEach-Object { Write-Host $_ }
            throw "$Label failed with exit code $($process.ExitCode)."
        }

        $commandOutput | Select-Object -Last 8 | ForEach-Object { Write-Host $_ }
    }
    finally {
        Remove-Item -LiteralPath $standardOutputPath -Force -ErrorAction SilentlyContinue
        Remove-Item -LiteralPath $standardErrorPath -Force -ErrorAction SilentlyContinue
    }
}

$resolvedTex = (Resolve-Path -LiteralPath $TexFile).Path
$workingDirectory = Split-Path -Parent $resolvedTex
$texName = Split-Path -Leaf $resolvedTex
$jobName = [System.IO.Path]::GetFileNameWithoutExtension($texName)
$engineExecutable = Resolve-ReportExecutable -Name $Engine

$sourceText = Get-Content -LiteralPath $resolvedTex -Raw
$bibliographyMode = $Bibliography
if ($bibliographyMode -eq "auto") {
    if ($sourceText -match "\\addbibresource") {
        $bibliographyMode = "biber"
    }
    elseif ($sourceText -match "\\bibliography\s*\{") {
        $bibliographyMode = "bibtex"
    }
    else {
        $bibliographyMode = "none"
    }
}

$latexArguments = @("-interaction=nonstopmode", "-halt-on-error", $texName)

Push-Location -LiteralPath $workingDirectory
try {
    Invoke-ReportCommand -Executable $engineExecutable -Arguments $latexArguments -Label "LaTeX pass 1"

    if ($bibliographyMode -ne "none") {
        $bibliographyExecutable = Resolve-ReportExecutable -Name $bibliographyMode
        Invoke-ReportCommand -Executable $bibliographyExecutable -Arguments @($jobName) -Label $bibliographyMode
    }

    Invoke-ReportCommand -Executable $engineExecutable -Arguments $latexArguments -Label "LaTeX pass 2"
    Invoke-ReportCommand -Executable $engineExecutable -Arguments $latexArguments -Label "LaTeX pass 3"
}
finally {
    Pop-Location
}

$pdfPath = Join-Path $workingDirectory "$jobName.pdf"
$logPath = Join-Path $workingDirectory "$jobName.log"
if (-not (Test-Path -LiteralPath $pdfPath)) {
    throw "Expected PDF was not created: $pdfPath"
}

$fatalPatterns = @(
    "LaTeX Error",
    "Undefined control sequence",
    "Emergency stop",
    "Citation .+ undefined",
    "Reference .+ undefined",
    "There were undefined citations"
)
$qualityPatterns = @("Overfull \\[hv]box")

$fatalMatches = @()
$qualityMatches = @()
if (Test-Path -LiteralPath $logPath) {
    $fatalMatches = @(Select-String -LiteralPath $logPath -Pattern $fatalPatterns)
    $qualityMatches = @(Select-String -LiteralPath $logPath -Pattern $qualityPatterns)
}

if ($fatalMatches.Count -gt 0) {
    $fatalMatches | ForEach-Object { Write-Error $_.Line }
    throw "The final LaTeX log contains unresolved errors or references."
}

if ($qualityMatches.Count -gt 0) {
    $qualityMatches | ForEach-Object { Write-Warning $_.Line }
    if ($Strict) {
        throw "Strict mode rejected overfull boxes in the final log."
    }
}

Write-Output $pdfPath
