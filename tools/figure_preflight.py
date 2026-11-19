#!/usr/bin/env python3
"""Automated preflight checks for publication-oriented scientific figures.

The tool reports objective file/layout issues and manifest-driven checks. It cannot
replace scientific peer review, a human visual inspection, or the target venue's live
submission instructions.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageColor
except ImportError:  # pragma: no cover - dependency error is reported by CLI
    Image = None  # type: ignore[assignment]
    ImageColor = None  # type: ignore[assignment]

try:
    import pymupdf as fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    fitz = None  # type: ignore[assignment]

try:
    from colorspacious import cspace_convert
except ImportError:  # pragma: no cover
    cspace_convert = None  # type: ignore[assignment]

try:
    from .svg_layout import inspect_svg_text
except ImportError:  # support direct script execution
    from svg_layout import inspect_svg_text

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILE = ROOT / "profiles" / "ieee-baseline.json"


@dataclass
class Finding:
    severity: str
    code: str
    message: str
    location: str | None = None


class Report:
    def __init__(self, figure: str, profile: str):
        self.figure = figure
        self.profile = profile
        self.findings: list[Finding] = []
        self.metrics: dict[str, Any] = {}

    def add(self, severity: str, code: str, message: str, location: str | None = None) -> None:
        self.findings.append(Finding(severity, code, message, location))

    def as_dict(self) -> dict[str, Any]:
        counts = {level: sum(f.severity == level for f in self.findings) for level in ("error", "warning", "info")}
        status = "FAIL" if counts["error"] else ("WARN" if counts["warning"] else "PASS")
        return {
            "figure": self.figure,
            "profile": self.profile,
            "status": status,
            "counts": counts,
            "metrics": self.metrics,
            "findings": [asdict(f) for f in self.findings],
        }


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def parse_length(value: str | None) -> float | None:
    """Convert an SVG absolute length to CSS px (96 px/in); percentages are unsupported."""
    if not value:
        return None
    match = re.fullmatch(r"\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*(px|pt|pc|in|cm|mm)?\s*", value)
    if not match:
        return None
    number = float(match.group(1))
    unit = match.group(2) or "px"
    factors = {"px": 1.0, "pt": 96 / 72, "pc": 16.0, "in": 96.0, "cm": 96 / 2.54, "mm": 96 / 25.4}
    return number * factors[unit]


def parse_physical_inches(value: str | None) -> float | None:
    """Return inches only when the SVG length uses an explicit physical unit."""
    if not value:
        return None
    match = re.fullmatch(r"\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*(in|pt|pc|cm|mm)\s*", value)
    if not match:
        return None
    px = parse_length(value)
    return px / 96 if px is not None else None


def rgb_from_color(value: str) -> tuple[float, float, float] | None:
    if ImageColor is None:
        return None
    raw = value.strip()
    if raw.lower() in {"none", "transparent", "currentcolor", "inherit", "initial", "unset"} or raw.startswith("url("):
        return None
    try:
        rgb = ImageColor.getrgb(raw)
    except Exception:
        return None
    if len(rgb) == 4:
        rgb = rgb[:3]
    return tuple(channel / 255 for channel in rgb)


def rgb_to_lab(rgb: tuple[float, float, float]) -> tuple[float, float, float]:
    def linear(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = map(linear, rgb)
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    y = (0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / 1.00000
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883
    def f(t: float) -> float:
        return t ** (1 / 3) if t > 0.008856451679 else (7.787037037 * t) + (16 / 116)
    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e76(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    la, lb = rgb_to_lab(a), rgb_to_lab(b)
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(la, lb)))


def relative_luminance(rgb: tuple[float, float, float]) -> float:
    def linear(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = map(linear, rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(foreground: tuple[float, float, float], background: tuple[float, float, float]) -> float:
    a, b = sorted((relative_luminance(foreground), relative_luminance(background)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def check_caption(manifest: dict[str, Any], report: Report) -> None:
    caption = str(manifest.get("caption", "")).strip()
    if not caption:
        report.add("error", "CAPTION_MISSING", "A manifest was supplied but its caption field is empty.")
        return

    figure_number = manifest.get("figure_number")
    if figure_number is not None:
        patterns = [rf"\bFig\.\s*{re.escape(str(figure_number))}\b", rf"\bFigure\s*{re.escape(str(figure_number))}\b"]
        if not any(re.search(pattern, caption, re.IGNORECASE) for pattern in patterns):
            report.add("warning", "CAPTION_NUMBER", f"Caption does not visibly identify figure number {figure_number} (expected e.g. 'Fig. {figure_number}.').")

    for panel in manifest.get("panels", []):
        label = str(panel.get("label", "")).strip() if isinstance(panel, dict) else str(panel).strip()
        if label and label not in caption:
            report.add("warning", "CAPTION_PANEL", f"Panel label {label!r} is not mentioned in the caption.")

    for field, code, label in (
        ("abbreviations", "CAPTION_ABBREVIATION", "abbreviation"),
        ("symbols", "CAPTION_SYMBOL", "symbol"),
        ("color_encodings", "CAPTION_COLOR", "color encoding"),
    ):
        for item in manifest.get(field, []):
            if not isinstance(item, dict):
                report.add("warning", code, f"Malformed {label} entry; expected an object with term and definition.")
                continue
            term = str(item.get("term", "")).strip()
            definition = str(item.get("definition", "")).strip()
            if not term or not definition:
                report.add("warning", code, f"A {label} entry is missing its term or definition.")
                continue
            if term.casefold() not in caption.casefold():
                report.add("warning", code, f"{label.capitalize()} {term!r} is listed in the manifest but not found in the caption.")
            elif definition.casefold() not in caption.casefold():
                report.add("warning", code, f"Definition for {label} {term!r} is not found in the caption.")

    for term in manifest.get("required_caption_terms", []):
        if str(term).casefold() not in caption.casefold():
            report.add("warning", "CAPTION_REQUIRED_TERM", f"Required caption term {term!r} is missing.")

    if manifest.get("source_reused") is True:
        source_credit = str(manifest.get("source_credit", "")).strip()
        if not source_credit:
            report.add("error", "SOURCE_CREDIT_MISSING", "The manifest marks the figure as reused/adapted but provides no source credit. Check permission and the target venue's credit-line rules.")
        elif source_credit.casefold() not in caption.casefold():
            report.add("warning", "SOURCE_CREDIT_NOT_IN_CAPTION", "A source credit is declared in the manifest but its text is not present in the caption. Verify where the target venue requires the credit line.")

    report.metrics["caption_characters"] = len(caption)
    report.add("info", "CAPTION_HEURISTIC", "Caption checks validate manifest-declared items only; they cannot determine whether the scientific explanation is complete or accurate.")


def check_palette(manifest: dict[str, Any], profile: dict[str, Any], report: Report) -> None:
    palette = manifest.get("palette", [])
    if not palette:
        report.add("info", "PALETTE_NOT_DECLARED", "No semantic palette was declared; color-distinguishability checks were skipped. Add manifest.palette entries for categories that readers must distinguish.")
        return

    parsed: list[tuple[str, tuple[float, float, float]]] = []
    for item in palette:
        if not isinstance(item, dict) or not item.get("name") or not item.get("hex"):
            report.add("warning", "PALETTE_ENTRY_INVALID", "Each palette entry must contain name and hex fields.")
            continue
        rgb = rgb_from_color(str(item["hex"]))
        if rgb is None:
            report.add("warning", "PALETTE_COLOR_INVALID", f"Could not parse palette color {item.get('hex')!r}.")
            continue
        parsed.append((str(item["name"]), rgb))

    min_delta = float(profile.get("color_checks", {}).get("minimum_delta_e76", 12.0))
    min_gray = float(profile.get("color_checks", {}).get("minimum_grayscale_luminance_difference", 0.10))
    pairs_checked = 0
    for i, (name_a, rgb_a) in enumerate(parsed):
        for name_b, rgb_b in parsed[i + 1 :]:
            pairs_checked += 1
            de = delta_e76(rgb_a, rgb_b)
            gray_gap = abs(relative_luminance(rgb_a) - relative_luminance(rgb_b))
            if de < min_delta:
                report.add("warning", "PALETTE_SIMILAR", f"Palette colors {name_a!r} and {name_b!r} are perceptually close (CIE76 ΔE={de:.1f}; heuristic threshold {min_delta:.1f}).")
            if gray_gap < min_gray:
                report.add("warning", "PALETTE_GRAYSCALE", f"Palette colors {name_a!r} and {name_b!r} have similar grayscale luminance (difference={gray_gap:.3f}); add marker/line-style/pattern cues or revise the palette.")

    report.metrics["palette_colors"] = len(parsed)
    report.metrics["palette_pairs_checked"] = pairs_checked

    if cspace_convert is None:
        report.add("info", "CVD_CHECK_SKIPPED", "Color-vision-deficiency simulation requires colorspacious; install project dependencies to enable it.")
        return

    cvd_types = profile.get("color_checks", {}).get("cvd_types", ["protanomaly", "deuteranomaly", "tritanomaly"])
    for cvd_type in cvd_types:
        try:
            import numpy as np
            values = np.array([rgb for _, rgb in parsed], dtype=float)
            simulated = cspace_convert(values, "sRGB1", {"name": "sRGB1+CVD", "cvd_type": cvd_type, "severity": 100})
            simulated = np.clip(simulated, 0, 1)
            for i in range(len(parsed)):
                for j in range(i + 1, len(parsed)):
                    distance = delta_e76(tuple(simulated[i]), tuple(simulated[j]))
                    if distance < min_delta:
                        report.add("warning", "PALETTE_CVD", f"{parsed[i][0]!r} and {parsed[j][0]!r} may be difficult to distinguish under {cvd_type} simulation (CIE76 ΔE={distance:.1f}).")
        except Exception as exc:
            report.add("info", "CVD_CHECK_SKIPPED", f"Could not run {cvd_type} simulation: {exc}")


def check_text_contrast(manifest: dict[str, Any], profile: dict[str, Any], report: Report) -> None:
    samples = manifest.get("text_samples", [])
    if not samples:
        report.add("info", "TEXT_CONTRAST_NOT_DECLARED", "No foreground/background text samples were declared; text contrast checks were skipped.")
        return
    threshold = float(profile.get("color_checks", {}).get("minimum_text_contrast_ratio", 4.5))
    for sample in samples:
        label = str(sample.get("name", "text"))
        fg = rgb_from_color(str(sample.get("foreground", "")))
        bg = rgb_from_color(str(sample.get("background", "")))
        if fg is None or bg is None:
            report.add("warning", "TEXT_CONTRAST_INVALID", f"Could not parse foreground/background colors for {label!r}.")
            continue
        ratio = contrast_ratio(fg, bg)
        if ratio < threshold:
            report.add("warning", "TEXT_CONTRAST_LOW", f"Text sample {label!r} has contrast ratio {ratio:.2f}:1, below the configurable {threshold:.1f}:1 screening heuristic.")


def check_svg(path: Path, manifest: dict[str, Any], profile: dict[str, Any], report: Report, skip_browser: bool) -> None:
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        report.add("error", "SVG_PARSE_ERROR", f"SVG is not well-formed XML: {exc}")
        return
    tag = root.tag.rsplit("}", 1)[-1].lower()
    if tag != "svg":
        report.add("error", "SVG_ROOT_INVALID", "The document root is not an <svg> element.")
        return

    view_box = root.attrib.get("viewBox") or root.attrib.get("viewbox")
    if view_box:
        try:
            vb = [float(x) for x in re.split(r"[ ,]+", view_box.strip())]
            if len(vb) != 4 or vb[2] <= 0 or vb[3] <= 0:
                raise ValueError
            report.metrics["svg_viewBox"] = vb
        except ValueError:
            report.add("error", "SVG_VIEWBOX_INVALID", f"Invalid SVG viewBox: {view_box!r}.")
    else:
        report.add("warning", "SVG_VIEWBOX_MISSING", "SVG has no viewBox; scaling and text-boundary checks may be unreliable.")

    width_px = parse_length(root.attrib.get("width"))
    height_px = parse_length(root.attrib.get("height"))
    physical_width = parse_physical_inches(root.attrib.get("width"))
    physical_height = parse_physical_inches(root.attrib.get("height"))
    if width_px and height_px:
        report.metrics["svg_intrinsic_canvas_px"] = [round(width_px, 1), round(height_px, 1)]
    target_width = manifest.get("target_width_in")
    target_height = manifest.get("target_height_in")
    final_width = float(target_width) if target_width else physical_width
    final_height = float(target_height) if target_height else physical_height
    if final_width:
        report.metrics["svg_final_width_in"] = round(final_width, 3)
    if final_height:
        report.metrics["svg_final_height_in"] = round(final_height, 3)
    max_width = float(profile.get("maximum_width_in", 7.16))
    max_height = float(profile.get("maximum_height_in", 8.8))
    if final_width and final_width > max_width + 0.01:
        report.add("warning", "FIGURE_WIDTH_EXCEEDS_PROFILE", f"SVG final width is {final_width:.2f} in, above the profile maximum {max_width:.2f} in.")
    if final_height and final_height > max_height + 0.01:
        report.add("warning", "FIGURE_HEIGHT_EXCEEDS_PROFILE", f"SVG final height is {final_height:.2f} in, above the profile maximum {max_height:.2f} in.")
    if not final_width or not final_height:
        report.add("info", "SVG_FINAL_SIZE_PARTIAL", "SVG intrinsic pixel dimensions are not treated as final print dimensions. Set target_width_in/target_height_in in the manifest, or use explicit physical units, to check final size.")

    text_nodes = [node for node in root.iter() if node.tag.rsplit("}", 1)[-1].lower() == "text"]
    text_content = " ".join("".join(node.itertext()).strip() for node in text_nodes)
    report.metrics["svg_text_characters"] = len(text_content)
    for panel in manifest.get("panels", []):
        label = str(panel.get("label", "")).strip() if isinstance(panel, dict) else str(panel).strip()
        if label and label not in text_content:
            report.add("warning", "PANEL_LABEL_MISSING_IN_FIGURE", f"Panel label {label!r} is declared in the manifest but not found in SVG text.")
    for term in manifest.get("required_figure_terms", []):
        if str(term).casefold() not in text_content.casefold():
            report.add("warning", "FIGURE_REQUIRED_TERM_MISSING", f"Required figure label {term!r} is not found in SVG text.")
    for term in manifest.get("legend_labels", []):
        if str(term).casefold() not in text_content.casefold():
            report.add("warning", "LEGEND_LABEL_MISSING", f"Declared legend label {term!r} is not found in SVG text.")

    if skip_browser:
        report.add("info", "SVG_BROWSER_CHECK_SKIPPED", "Browser-based SVG text-boundary inspection was disabled.")
        return
    try:
        result = inspect_svg_text(path, manifest.get("target_width_in"))
        if result.get("error"):
            report.add("warning", "SVG_TEXT_GEOMETRY_UNAVAILABLE", result["error"])
            return
        vb = result["viewBox"]
        tol = float(profile.get("svg_checks", {}).get("boundary_tolerance_user_units", 0.75))
        overflow = []
        font_threshold = float(profile.get("recommended_min_font_pt", 8.0))
        small_text = []
        for item in result.get("texts", []):
            if (item["x1"] < vb["x"] - tol or item["y1"] < vb["y"] - tol or
                item["x2"] > vb["x"] + vb["width"] + tol or item["y2"] > vb["y"] + vb["height"] + tol):
                overflow.append(item)
            font_pt = item.get("font_size_pt_at_target_width")
            if font_pt is not None and font_pt < font_threshold:
                small_text.append((item.get("text", "")[:70], font_pt))
        report.metrics["svg_text_elements_checked"] = result.get("textCount", 0)
        report.metrics["svg_text_outside_viewBox"] = len(overflow)
        for item in overflow:
            report.add("warning", "SVG_TEXT_OVERFLOW", f"Text appears outside the SVG viewBox: {item['text']!r} (bounds x={item['x1']:.1f}..{item['x2']:.1f}, y={item['y1']:.1f}..{item['y2']:.1f}).")
        for text, font_pt in small_text:
            report.add("warning", "SVG_TEXT_SMALL", f"Text {text!r} is approximately {font_pt:.1f} pt at the requested width; configurable screening threshold is {font_threshold:.1f} pt.")
        if not overflow:
            report.add("info", "SVG_TEXT_BOUNDS_PASS", f"Checked {result.get('textCount', 0)} visible SVG text elements; none extends beyond the root viewBox.")
    except Exception as exc:
        report.add("warning", "SVG_BROWSER_CHECK_UNAVAILABLE", f"Could not run browser-based SVG text inspection: {exc}")


def get_tiff_dpi(image: Any) -> tuple[float, float] | None:
    info = getattr(image, "info", {})
    dpi = info.get("dpi")
    if dpi and len(dpi) >= 2 and all(float(v) > 0 for v in dpi[:2]):
        return float(dpi[0]), float(dpi[1])
    tags = getattr(image, "tag_v2", None)
    if tags:
        try:
            xres, yres = float(tags.get(282)), float(tags.get(283))
            unit = int(tags.get(296, 2))
            if unit == 3:
                xres, yres = xres * 2.54, yres * 2.54
            if unit in (2, 3) and xres > 0 and yres > 0:
                return xres, yres
        except (TypeError, ValueError, ZeroDivisionError):
            pass
    return None


def resolution_threshold(profile: dict[str, Any], artwork_type: str) -> float:
    mapping = profile.get("minimum_raster_dpi", {})
    if artwork_type == "black_white_line_art":
        return float(mapping.get("black_white_line_art", 600))
    return float(mapping.get("color_grayscale", 300))


def check_resolution(dpi_x: float, dpi_y: float, artwork_type: str, profile: dict[str, Any], report: Report, location: str) -> None:
    threshold = resolution_threshold(profile, artwork_type)
    report.metrics.setdefault("raster_resolution_checks", []).append({"location": location, "dpi_x": round(dpi_x, 1), "dpi_y": round(dpi_y, 1), "threshold_dpi": threshold})
    if dpi_x <= threshold or dpi_y <= threshold:
        report.add("warning", "RASTER_RESOLUTION_LOW", f"{location} is {dpi_x:.1f} × {dpi_y:.1f} dpi; profile guidance is greater than {threshold:.0f} dpi for {artwork_type}.", location)


def check_raster(path: Path, manifest: dict[str, Any], profile: dict[str, Any], report: Report) -> None:
    if Image is None:
        report.add("error", "PILLOW_MISSING", "Pillow is required to inspect PNG/TIFF dimensions and resolution.")
        return
    try:
        with Image.open(path) as im:
            width_px, height_px = im.size
            dpi = get_tiff_dpi(im)
            report.metrics["pixel_dimensions"] = [width_px, height_px]
            report.metrics["raster_format"] = im.format
            report.add("info", "RASTER_TEXT_CHECK_LIMITED", "Text clipping and panel-label extraction are not checked for raster-only figures; inspect the image at final print size.")
            if dpi:
                report.metrics["metadata_dpi"] = [round(dpi[0], 1), round(dpi[1], 1)]
            target_w = float(manifest["target_width_in"]) if manifest.get("target_width_in") else None
            target_h = float(manifest["target_height_in"]) if manifest.get("target_height_in") else None
            effective = None
            if target_w and target_h:
                effective = (width_px / target_w, height_px / target_h)
            elif target_w:
                effective = (width_px / target_w, width_px / target_w)
            elif target_h:
                effective = (height_px / target_h, height_px / target_h)
            elif dpi:
                effective = dpi
            if effective:
                check_resolution(effective[0], effective[1], str(manifest.get("artwork_type", "color_grayscale")), profile, report, path.name)
                final_w = target_w if target_w else width_px / effective[0]
                final_h = target_h if target_h else height_px / effective[1]
                if final_w > float(profile.get("maximum_width_in", 7.16)) + 0.01:
                    report.add("warning", "FIGURE_WIDTH_EXCEEDS_PROFILE", f"Raster final width is {final_w:.2f} in, above the profile maximum.")
                if final_h > float(profile.get("maximum_height_in", 8.8)) + 0.01:
                    report.add("warning", "FIGURE_HEIGHT_EXCEEDS_PROFILE", f"Raster final height is {final_h:.2f} in, above the profile maximum.")
            else:
                report.add("warning", "RASTER_DPI_UNKNOWN", "No usable DPI metadata or target physical width/height was supplied; effective print resolution cannot be verified.")
    except Exception as exc:
        report.add("error", "RASTER_READ_ERROR", f"Could not read raster image: {exc}")


def check_pdf(path: Path, manifest: dict[str, Any], profile: dict[str, Any], report: Report) -> None:
    if fitz is None:
        report.add("error", "PYMUPDF_MISSING", "PyMuPDF is required to inspect PDF dimensions, embedded images, and fonts.")
        return
    try:
        doc = fitz.open(path)
    except Exception as exc:
        report.add("error", "PDF_READ_ERROR", f"Could not open PDF: {exc}")
        return
    try:
        if doc.page_count == 0:
            report.add("error", "PDF_EMPTY", "PDF contains no pages.")
            return
        if doc.page_count > 1:
            report.add("warning", "PDF_MULTIPAGE", f"PDF has {doc.page_count} pages; verify whether the submission expects one figure per file.")
        page = doc[0]
        width_in, height_in = page.rect.width / 72, page.rect.height / 72
        report.metrics["pdf_page_count"] = doc.page_count
        report.metrics["pdf_page_size_in"] = [round(width_in, 3), round(height_in, 3)]
        max_width = float(profile.get("maximum_width_in", 7.16))
        max_height = float(profile.get("maximum_height_in", 8.8))
        if width_in > max_width + 0.01:
            report.add("warning", "FIGURE_WIDTH_EXCEEDS_PROFILE", f"PDF page width is {width_in:.2f} in, above profile maximum {max_width:.2f} in.")
        if height_in > max_height + 0.01:
            report.add("warning", "FIGURE_HEIGHT_EXCEEDS_PROFILE", f"PDF page height is {height_in:.2f} in, above profile maximum {max_height:.2f} in.")
        tolerance = float(profile.get("dimension_tolerance_in", 0.15))
        if manifest.get("target_width_in"):
            expected = float(manifest["target_width_in"])
            if abs(width_in - expected) > tolerance:
                report.add("warning", "TARGET_WIDTH_MISMATCH", f"PDF width {width_in:.2f} in differs from requested {expected:.2f} in by more than {tolerance:.2f} in.")
        if manifest.get("target_height_in"):
            expected_h = float(manifest["target_height_in"])
            if abs(height_in - expected_h) > tolerance:
                report.add("warning", "TARGET_HEIGHT_MISMATCH", f"PDF height {height_in:.2f} in differs from requested {expected_h:.2f} in by more than {tolerance:.2f} in.")

        artwork_type = str(manifest.get("artwork_type", "color_grayscale"))
        image_count = 0
        for pageno in range(doc.page_count):
            p = doc[pageno]
            for index, image in enumerate(p.get_image_info(xrefs=True)):
                bbox = fitz.Rect(image.get("bbox", (0, 0, 0, 0)))
                if bbox.width <= 0 or bbox.height <= 0:
                    continue
                dpi_x = float(image["width"]) / (bbox.width / 72)
                dpi_y = float(image["height"]) / (bbox.height / 72)
                check_resolution(dpi_x, dpi_y, artwork_type, profile, report, f"PDF page {pageno + 1} embedded image {index + 1}")
                image_count += 1
        report.metrics["pdf_embedded_image_instances"] = image_count

        pdf_text_parts: list[str] = []
        for pageno in range(doc.page_count):
            p = doc[pageno]
            page_rect = p.rect
            for block in p.get_text("dict").get("blocks", []):
                if block.get("type") != 0:
                    continue
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        text_value = str(span.get("text", "")).strip()
                        if text_value:
                            pdf_text_parts.append(text_value)
                        bbox = fitz.Rect(span.get("bbox", (0, 0, 0, 0)))
                        tol = 0.75
                        if (bbox.x0 < page_rect.x0 - tol or bbox.y0 < page_rect.y0 - tol or
                            bbox.x1 > page_rect.x1 + tol or bbox.y1 > page_rect.y1 + tol):
                            report.add("warning", "PDF_TEXT_OUTSIDE_PAGE", f"PDF text {text_value[:70]!r} extends beyond the page boundary.")
                        font_pt = float(span.get("size", 0) or 0)
                        min_font = float(profile.get("recommended_min_font_pt", 8.0))
                        if font_pt and font_pt < min_font:
                            report.add("warning", "PDF_TEXT_SMALL", f"PDF text {text_value[:70]!r} is {font_pt:.1f} pt, below the configurable {min_font:.1f} pt screening threshold.")
        pdf_text = " ".join(pdf_text_parts)
        report.metrics["pdf_text_characters"] = len(pdf_text)
        for panel in manifest.get("panels", []):
            label = str(panel.get("label", "")).strip() if isinstance(panel, dict) else str(panel).strip()
            if label and label not in pdf_text:
                report.add("warning", "PANEL_LABEL_MISSING_IN_FIGURE", f"Panel label {label!r} is declared in the manifest but not found in PDF text.")
        for term in manifest.get("required_figure_terms", []):
            if str(term).casefold() not in pdf_text.casefold():
                report.add("warning", "FIGURE_REQUIRED_TERM_MISSING", f"Required figure label {term!r} is not found in PDF text.")
        for term in manifest.get("legend_labels", []):
            if str(term).casefold() not in pdf_text.casefold():
                report.add("warning", "LEGEND_LABEL_MISSING", f"Declared legend label {term!r} is not found in PDF text.")

        font_records: list[dict[str, Any]] = []
        seen_fonts: set[tuple[int, str]] = set()
        for pageno in range(doc.page_count):
            for font in doc[pageno].get_fonts(full=True):
                xref = int(font[0])
                basefont = str(font[3]) if len(font) > 3 else "unknown"
                key = (xref, basefont)
                if key in seen_fonts:
                    continue
                seen_fonts.add(key)
                if xref == 0:
                    font_records.append({"font": basefont, "embedded": None})
                    continue
                try:
                    extracted = doc.extract_font(xref)
                    embedded = bool(extracted and len(extracted) >= 4 and extracted[3])
                except Exception:
                    embedded = False
                font_records.append({"font": basefont, "embedded": embedded})
                if not embedded:
                    report.add("warning", "PDF_FONT_NOT_EMBEDDED", f"PDF font {basefont!r} may not be embedded. Embed the font or convert text to outlines, then recheck.")
        report.metrics["pdf_fonts"] = font_records
        if not font_records:
            report.add("info", "PDF_NO_FONT_OBJECTS", "No PDF font resources were found; text may be outlined or the PDF may be image-only. Visual inspection is still required.")
    finally:
        doc.close()


def check_file(path: Path, manifest: dict[str, Any], profile: dict[str, Any], report: Report, skip_browser: bool) -> None:
    if not path.exists() or not path.is_file():
        report.add("error", "FIGURE_FILE_MISSING", f"Figure file does not exist: {path}")
        return
    ext = path.suffix.lower()
    accepted = {str(x).lower() for x in profile.get("accepted_formats", [])}
    source_formats = {str(x).lower() for x in profile.get("editable_source_formats", [])}
    if ext not in accepted and ext not in source_formats:
        report.add("error", "FORMAT_NOT_ACCEPTED", f"File extension {ext!r} is neither an accepted submission format nor a declared editable source format.")
        return
    if ext in source_formats and ext not in accepted:
        report.add("info", "EDITABLE_SOURCE_ONLY", f"{ext.upper()} is treated as an editable working source, not an accepted final submission format in this profile. Export a permitted PDF/EPS/PS/PNG/TIFF file for submission.")
    report.metrics["file_size_bytes"] = path.stat().st_size
    if path.stat().st_size == 0:
        report.add("error", "FIGURE_FILE_EMPTY", "Figure file is empty.")
        return
    if ext == ".svg":
        check_svg(path, manifest, profile, report, skip_browser)
    elif ext in {".png", ".tif", ".tiff"}:
        check_raster(path, manifest, profile, report)
    elif ext == ".pdf":
        check_pdf(path, manifest, profile, report)
    elif ext in {".eps", ".ps"}:
        report.add("warning", "FORMAT_TECHNICAL_CHECK_LIMITED", f"{ext.upper()} is an accepted format in the profile, but this version does not parse its bounding box, fonts, or embedded raster resolution. Convert to PDF for deeper preflight or use Ghostscript-based validation.")


def run_preflight(figure: Path, manifest: dict[str, Any], profile: dict[str, Any], profile_name: str, skip_browser: bool, manifest_provided: bool = True) -> Report:
    report = Report(str(figure), profile_name)
    check_file(figure, manifest, profile, report, skip_browser)
    if manifest_provided:
        check_caption(manifest, report)
        check_palette(manifest, profile, report)
        check_text_contrast(manifest, profile, report)
    else:
        report.add("info", "MANIFEST_NOT_PROVIDED", "No sidecar manifest was supplied; caption, semantic palette, and declared text-contrast checks were skipped.")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run automated preflight checks on an IEEE-style research figure.")
    parser.add_argument("--figure", help="Figure file path; may be supplied in the manifest instead.")
    parser.add_argument("--manifest", help="JSON sidecar describing caption, panels, palette, and target size.")
    parser.add_argument("--profile", default=str(DEFAULT_PROFILE), help="Journal/profile JSON. Defaults to the repository IEEE baseline profile.")
    parser.add_argument("--report", help="Optional path to write a machine-readable JSON report.")
    parser.add_argument("--skip-browser", action="store_true", help="Skip Chromium-based SVG text-boundary checks.")
    parser.add_argument("--strict", action="store_true", help="Return a failing exit code when warnings are present.")
    args = parser.parse_args(argv)

    manifest: dict[str, Any] = {}
    manifest_path = Path(args.manifest).resolve() if args.manifest else None
    if manifest_path:
        try:
            manifest = load_json(manifest_path)
        except Exception as exc:
            print(f"ERROR: cannot load manifest: {exc}", file=sys.stderr)
            return 2

    if args.figure:
        # Explicit CLI paths are relative to the caller's current working directory.
        figure_path = Path(args.figure).resolve()
    else:
        figure_arg = manifest.get("file")
        if not figure_arg:
            parser.error("Provide --figure or a manifest containing 'file'.")
        figure_path = Path(figure_arg)
        if not figure_path.is_absolute():
            figure_path = (manifest_path.parent / figure_path).resolve() if manifest_path else figure_path.resolve()

    profile_path = Path(args.profile).resolve()
    try:
        profile = load_json(profile_path)
    except Exception as exc:
        print(f"ERROR: cannot load profile: {exc}", file=sys.stderr)
        return 2

    report = run_preflight(figure_path, manifest, profile, str(profile_path), args.skip_browser, manifest_provided=bool(manifest_path))
    result = report.as_dict()
    print(f"{result['status']}: {figure_path}")
    print(f"Errors: {result['counts']['error']} | Warnings: {result['counts']['warning']} | Info: {result['counts']['info']}")
    for item in result["findings"]:
        prefix = {"error": "ERROR", "warning": "WARN", "info": "INFO"}[item["severity"]]
        print(f"[{prefix}] {item['code']}: {item['message']}")
    if args.report:
        report_path = Path(args.report).resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"JSON report: {report_path}")
    if result["counts"]["error"]:
        return 1
    if args.strict and result["counts"]["warning"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
