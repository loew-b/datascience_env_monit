"""
01_first_figure.py
Environmental Monitoring and Data Analysis · Block 1

Goal: go from a raw data file to a labelled, reproducible figure.

How to run (working directory must be the project folder `lecture01_starter`):
    VS Code : open the folder lecture01_starter, select your Python
              interpreter, then in the terminal run
              python scripts/01_first_figure.py
"""

# --- 0. Packages -------------------------------------------------------------
# Install once:  pip install -r requirements.txt
from pathlib import Path
import platform
import sys

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# --- 1. Paths ----------------------------------------------------------------
# Relative paths: the script works on any computer as long as the
# working directory is the project folder.
raw_file = Path("data/raw/XX-Demo_daily_2022-2023.csv")
fig_file = Path("outputs/figures/fig01_gpp_timeseries_py.png")

if not raw_file.exists():
    sys.exit(f"Cannot find {raw_file}. Is your working directory the project "
             f"folder? Current working directory: {Path.cwd()}")

# --- 2. Import ---------------------------------------------------------------
# FLUXNET-style files code missing values as -9999. Declare it on import,
# otherwise -9999 is treated as a real measurement.
flux = pd.read_csv(raw_file, na_values=[-9999])

# --- 3. Inspect --------------------------------------------------------------
print(flux.shape)                          # rows, columns
print(list(flux.columns))                  # variable names
print(flux["GPP_NT_VUT_REF"].describe())   # summary
print("Missing GPP days:", flux["GPP_NT_VUT_REF"].isna().sum())

# --- 4. Prepare --------------------------------------------------------------
# TIMESTAMP is stored as YYYYMMDD; convert it to a real date.
flux["date"] = pd.to_datetime(flux["TIMESTAMP"].astype(str), format="%Y%m%d")

# --- 5. Plot -----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(flux["date"], flux["GPP_NT_VUT_REF"], color="#2b7a4b", linewidth=0.6)
ax.set_title("Daily gross primary productivity at site XX-Demo", loc="left")
ax.set_xlabel("Date")
ax.set_ylabel(r"GPP (g C m$^{-2}$ d$^{-1}$)")
ax.text(0, -0.22, "Synthetic teaching data · gaps are missing observations, "
        "not zero flux\nSource: course practice dataset "
        "(data/raw/XX-Demo_daily_2022-2023.csv)", transform=ax.transAxes,
        fontsize=8, color="grey", va="top")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()

# --- 6. Save -----------------------------------------------------------------
fig_file.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(fig_file, dpi=300)
print(f"Saved figure to {fig_file}")

# --- 7. Record the environment (part of reproducibility) ---------------------
Path("outputs", "environment_python.txt").write_text(
    f"Python {platform.python_version()}\n"
    f"pandas {pd.__version__}\n"
    f"matplotlib {matplotlib.__version__}\n"
)

plt.show()
