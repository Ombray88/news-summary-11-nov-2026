#!/usr/bin/env python3
"""news-summary-01 entry (Python 3.13, standard library only).

The summary is the summary.txt beside this file; the program copies it to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
No network, no randomness, no clock: two runs write the same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "summary.txt", OUT_DIR / "entry.txt")
