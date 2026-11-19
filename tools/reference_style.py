"""Load and apply an AI-extracted visual reference style profile."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

_HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")
_REQUIRED_COLORS = ("primary", "secondary", "accent", "neutral", "text", "background")


def validate_style_profile(profile: Any) -> list[str]:
    """Return validation errors for a reference-style profile.

    The validator intentionally checks structure and values, not whether the
    extracted style is scientifically appropriate. That judgement belongs to
    the AI/researcher reviewing the original reference.
    """
    errors: list[str] = []
    if not isinstance(profile, dict):
        return ["The style profile root must be a JSON object."]

    for key in ("schema_version", "profile_name", "figure_family", "canvas", "typography", "palette", "geometry", "layout", "export", "extraction"):
        if key not in profile:
            errors.append(f"Missing required field: {key}")

    if profile.get("schema_version") != "1.0":
        errors.append("schema_version must be '1.0'.")

    canvas = profile.get("canvas", {})
    if isinstance(canvas, dict):
        for key in ("width_in", "height_in"):
            value = canvas.get(key)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
                errors.append(f"canvas.{key} must be a positive number.")
        bg = canvas.get("background")
        if bg is not None and (not isinstance(bg, str) or not _HEX.fullmatch(bg)):
            errors.append("canvas.background must be a six-digit HEX color.")
    else:
        errors.append("canvas must be an object.")

    typography = profile.get("typography", {})
    if isinstance(typography, dict):
        for key in ("base_size_pt", "axis_label_size_pt", "tick_label_size_pt", "legend_size_pt"):
            value = typography.get(key)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
                errors.append(f"typography.{key} must be a positive number.")
        fonts = typography.get("fallback_fonts", [])
        if not isinstance(fonts, list) or any(not isinstance(font, str) or not font.strip() for font in fonts):
            errors.append("typography.fallback_fonts must be a list of non-empty strings.")
    else:
        errors.append("typography must be an object.")

    palette = profile.get("palette", {})
    if isinstance(palette, dict):
        for key in _REQUIRED_COLORS:
            value = palette.get(key)
            if not isinstance(value, str) or not _HEX.fullmatch(value):
                errors.append(f"palette.{key} must be a six-digit HEX color.")
        categories = palette.get("categories", [])
        if not isinstance(categories, list):
            errors.append("palette.categories must be a list.")
        else:
            for index, category in enumerate(categories):
                if not isinstance(category, dict):
                    errors.append(f"palette.categories[{index}] must be an object.")
                    continue
                if not isinstance(category.get("name"), str) or not category["name"].strip():
                    errors.append(f"palette.categories[{index}].name must be a non-empty string.")
                if not isinstance(category.get("color"), str) or not _HEX.fullmatch(category["color"]):
                    errors.append(f"palette.categories[{index}].color must be a six-digit HEX color.")
    else:
        errors.append("palette must be an object.")

    geometry = profile.get("geometry", {})
    if isinstance(geometry, dict):
        for key in ("line_width_pt", "axis_line_width_pt", "marker_size_pt", "grid_line_width_pt"):
            value = geometry.get(key)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
                errors.append(f"geometry.{key} must be a positive number.")
    else:
        errors.append("geometry must be an object.")

    layout = profile.get("layout", {})
    if not isinstance(layout, dict):
        errors.append("layout must be an object.")
    export = profile.get("export", {})
    if isinstance(export, dict):
        formats = export.get("formats")
        allowed = {"pdf", "svg", "png", "tif", "tiff"}
        if not isinstance(formats, list) or not formats or any(item not in allowed for item in formats):
            errors.append("export.formats must be a non-empty list using pdf, svg, png, tif, or tiff.")
        dpi = export.get("raster_dpi")
        if not isinstance(dpi, int) or isinstance(dpi, bool) or dpi < 1:
            errors.append("export.raster_dpi must be a positive integer.")
    else:
        errors.append("export must be an object.")

    extraction = profile.get("extraction", {})
    if isinstance(extraction, dict):
        if extraction.get("evidence_level") not in {"visually_inspected", "mixed", "textually_inspected", "estimated"}:
            errors.append("extraction.evidence_level must be visually_inspected, mixed, textually_inspected, or estimated.")
    else:
        errors.append("extraction must be an object.")

    return errors


def load_style_profile(path: str | Path) -> dict[str, Any]:
    """Load a JSON profile and fail clearly if it is malformed or incomplete."""
    profile_path = Path(path)
    try:
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {profile_path}: {exc}") from exc
    errors = validate_style_profile(profile)
    if errors:
        raise ValueError("Invalid reference-style profile:\n- " + "\n- ".join(errors))
    return profile


def color_for_category(profile: dict[str, Any], category: str, index: int = 0) -> str:
    """Return a declared category color, falling back to the profile's role palette."""
    palette = profile["palette"]
    for item in palette.get("categories", []):
        if item.get("name") == category:
            return item["color"]
    fallback_keys = ("primary", "secondary", "accent", "neutral")
    return palette[fallback_keys[index % len(fallback_keys)]]


def matplotlib_rcparams(profile: dict[str, Any]) -> dict[str, Any]:
    """Translate the portable profile subset into Matplotlib rcParams."""
    typography = profile["typography"]
    palette = profile["palette"]
    canvas = profile["canvas"]
    geometry = profile["geometry"]
    export = profile["export"]
    fallbacks = typography.get("fallback_fonts", ["Arial", "Helvetica", "DejaVu Sans"])
    return {
        "font.family": typography.get("font_family", "sans-serif"),
        "font.sans-serif": fallbacks,
        "font.size": typography["base_size_pt"],
        "axes.labelsize": typography["axis_label_size_pt"],
        "axes.titlesize": typography.get("title_size_pt", typography["base_size_pt"]),
        "xtick.labelsize": typography["tick_label_size_pt"],
        "ytick.labelsize": typography["tick_label_size_pt"],
        "legend.fontsize": typography["legend_size_pt"],
        "axes.edgecolor": palette["text"],
        "axes.linewidth": geometry["axis_line_width_pt"],
        "grid.color": palette.get("grid", "#D9DEE5"),
        "grid.linewidth": geometry["grid_line_width_pt"],
        "figure.facecolor": canvas.get("background", palette["background"]),
        "axes.facecolor": canvas.get("background", palette["background"]),
        "savefig.facecolor": canvas.get("background", palette["background"]),
        "savefig.transparent": bool(export.get("transparent_background", False)),
    }


def apply_matplotlib_style(profile: dict[str, Any]) -> None:
    """Apply the profile to Matplotlib. Matplotlib is imported only when requested."""
    try:
        import matplotlib
    except ImportError as exc:
        raise RuntimeError("Matplotlib is required. Install with: python -m pip install matplotlib") from exc
    matplotlib.rcParams.update(matplotlib_rcparams(profile))
