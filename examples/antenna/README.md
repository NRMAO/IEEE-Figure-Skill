# Antenna radiation-pattern example

The Python script reads real measurement or simulation data from a CSV file and creates PDF, SVG, and PNG polar plots. It contains no example measurement values.

Required CSV columns: series, angle_deg, gain_dbi.

Run: python radiation-pattern-template.py your_measurements.csv --out figure_name

Check the target journal's expected angular convention, normalization, polarization, and gain reference before exporting.