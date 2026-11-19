# General Design Rules for IEEE-Style Scientific Figures

These are cross-domain recommendations. They are not a replacement for the target venue's author instructions.

## 1. One figure, one primary message

A multi-panel figure may contain several related views, but the reader should understand the figure's overall purpose quickly. If a figure is trying to explain system architecture, algorithm order, spatial evidence, and quantitative results at once, consider splitting it.

## 2. Choose visual grammar by scientific purpose

- Structure → architecture diagram, schematic, or model graph.
- Order → flowchart or workflow.
- State → state machine.
- Interaction over time → sequence diagram.
- Measured relationship → plot.
- Spatial evidence → map, image, microscopy, trajectory, or field plot.
- Exact values → table.
- Mechanism → scientific illustration with labels and a clear evidence boundary.

## 3. Layout and reading order

- Use a consistent reading direction.
- Align related blocks, panels, and plot areas.
- Keep enough whitespace around text and symbols.
- Group only elements with a real relationship.
- Put primary inputs and outputs where they are easy to find.
- Avoid crossing connectors and ambiguous junctions.
- Keep repeated lanes, agents, or experimental groups aligned.

## 4. Labels and annotation

- Use concise labels with consistent capitalization.
- Put labels close to the feature, line, or component they describe.
- Define non-obvious abbreviations, symbols, and colors in the caption or legend.
- Include units on axes and dimensions on physical drawings.
- Avoid text that is too small after reduction to final column width.

## 5. Color and accessibility

- Use color only when it communicates information.
- Do not rely on color alone for a critical distinction.
- Use direct labels, marker shapes, line styles, or hatching as secondary cues.
- Check contrast and grayscale legibility.
- Avoid problematic red-green distinctions.
- Keep a semantic mapping stable across related panels.

See references/color-and-typography.md.

## 6. Plot integrity

- Choose a chart type that matches the data and the question.
- Label axes with metric and unit.
- Keep comparable panels on comparable scales.
- Include error bars, confidence intervals, or statistical annotations only when supported.
- Avoid dual axes for unrelated metrics.
- State normalization and baselines.
- Use logarithmic axes only when the scale and interpretation justify them.
- Do not obscure individual data points when their distribution is important.

## 7. Multi-panel figures

- Use consistent panel labels.
- Align panels and maintain common dimensions when comparison is intended.
- Share a legend only if the encoding is shared.
- Keep each panel's scale visible.
- Avoid excessive panel count and tiny labels.
- Explain the role of each panel in the caption.

## 8. Vector and raster output

Prefer vector output for line art, diagrams, text, and plots. Use raster images when the scientific content is inherently pixel-based.

IEEE Author Center guidance gives greater than 300 dpi for non-vector color/grayscale artwork and greater than 600 dpi for black-and-white line art, with common widths of 3.5 in for one column and 7.16 in for two columns. These are baseline references; the target publication's current instructions take precedence.

See references/ieee-publication-baseline.md.

## 9. Copyright and research integrity

Create original diagrams rather than tracing published figures. Preserve the scientific meaning and provenance of data and images. Public accessibility does not automatically grant permission to reuse a figure.

See references/visualization-ethics.md.
