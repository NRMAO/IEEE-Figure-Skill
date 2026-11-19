# Reference-styled figure project

This folder was scaffolded by IEEE-Figure-Skill from an AI-extracted visual style profile.

## Files

- `reference-style-profile.json`: the portable style tokens extracted from the supplied reference.
- `figure_style.py`: validates the profile and maps supported tokens to Matplotlib.
- `generate_figure.py`: editable starter script for CSV-driven line, scatter, and bar plots.
- `data/`: place your own source data here.
- `output/`: generated figure exports.

## Install and run

~~~bash
python -m pip install matplotlib
python generate_figure.py data/your_data.csv --x time --y value --group cohort --kind line
~~~

Change the column names and labels to match your real dataset. The script never fabricates measurements. For architecture diagrams, flowcharts, microscopy composites, or other figure families, ask your Skill-enabled AI to replace or extend `generate_figure.py` with a figure-specific editable Python implementation while retaining the style profile.

Review all generated figures against the source data, the original scientific method, and the target venue's current instructions.
