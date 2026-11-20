#!/usr/bin/env python3
from pathlib import Path
for d in ("workspace","data","logs"):
 Path(d).mkdir(exist_ok=True)
print("Directories initialized. No third-party dependencies required.")
