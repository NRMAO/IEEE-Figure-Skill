#!/usr/bin/env python3
"""Generate separate, reproducible metric plots from a tidy CSV.

Expected columns: platform,design,metric,value,unit
Each metric is plotted separately. Do not combine unlike units on one axis.
"""
from pathlib import Path
import argparse
import pandas as pd
import matplotlib.pyplot as plt

COLORS = {
    "Baseline": "#7A8491",
    "Reference": "#7A8491",
    "Proposed": "#D9822B",
    "Optimized": "#2468A2",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", nargs="?", default="sample_metrics.csv")
    parser.add_argument("--out", default="figures")
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    required = {"platform", "design", "metric", "value", "unit"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing columns: {sorted(missing)}")
    if df[list(required)].isnull().any().any():
        raise ValueError("CSV contains missing values in required columns.")
    df["value"] = pd.to_numeric(df["value"], errors="raise")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 9,
        "axes.labelsize": 9,
        "axes.titlesize": 10,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "axes.edgecolor": "#202A35",
        "axes.linewidth": 0.8,
        "savefig.facecolor": "white",
        "figure.facecolor": "white",
    })

    for (platform, metric, unit), part in df.groupby(["platform", "metric", "unit"], sort=True):
        fig, ax = plt.subplots(figsize=(3.45, 2.35), constrained_layout=True)
        part = part.sort_values("design")
        bars = ax.bar(
            part["design"],
            part["value"],
            color=[COLORS.get(x, "#2468A2") for x in part["design"]],
            edgecolor="#202A35",
            linewidth=0.55,
            width=0.62,
        )
        ax.set_title(f"{platform}: {metric}")
        ax.set_ylabel(f"{metric} ({unit})")
        ax.set_xlabel("")
        ax.grid(axis="y", color="#D9DEE5", linewidth=0.45)
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(axis="x", length=0, pad=5)
        for bar, value in zip(bars, part["value"]):
            ax.annotate(
                f"{value:g}",
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                xytext=(0, 3), textcoords="offset points",
                ha="center", va="bottom", fontsize=7,
            )
        stem = f"{platform}_{metric}".lower().replace(" ", "_").replace("/", "_")
        fig.savefig(out / f"{stem}.pdf", bbox_inches="tight")
        fig.savefig(out / f"{stem}.svg", bbox_inches="tight")
        fig.savefig(out / f"{stem}.png", dpi=450, bbox_inches="tight")
        plt.close(fig)

if __name__ == "__main__":
    main()
