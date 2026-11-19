# Performance plot example

Run:

\`\`\`bash
python plot_sample.py sample_metrics.csv --out figures
\`\`\`

The CSV values are **synthetic demonstration values**, not measurements from the supplied papers
or the user's research. The script creates a separate PDF, SVG, and 450-dpi PNG for each
platform/metric combination. It intentionally does not put ASIC area and FPGA LUT count on the
same axis because those are different units.
