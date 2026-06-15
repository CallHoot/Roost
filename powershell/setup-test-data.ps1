# Purpose: Recreate the fake test_users folders so anyone can test folder-size-report.ps1.
# Usage:   .\setup-test-data.ps1
# What it automates away: hand-building a sized test tree, and keeps binary files out of Git.

function New-SizedFile {
    param([string]$Path, [long]$Bytes)
    New-Item -ItemType Directory -Force -Path (Split-Path $Path -Parent) | Out-Null
    $fs = [System.IO.File]::Create($Path)
    $fs.SetLength($Bytes)
    $fs.Close()
}

New-SizedFile ".\test_users\alice\big.bin"         2MB    # alice = 2.0 MB
New-SizedFile ".\test_users\bob\small.bin"         500KB  # bob   = 500 KB
New-SizedFile ".\test_users\carol\part1.bin"       1MB    # carol top-level
New-SizedFile ".\test_users\carol\archive\old.bin" 512KB  # carol nested -> 1.5 MB

Write-Host "Test data created under .\test_users"