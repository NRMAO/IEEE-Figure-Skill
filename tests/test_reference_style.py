from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from tools.create_figure_project import create_project
from tools.reference_style import color_for_category, load_style_profile, validate_style_profile


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_PROFILE = ROOT / "templates" / "reference-to-figure" / "style-profile.example.json"


def test_example_reference_profile_is_valid():
    profile = load_style_profile(EXAMPLE_PROFILE)
    assert profile["figure_family"] == "quantitative_plot"
    assert color_for_category(profile, "Control") == "#2468A2"
    assert color_for_category(profile, "Unknown", 1) == profile["palette"]["secondary"]


def test_invalid_profile_color_is_reported():
    profile = json.loads(EXAMPLE_PROFILE.read_text(encoding="utf-8"))
    profile["palette"]["primary"] = "blue"
    errors = validate_style_profile(profile)
    assert any("palette.primary" in error for error in errors)


def test_invalid_profile_dimensions_are_reported():
    profile = json.loads(EXAMPLE_PROFILE.read_text(encoding="utf-8"))
    profile["canvas"]["width_in"] = 0
    errors = validate_style_profile(profile)
    assert any("canvas.width_in" in error for error in errors)


def test_project_scaffolder_creates_editable_files(tmp_path: Path):
    output = create_project(EXAMPLE_PROFILE, tmp_path / "my-figure")
    assert (output / "reference-style-profile.json").exists()
    assert (output / "figure_style.py").exists()
    assert (output / "generate_figure.py").exists()
    assert (output / "README.md").exists()
    assert (output / "data").is_dir()
    assert (output / "output").is_dir()


def test_project_scaffolder_refuses_to_overwrite(tmp_path: Path):
    output = tmp_path / "existing"
    output.mkdir()
    important = output / "keep.txt"
    important.write_text("do not overwrite", encoding="utf-8")
    with pytest.raises(FileExistsError):
        create_project(EXAMPLE_PROFILE, output)
    assert important.read_text(encoding="utf-8") == "do not overwrite"


def test_generated_plot_script_runs_with_user_csv(tmp_path: Path):
    matplotlib = pytest.importorskip("matplotlib")
    output = create_project(EXAMPLE_PROFILE, tmp_path / "plot-project")
    data = output / "data" / "observations.csv"
    data.write_text(
        "time,value,cohort\n0,1.2,Control\n1,1.8,Control\n0,0.9,Treatment\n1,1.4,Treatment\n",
        encoding="utf-8",
    )
    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"
    result = subprocess.run(
        [
            sys.executable,
            str(output / "generate_figure.py"),
            str(data),
            "--x", "time",
            "--y", "value",
            "--group", "cohort",
            "--kind", "line",
            "--output-dir", str(output / "output"),
        ],
        cwd=output,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert (output / "output" / "reference_styled_figure.pdf").exists()
    assert (output / "output" / "reference_styled_figure.svg").exists()
    assert (output / "output" / "reference_styled_figure.png").exists()
