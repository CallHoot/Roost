# Purpose: Generate standard usernames for new hires from a CSV.
# Usage:   python csv-update.py
# What it automates away: hand-typing a login for every new employee during onboarding.

import csv
import re
import os
import sys

# Safety check: stop with a clear message if the input file is missing,
# instead of crashing with a confusing error.
if not os.path.exists("new_hires.csv"):
    print("ERROR: new_hires.csv not found in this folder. Aborting.")
    sys.exit(1)

# Read the CSV into a list of rows. DictReader makes each row a dictionary
# keyed by column name. -- so hire["FirstName"] is Python's version of $hire.FirstName.
with open("new_hires.csv", newline="") as f:
    hires = list(csv.DictReader(f))

#Build a username for each hire -- first letter of first name + last name, all lowercase.
# Also, remove any non-alphanumeric characters from the username, to be safe.
for hire in hires:
    initial    = hire["FirstName"][0]  # first letter of first name
    clean_last = re.sub(r"[^a-zA-Z]", "", hire["LastName"])  # lastname with non-letters stripped
    hire["Username"] = (initial + clean_last).lower()  # combine and lowercase

# Write the updated rows to a NEW file. "w" overwries cleanly every run -- idempotont.
fieldnames = ["FirstName", "LastName", "Department", "Username"]  # specify column order for output
with open("users_with_logins.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # write the column names as the first row
    writer.writerows(hires)  # write all the updated rows at once

# Human-readable summary so whoever runs it knows what happened.
print(f"Processed {len(hires)} users -> users_with_logins.csv")