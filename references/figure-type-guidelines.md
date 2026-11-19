# Figure-Type Guidelines

## 1. System and architecture diagrams

Use when the reader needs to understand components, boundaries, and relationships.

- Show system boundaries and the main data/control/power paths.
- Group components only when the grouping has a real scientific or engineering meaning.
- Distinguish physical objects from logical functions.
- Label interfaces, units, protocols, and direction.
- Use a separate detailed view when the overview becomes crowded.
- Keep a consistent abstraction level within one panel.

## 2. Block diagrams and schematics

Use when the internal organization or signal path matters.

- Prefer conventional symbols for circuits and recognized symbols for common operations.
- Preserve actual port and signal connectivity.
- Mark buses, dimensions, polarities, grounds, reference nodes, and clock/reset semantics.
- Use explicit junction dots when wires connect.
- Do not infer a transistor-level or gate-level circuit from a conceptual description.

## 3. Algorithms, flowcharts, state machines, and sequence diagrams

These are not interchangeable:

- **Flowchart:** ordered operations and decision branches.
- **State machine:** allowed states and event-triggered transitions.
- **Sequence diagram:** time-ordered interactions among actors or modules.
- **Workflow:** stages in an experimental or analytical procedure.

Label every decision branch. Show loop conditions and termination. Keep the number of crossing arrows small. Do not invent timing or transitions that are absent from the source.

## 4. AI/ML model and data-pipeline diagrams

- Separate input data, preprocessing, model components, feature fusion, prediction heads, and outputs.
- Use repeated shapes for repeated blocks and label shared weights or parameter sharing only when true.
- Distinguish training and inference paths.
- Label tensor dimensions only when they are known and useful.
- Keep loss functions and evaluation metrics separate from the forward inference path.
- Avoid decorative pseudo-3D stacks that obscure tensor flow.

## 5. Experimental setup and measurement geometry

- Show the instrument, sample, sensor/probe, source, detector, and relevant connections.
- Include physical dimensions and coordinate axes when necessary.
- Label acquisition settings, measurement distance, frequency, orientation, and reference planes when relevant.
- Use a photograph for real apparatus and a schematic for hidden or abstract geometry; combine them in separate aligned panels if both are needed.
- Mark conceptual geometry as not to scale when appropriate.

## 6. Scientific and biomedical illustrations

- Use a scientifically appropriate level of anatomical, cellular, molecular, or material detail.
- Label structures clearly and keep labels outside dense regions where possible.
- Use consistent colors for the same structures across panels.
- Include a legend for non-obvious colors, arrows, and symbols.
- Do not use decorative anatomy or cellular details that imply unsupported biology.
- For microscopy and medical images, preserve the original data and follow the rules in references/visualization-ethics.md.

## 7. Quantitative plots

Choose the plot based on the data and scientific question:

- **Line plot:** continuous trends, time series, frequency response, or parameter sweeps.
- **Scatter plot:** relationships between paired observations.
- **Bar plot:** discrete category summaries; show individual observations when useful and appropriate.
- **Box/violin plot:** distributions across groups; define whiskers and show sample size.
- **Histogram/density:** distributions of one variable.
- **Heatmap:** structured two-dimensional values; include a readable colorbar with units.
- **ROC/PR curve:** classifier operating characteristics; state class/averaging convention.
- **Survival curve:** time-to-event data; include censoring and risk-table information when appropriate.
- **Forest plot:** effect estimates and confidence intervals.
- **Polar plot:** direction-dependent or angular quantities such as radiation patterns.
- **Time-frequency plot:** spectrograms or time-varying spectra; label time, frequency, and scale.

Rules:
- Label each axis with metric and unit.
- Preserve meaningful scales and zero baselines where appropriate.
- Do not use dual axes merely to fit unrelated metrics together.
- Do not add error bars or significance marks unless supported by the data and analysis.
- Keep method colors and markers consistent across related panels.
- State normalization, reference baseline, and statistical definitions.

## 8. Maps, spatial plots, and trajectories

- Include map projection, scale bar, north arrow, coordinate system, or spatial reference when needed.
- Preserve geographic extent and acquisition time across comparison panels.
- Distinguish observed and predicted trajectories.
- Use a legend for classes, regions, sensors, or agents.
- Avoid arbitrary image stretching or aspect-ratio changes.
- If maps are not to scale, state this.

## 9. Microscopy, medical imaging, and image composites

- Keep image panels aligned and use consistent crop, orientation, and scale when comparison is intended.
- Include scale bars and define how they were calculated.
- Preserve image provenance and preprocessing history.
- Use a consistent color scale for the same quantitative measurement across panels.
- Clearly distinguish raw images, processed images, segmentation masks, and overlays.
- Never conceal, fabricate, or selectively remove scientific evidence.

## 10. Tables and mathematical figures

- Align numeric columns and use consistent significant digits.
- Put units in column headings.
- Define abbreviations and statistical notation.
- Use sparse rules and restrained emphasis.
- Preserve exact mathematical notation and assumptions.
- Do not replace a proof or equation with a misleading cartoon.

## 11. Multi-panel composites

- Give the full figure one primary message.
- Use panel labels consistently.
- Align panels and maintain comparable plot dimensions where comparison is intended.
- Share legends only when the encoding is genuinely shared.
- Keep panel-specific scales visible.
- Do not reduce every panel to an unreadable size just to fit more content.
