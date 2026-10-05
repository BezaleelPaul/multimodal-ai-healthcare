param(
    [string]$Deck = "$PSScriptRoot\..\AI-in-Software-Design-and-Engineering.pptx",
    [string]$Out  = "$PSScriptRoot\..\preview",
    [int]$Only = 0
)

$Deck = (Resolve-Path $Deck).Path
if (-not [System.IO.Path]::IsPathRooted($Out)) { $Out = Join-Path (Get-Location) $Out }
if (-not (Test-Path $Out)) { New-Item -ItemType Directory -Force -Path $Out | Out-Null }
$Out = (Resolve-Path $Out).Path
Get-ChildItem $Out -Filter *.png -ErrorAction SilentlyContinue | Remove-Item -Force

$pp = New-Object -ComObject PowerPoint.Application
try {
    $pres = $pp.Presentations.Open($Deck, $true, $false, $false)
    $n = $pres.Slides.Count
    for ($i = 1; $i -le $n; $i++) {
        if ($Only -ne 0 -and $i -ne $Only) { continue }
        $file = Join-Path $Out ("slide-{0:d2}.png" -f $i)
        $pres.Slides.Item($i).Export($file, "PNG", 1600, 900)
    }
    $pres.Close()
    Write-Output "exported $n slides to $Out"
}
finally {
    $pp.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
}
