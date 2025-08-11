$ErrorActionPreference = 'Stop'

# === CONFIG ===
$User       = 'FunPhantasie'
$Repo       = 'Loki'
$ReleaseZip = 'CommandPromt_Windows.zip'   # must match the asset name in Releases
$GameName   = 'Command Promt'
$ExeName    = 'Command Promt.exe'

# === Paths ===
$Url      = "https://github.com/$User/$Repo/releases/latest/download/$ReleaseZip"
$ZipPath  = Join-Path $env:TEMP "$GameName.zip"

# Install to the folder where this script is run from:
if (-not $DestDir) { $DestDir = $PWD.Path }

Write-Host "→ Downloading $GameName..."
Write-Host "  $Url"
Invoke-WebRequest $Url -OutFile $ZipPath

Write-Host "→ Extracting to $DestDir"
Expand-Archive -Path $ZipPath -DestinationPath $DestDir -Force

# Validate exe exists
$ExePath = Join-Path $DestDir $ExeName
if (!(Test-Path $ExePath)) {
    throw "Expected EXE not found: $ExePath"
}

# Launch game (no desktop shortcut now, since it’s in your chosen folder)
Write-Host "→ Launching $GameName..."
Start-Process $ExePath

Write-Host "✓ Done."
