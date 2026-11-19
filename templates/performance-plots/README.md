# Performance plot template

\`plot_template.py\` expects a tidy CSV with columns:

\`platform,design,metric,value,unit\`

It creates a separate figure for each platform/metric/unit group and exports PDF, SVG, and 450-dpi
PNG. This avoids mixing incompatible metrics such as ASIC area and FPGA LUT count on one axis.

Run:

\`\`\`bash
python plot_template.py results.csv --out figures
\`\`\`

Dependencies: Python 3, pandas, and Matplotlib.
