# Purpose: (Re)create the temp_builds test folder with files of known ages,
#          so anyone can test cleanup_by_age.py. Keeps fixtures out of Git.
# Usage:   python setup_cleanup_test.py

import os
import time
import shutil

folder  = "temp_builds"
archive = "temp_builds_archive"

# Start clean: wipe any leftovers from previous runs.
for d in (folder, archive):
    if os.path.isdir(d):
        shutil.rmtree(d)
os.makedirs(folder)

now = time.time()

# (filename, age in days, contents)
files = [
    ("old1.log",    30, "nightly build log"),
    ("old2.tmp",    10, "stale artifact"),
    ("recent1.log",  2, "recent build log"),
    ("recent2.tmp",  0, "today's artifact"),
]

for name, age_days, content in files:
    path = os.path.join(folder, name)
    with open(path, "w") as f:
        f.write(content + "\n")
    stamp = now - (age_days * 86400)   # the file's pretend "last modified" time
    os.utime(path, (stamp, stamp))     # set it to N days ago

print(f"Reset {folder}\\ with {len(files)} test files.")