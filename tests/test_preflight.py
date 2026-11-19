from pathlib import Path

from PIL import Image

from tools.figure_preflight import (
    check_caption,
    check_palette,
    check_text_contrast,
    contrast_ratio,
    delta_e76,
    parse_length,
    rgb_from_color,
    run_preflight,
    Report,
)

PROFILE = {
    "accepted_formats": [".png", ".tif", ".tiff", ".pdf", ".eps", ".ps"],
    "editable_source_formats": [".svg"],
    "maximum_width_in": 7.16,
    "maximum_height_in": 8.8,
    "minimum_raster_dpi": {"color_grayscale": 300, "black_white_line_art": 600},
    "recommended_min_font_pt": 8,
    "dimension_tolerance_in": 0.15,
    "svg_checks": {"boundary_tolerance_user_units": 0.75},
    "color_checks": {
        "minimum_delta_e76": 12,
        "minimum_grayscale_luminance_difference": 0.1,
        "minimum_text_contrast_ratio": 4.5,
        "cvd_types": [],
    },
}


def test_parse_length_units():
    assert parse_length("1in") == 96
    assert parse_length("72pt") == 96
    assert abs(parse_length("25.4mm") - 96) < 1e-8
    assert parse_length("100%") is None


def test_color_distance_and_contrast():
    black = rgb_from_color("#000000")
    white = rgb_from_color("#FFFFFF")
    assert black and white
    assert contrast_ratio(black, white) == 21
    assert delta_e76(black, white) > 90


def test_caption_missing_is_error():
    report = Report("figure.svg", "test")
    check_caption({}, report)
    assert any(f.code == "CAPTION_MISSING" and f.severity == "error" for f in report.findings)


def test_caption_panel_and_abbreviation_warnings():
    report = Report("figure.svg", "test")
    check_caption({
        "caption": "Fig. 2. Overview of the system.",
        "figure_number": 2,
        "panels": [{"label": "(a)"}],
        "abbreviations": [{"term": "ROI", "definition": "region of interest"}],
    }, report)
    codes = {f.code for f in report.findings}
    assert "CAPTION_PANEL" in codes
    assert "CAPTION_ABBREVIATION" in codes


def test_reused_figure_requires_credit():
    report = Report("figure.svg", "test")
    check_caption({"caption": "Fig. 1. Adapted figure.", "source_reused": True}, report)
    assert any(f.code == "SOURCE_CREDIT_MISSING" for f in report.findings)


def test_low_resolution_png_warns(tmp_path: Path):
    path = tmp_path / "low.png"
    Image.new("RGB", (700, 500), "white").save(path, dpi=(200, 200))
    manifest = {"target_width_in": 3.5, "target_height_in": 2.5, "caption": "Fig. 1. Test."}
    report = run_preflight(path, manifest, PROFILE, "test", True)
    assert any(f.code == "RASTER_RESOLUTION_LOW" for f in report.findings)


def test_missing_figure_is_error(tmp_path: Path):
    report = run_preflight(tmp_path / "missing.svg", {"caption": "Fig. 1. Test."}, PROFILE, "test", True)
    assert report.as_dict()["status"] == "FAIL"


def test_svg_parse_error(tmp_path: Path):
    path = tmp_path / "broken.svg"
    path.write_text("<svg><text>broken", encoding="utf-8")
    report = run_preflight(path, {"caption": "Fig. 1. Test."}, PROFILE, "test", True)
    assert any(f.code == "SVG_PARSE_ERROR" for f in report.findings)


def test_invalid_extension_fails(tmp_path: Path):
    path = tmp_path / "figure.jpg"
    path.write_bytes(b"not a real image")
    report = run_preflight(path, {"caption": "Fig. 1. Test."}, PROFILE, "test", True)
    assert any(f.code == "FORMAT_NOT_ACCEPTED" for f in report.findings)


def test_svg_browser_detects_text_outside_viewbox(tmp_path: Path):
    import importlib.util
    import pytest
    if importlib.util.find_spec("playwright") is None:
        pytest.skip("Playwright is optional")
    from tools.svg_layout import inspect_svg_text
    path = tmp_path / "overflow.svg"
    path.write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="300px" height="100px" viewBox="0 0 300 100">'
        '<text x="280" y="50" font-size="16">This label is outside the right edge</text></svg>',
        encoding="utf-8",
    )
    result = inspect_svg_text(path)
    assert result["textCount"] == 1
    text = result["texts"][0]
    assert text["x2"] > result["viewBox"]["x"] + result["viewBox"]["width"]


def test_palette_flags_low_grayscale_separation():
    profile = {"color_checks": {"minimum_delta_e76": 1, "minimum_grayscale_luminance_difference": 0.1, "cvd_types": []}}
    manifest = {"palette": [
        {"name": "blue", "hex": "#0000FF"},
        {"name": "dark green", "hex": "#006600"},
    ]}
    report = Report("figure.svg", "test")
    check_palette(manifest, profile, report)
    assert any(f.code == "PALETTE_GRAYSCALE" for f in report.findings)


def test_text_contrast_flags_low_contrast():
    report = Report("figure.svg", "test")
    check_text_contrast(
        {"text_samples": [{"name": "small label", "foreground": "#CCCCCC", "background": "#FFFFFF"}]},
        {"color_checks": {"minimum_text_contrast_ratio": 4.5}},
        report,
    )
    assert any(f.code == "TEXT_CONTRAST_LOW" for f in report.findings)


def test_cli_figure_override_is_relative_to_working_directory(tmp_path: Path, monkeypatch):
    import json
    from tools.figure_preflight import main

    monkeypatch.chdir(tmp_path)
    (tmp_path / "manifests").mkdir()
    figure = tmp_path / "figure.svg"
    figure.write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="300px" height="100px" viewBox="0 0 300 100">'
        '<text x="10" y="40" font-size="16">Figure</text></svg>',
        encoding="utf-8",
    )
    manifest = tmp_path / "manifests" / "manifest.json"
    manifest.write_text(json.dumps({"caption": "Fig. 1. Example."}), encoding="utf-8")
    profile = tmp_path / "profile.json"
    profile.write_text(json.dumps(PROFILE), encoding="utf-8")

    code = main([
        "--figure", "figure.svg",
        "--manifest", "manifests/manifest.json",
        "--profile", "profile.json",
        "--skip-browser",
    ])
    assert code == 0
