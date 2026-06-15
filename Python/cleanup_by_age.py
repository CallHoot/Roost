# Purpose: Archive old files from a build-output folder so it stops filling up.
# Usage:   python cleanup_by_age.py           (dry run - shows what it would do)
#          python cleanup_by_age.py --apply   (actually moves the old files)
# What it automates away: hand-clearing a temp folder that fills up every week.

import os
import sys
import time
import shutil
from datetime import datetime

folder       = "temp_builds"
archive      = "temp_builds_archive"
log_file     = "cleanup.log"
max_age_days = 7

apply_changes = "--apply" in sys.argv

def log(message):
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S}  {message}"
    print(line)
    with open(log_file, "a") as f:
        f.write(line + "\n")

# Safety check: the target folder must exist before we touch anything.
if not os.path.isdir(folder):
    print(f"ERROR: folder '{folder}' not found. Aborting.")
    sys.exit(1)

mode = "APPLY" if apply_changes else "DRY RUN"
log(f"--- cleanup start ({mode}, older than {max_age_days} days) ---")

now    = time.time()
cutoff = now - (max_age_days * 86400)
count  = 0

for name in os.listdir(folder):
    path = os.path.join(folder, name)
    if os.path.isfile(path) and os.path.getmtime(path) < cutoff:
        if apply_changes:
            os.makedirs(archive, exist_ok=True)
            shutil.move(path, os.path.join(archive, name))
            log(f"ARCHIVED: {name}")
        else:
            log(f"WOULD ARCHIVE: {name}")
        count += 1

log(f"--- done: {count} file(s) {'archived' if apply_changes else 'flagged'} ---")