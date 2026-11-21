"""00_setup_check.py — run this first. It tells you what is missing.
VS Code terminal:  python scripts/00_setup_check.py
"""
import importlib
import sys
from pathlib import Path

print("Python:", sys.version.split()[0], "at", sys.executable)
print("Working directory:", Path.cwd(), "\n")

missing = []
for pkg in ["pandas", "matplotlib"]:
    try:
        mod = importlib.import_module(pkg)
        print(f"OK  {pkg} {mod.__version__}")
    except ImportError:
        missing.append(pkg)
        print(f"MISSING {pkg}")
if missing:
    print("Fix: pip install -r requirements.txt  (check VS Code uses the same interpreter!)")

data_ok = (Path("data") / "raw" / "XX-Demo_daily_2022-2023.csv").exists()
print("OK  data file found" if data_ok else
      "MISSING data file -> is your working directory the project folder?")

if not missing and data_ok:
    print("\nAll set. Continue with scripts/01_first_figure.py")
