#!/usr/bin/env python3
"""Generate a reproducible plot using an AI-extracted reference style profile.

Example:
    python generate_figure.py data/example.csv --x time --y response --group cohort --kind line
    python generate_figure.py data/example.csv --x method --y score --kind bar

The script reads only user-supplied CSV values. It does not create sample measurements.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

from figure_style import apply_matplotlib_style, color_for_category, load_style_profile


def read_rows(path: Path, x_column: str, y_column: str, group_column: str | None):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {x_column, y_column}
        if group_column:
            required.add(group_column)
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV is missing columns: {sorted(missing)}")
        rows = []
        for line_number, row in enumerate(reader, start=2):
            try:
                y_value = float(row[y_column])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Invalid numeric value in {y_column!r} at CSV line {line_number}.") from exc
            if not row[x_column]:
                raise ValueError(f"Empty x value at CSV line {line_number}.")
            rows.append({
                "x": row[x_column],
                "y": y_value,
                "group": row[group_column] if group_column else "Series",
            })
    if not rows:
        raise ValueError("The CSV contains no data rows.")
    return rows


def main():
    parser = argparse.ArgumentParser(description="Create a figure using an extracted reference style profile.")
    parser.add_argument("csv", type=Path, help="User-supplied CSV data file.")
    parser.add_argument("--profile", type=Path, default=Path("reference-style-profile.json"))
    parser.add_argument("--x", required=True, help="CSV column used for the x axis.")
    parser.add_argument("--y", required=True, help="Numeric CSV column used for the y axis.")
    parser.add_argument("--group", default=None, help="Optional CSV column defining series/categories.")
    parser.add_argument("--kind", choices=("line", "scatter", "bar"), default="line")
    parser.add_argument("--title", default="")
    parser.add_argument("--xlabel", default="")
    parser.add_argument("--ylabel", default="")
    parser.add_argument("--output-dir", type=Path, default=Path("output"))
    parser.add_argument("--stem", default="reference_styled_figure")
    args = parser.parse_args()

    profile = load_style_profile(args.profile)
    apply_matplotlib_style(profile)
    import matplotlib.pyplot as plt
    import numpy as np

    rows = read_rows(args.csv, args.x, args.y, args.group)
    groups = list(dict.fromkeys(row["group"] for row in rows))
    palette = profile["palette"]
    geometry = profile["geometry"]
    layout = profile["layout"]
    canvas = profile["canvas"]
    export = profile["export"]
    line_styles = profile.get("line_styles", ["-", "--", "-.", ":"])

    fig, ax = plt.subplots(
        figsize=(float(canvas["width_in"]), float(canvas["height_in"])),
        constrained_layout=True,
    )

    if args.kind == "bar":
        x_categories = list(dict.fromkeys(row["x"] for row in rows))
        x_positions = np.arange(len(x_categories), dtype=float)
        bar_width = 0.8 / max(1, len(groups))
        for group_index, group in enumerate(groups):
            values = {
                row["x"]: row["y"] for row in rows if row["group"] == group
            }
            positions = []
            heights = []
            for category_index, category in enumerate(x_categories):
                if category in values:
                    positions.append(x_positions[category_index] - 0.4 + bar_width * (group_index + 0.5))
                    heights.append(values[category])
            ax.bar(
                positions,
                heights,
                width=bar_width,
                label=group,
                color=color_for_category(profile, group, group_index),
                edgecolor=palette["text"],
                linewidth=geometry.get("bar_edge_width_pt", 0.55),
            )
        ax.set_xticks(x_positions, x_categories)
    else:
        for group_index, group in enumerate(groups):
            part = [row for row in rows if row["group"] == group]
            x_values = [row["x"] for row in part]
            try:
                x_values = [float(value) for value in x_values]
            except ValueError:
                pass
            y_values = [row["y"] for row in part]
            color = color_for_category(profile, group, group_index)
            if args.kind == "line":
                ax.plot(
                    x_values,
                    y_values,
                    label=group,
                    color=color,
                    linewidth=geometry["line_width_pt"],
                    linestyle=line_styles[group_index % len(line_styles)],
                    marker=None,
                )
            else:
                ax.scatter(
                    x_values,
                    y_values,
                    label=group,
                    color=color,
                    edgecolors=palette["text"],
                    linewidths=geometry.get("marker_edge_width_pt", 0.6),
                    s=geometry["marker_size_pt"] ** 2,
                )

    if args.title:
        ax.set_title(args.title, fontweight=profile["typography"].get("title_weight", "normal"))
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)

    grid_axis = layout.get("grid_axis", "y")
    if grid_axis in {"x", "y", "both"}:
        ax.grid(True, axis=grid_axis, color=palette.get("grid", "#D9DEE5"),
                linewidth=geometry["grid_line_width_pt"])
        ax.set_axisbelow(True)
    if layout.get("hide_top_spine", True):
        ax.spines["top"].set_visible(False)
    if layout.get("hide_right_spine", True):
        ax.spines["right"].set_visible(False)

    if args.group:
        ax.legend(
            loc=layout.get("legend_position", "best"),
            frameon=bool(layout.get("legend_frame", False)),
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for image_format in export["formats"]:
        suffix = "tif" if image_format == "tiff" else image_format
        destination = args.output_dir / f"{args.stem}.{suffix}"
        save_kwargs = {"bbox_inches": "tight"}
        if suffix in {"png", "tif"}:
            save_kwargs["dpi"] = int(export["raster_dpi"])
        fig.savefig(destination, **save_kwargs)
        print(f"Saved: {destination}")
    plt.close(fig)


if __name__ == "__main__":
    main()
