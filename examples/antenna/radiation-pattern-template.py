#!/usr/bin/env python3
"""Create a polar radiation-pattern plot from real measurement or simulation data.

CSV format:
    series,angle_deg,gain_dbi
    Measured,0, ...
    Simulated,0, ...

The file must contain actual user-supplied data. This template intentionally includes no
fabricated antenna measurements. Use the same angular convention and reference for every series.
"""
from pathlib import Path
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

LINESTYLES = ["-", "--", "-.", ":"]
MARKERS = [None, "o", "s", "^"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="CSV containing series,angle_deg,gain_dbi")
    parser.add_argument("--out", default="radiation_pattern")
    parser.add_argument("--title", default="Antenna radiation pattern")
    parser.add_argument("--rmin", type=float, default=None)
    parser.add_argument("--rmax", type=float, default=None)
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    required = {"series", "angle_deg", "gain_dbi"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {sorted(missing)}")
    df["angle_deg"] = pd.to_numeric(df["angle_deg"], errors="raise")
    df["gain_dbi"] = pd.to_numeric(df["gain_dbi"], errors="raise")
    if df[list(required)].isnull().any().any():
        raise ValueError("Required columns contain missing values.")

    fig = plt.figure(figsize=(5.2, 5.0), constrained_layout=True)
    ax = fig.add_subplot(111, projection="polar")
    plt.rcParams.update({"font.size": 9, "axes.titlesize": 11})

    for i, (name, part) in enumerate(df.groupby("series", sort=False)):
        part = part.sort_values("angle_deg")
        theta = np.deg2rad(part["angle_deg"].to_numpy())
        radius = part["gain_dbi"].to_numpy()
        ax.plot(
            theta,
            radius,
            label=name,
            linestyle=LINESTYLES[i % len(LINESTYLES)],
            marker=MARKERS[i % len(MARKERS)],
            linewidth=1.6,
            markersize=3.0,
        )

    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_title(args.title, pad=18)
    if args.rmin is not None or args.rmax is not None:
        ax.set_ylim(args.rmin, args.rmax)
    ax.set_rlabel_position(135)
    ax.grid(True, linewidth=0.6, alpha=0.6)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.16), ncol=2, frameon=False)

    out = Path(args.out)
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".png"), dpi=450, bbox_inches="tight")
    plt.close(fig)

if __name__ == "__main__":
    main()
