# install.ps1
$ErrorActionPreference = 'Stop'

# === CONFIG ===
$User       = 'FunPhantasie'
$Repo       = 'Loki'
$ReleaseZip = 'CommandPromt_Windows.zip'   # must match the asset name in Releases
$GameName   = 'Command Promt'              # folder & shortcut name
$ExeName    = 'Command Promt.exe'          # the exe at the zip root

# === Paths ===
$Url      = "https://github.com/$User/$Repo/releases/latest/download/$ReleaseZip"
$ZipPath  = Join-Path $env:TEMP "$GameName.zip"
$DestDir  = Join-Path $env:LOCALAPPDATA $GameName

Write-Host "→ Downloading $GameName..."
Write-Host "  $Url"
Invoke-WebRequest $Url -OutFile $ZipPath

if (Test-Path $DestDir) {
    Write-Host "→ Removing previous install at $DestDir"
    Remove-Item $DestDir -Recurse -Force
}

Write-Host "→ Extracting to $DestDir"
Expand-Archive -Path $ZipPath -DestinationPath $DestDir -Force

# Validate exe exists
$ExePath = Join-Path $DestDir $ExeName
if (!(Test-Path $ExePath)) {
    throw "Expected EXE not found: $ExePath"
}

# Optional: Desktop shortcut
try {
    $shortcut = Join-Path ([Environment]::GetFolderPath('Desktop')) "$GameName.lnk"
    $wsh = New-Object -ComObject WScript.Shell
    $s  = $wsh.CreateShortcut($shortcut)
    $s.TargetPath = $ExePath
    $s.WorkingDirectory = $DestDir
    $s.Save()
    Write-Host "→ Created desktop shortcut: $shortcut"
} catch {
    Write-Warning "Could not create desktop shortcut: $($_.Exception.Message)"
}

Write-Host "→ Launching $GameName..."
Start-Process $ExePath

Write-Host "✓ Done."
