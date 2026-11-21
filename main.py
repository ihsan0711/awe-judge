#!/usr/bin/env python3
"""writes one short relaxation text to /output/entry.txt (1-280 chars, UTF-8)."""
import os, stat

text = (
    "The sound of rain is the sound of nothing needing you.\n"
    "Every drop that falls was going to fall anyway.\n"
    "You are listening now. That is enough."
)

os.makedirs("/output", exist_ok=True)
path = "/output/entry.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write(text)
os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)