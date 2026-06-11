# Purpose: Generate standard usernames for new hires from a CSV.
# Usage:   .\csv-update.ps1
# What it automates away: hand-typing a login for every new employee during onboarding.

# Safety check: stop with a clear message if the input file is missing,
# instead of crashing with a confusing error.
if (-not (Test-Path .\new_hires.csv)) {
    Write-Host "ERROR: new_hires.csv not found in this folder. Aborting."
    exit 1
}
# Read the CSV into memory. Each row becomes an object with
# FirstName, LastName, and Department properties.
$hires = Import-Csv .\new_hires.csv
foreach ($hire in $hires) {
    # Build the username in three readable steps:
    $initial   = $hire.FirstName.Substring(0,1)
    $cleanLast = $hire.LastName -replace '[^a-zA-Z]', ''
    $username  = ($initial + $cleanLast).ToLower()
    # Add the username as a new property to the object.
    $hire | Add-Member -NotePropertyName Username -NotePropertyValue $username
}
# Write the updated rows to a NEW file. This overwrites cleanly every run —
# same input always produces the same output. That is the idempotence.
$hires | Export-Csv .\users_with_logins.csv -NoTypeInformation

# Human-readable summary so whoever runs it knows what happened.
Write-Host "Processed $($hires.Count) users -> users_with_logins.csv"