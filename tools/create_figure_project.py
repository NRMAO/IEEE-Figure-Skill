"""Scaffold an editable figure project from an AI-extracted style profile."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

try:
    from .reference_style import load_style_profile
except ImportError:  # Support direct execution: python tools/create_figure_project.py
    from reference_style import load_style_profile


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = REPOSITORY_ROOT / "templates" / "reference-to-figure"


def create_project(profile_path: str | Path, output_dir: str | Path) -> Path:
    """Create a non-destructive, editable project directory from a validated profile."""
    source_profile = Path(profile_path).expanduser().resolve()
    destination = Path(output_dir).expanduser().resolve()
    profile = load_style_profile(source_profile)

    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise FileExistsError(
            f"Output path already exists and is not empty: {destination}. "
            "Choose a new directory to avoid overwriting user files."
        )

    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_profile, destination / "reference-style-profile.json")
    shutil.copy2(REPOSITORY_ROOT / "tools" / "reference_style.py", destination / "figure_style.py")
    shutil.copy2(TEMPLATE_ROOT / "generate_figure.py", destination / "generate_figure.py")
    (destination / "README.md").write_text(
        (TEMPLATE_ROOT / "project-README.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (destination / "data").mkdir(exist_ok=True)
    (destination / "output").mkdir(exist_ok=True)
    (destination / "data" / ".gitkeep").write_text("", encoding="utf-8")
    (destination / "output" / ".gitkeep").write_text("", encoding="utf-8")
    (destination / "profile-summary.json").write_text(
        json.dumps({
            "profile_name": profile["profile_name"],
            "figure_family": profile["figure_family"],
            "extraction_evidence_level": profile["extraction"]["evidence_level"],
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create an editable Python figure project from an extracted reference-style JSON profile."
    )
    parser.add_argument("--profile", required=True, help="Path to the AI-extracted style-profile JSON file.")
    parser.add_argument("--output", required=True, help="New or empty directory for the generated project.")
    args = parser.parse_args()
    project = create_project(args.profile, args.output)
    print(f"Created figure project: {project}")
    print("Next: edit generate_figure.py for your scientific content, then run it with your own CSV data.")


if __name__ == "__main__":
    main()
