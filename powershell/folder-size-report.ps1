# Purpose: Report which user home folders exceed a size limit.
# Usage:   .\folder-size-report.ps1
# What it automates away: right-clicking every user folder to read its size.

$basePath       = ".\test_users"   # parent folder holding all the user folders
$thresholdBytes = 1MB              # flag anything bigger than this (10GB in production)

# Safety check: make sure the base folder exists before we scan.
if (-not (Test-Path $basePath)) {
    Write-Host "ERROR: base path '$basePath' not found. Aborting."
    exit 1
}

$userFolders = Get-ChildItem -Path $basePath -Directory
$flagged = 0

foreach ($user in $userFolders) {
    # Sum the size of EVERY file underneath this user's folder, subfolders included.
    $totalBytes = (Get-ChildItem -Path $user.FullName -Recurse -File |
                   Measure-Object -Property Length -Sum).Sum

    # Report only the folders that go over the limit.
    if ($totalBytes -gt $thresholdBytes) {
        "OVER LIMIT: {0} = {1:N1} MB" -f $user.Name, ($totalBytes / 1MB)
        $flagged++
    }
}

# Human-readable summary so the reader knows it actually ran.
Write-Host ("Checked {0} folders. {1} over the {2:N1} MB limit." -f $userFolders.Count, $flagged, ($thresholdBytes / 1MB))