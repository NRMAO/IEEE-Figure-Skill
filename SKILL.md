---
name: ieee-figure-skill
description: >
  Design, generate, inspect, and refine publication-ready technical figures for IEEE-style
  research papers. Use when a user asks to create or improve hardware architecture diagrams,
  ECC/RS encoder or decoder diagrams, HBM/chiplet interconnect figures, algorithm flowcharts,
  timing diagrams, dataflow diagrams, circuit illustrations, or quantitative performance/PPA
  plots from prose, equations, RTL, CSV, Excel, or existing figures.
---

# IEEE Figure Skill

## Mission

Create technically faithful, publication-ready research figures. Apply a consistent visual
design system inspired by the reviewed DRAM, HBM, ECC, and interconnect literature, while
adapting the graphic grammar to the figure type.

**Priority order:** technical correctness > legibility at final print size > visual consistency
> decorative polish. Never change a signal relationship, algorithm step, formula, data value,
or hardware function merely to make a figure look cleaner.

## When to use this skill

Use this skill when the user asks to:

- create, redraw, or refine an IEEE-style research figure;
- turn prose, equations, RTL, or a block-level description into a diagram;
- visualize RS/ECC, HBM, DRAM, chiplet-interconnect, FPGA, or ASIC architecture;
- draw algorithm/dataflow/timing/circuit diagrams;
- create performance, reliability, area, delay, power, throughput, or error-rate plots;
- analyze the visual style of figures in supplied research papers.

Do not use it for ordinary decorative illustrations, logos, or slide artwork unless the user
explicitly wants a paper figure.

## Source and evidence discipline

1. Treat user-provided RTL, equations, architecture descriptions, and measured data as the
   authoritative technical sources.
2. For literature-style analysis, distinguish:
   - **Observed:** directly visible or stated in the supplied paper;
   - **Estimated:** approximate visual measurements or inferred colors/fonts;
   - **Recommendation:** a reusable design rule derived from the evidence.
3. Never claim an exact font, point size, HEX color, line width, or IEEE-wide requirement unless
   it is explicitly documented or measured reliably. Mark visual estimates as approximate.
4. Do not copy a paper's complete figure. Extract general design principles and create original
   diagrams. Do not upload source PDFs or copyrighted figure images to a public repository.
5. If a critical connection, polarity, bus width, pipeline stage, code parameter, or algorithm
   branch is unspecified, ask one focused question or mark the assumption visibly.
6. Do not invent measured data. Preserve supplied values, units, significant digits, and
   uncertainty. Label synthetic example data as illustrative.

## Workflow

### 1. Classify the requested figure

Choose one primary type and any secondary types:

- architecture / system overview;
- block diagram / datapath;
- algorithm flowchart;
- dataflow / memory mapping;
- circuit / logic-gate structure;
- timing / waveform diagram;
- performance or reliability plot;
- table;
- mathematical or error-pattern illustration;
- multi-panel composite figure.

Read `references/figure-type-guidelines.md` for type-specific rules.

### 2. Extract the technical model before drawing

Create a compact internal specification:

- purpose and intended message of the figure;
- inputs, outputs, modules, states, and transformations;
- directed connections and signal names;
- data widths, code parameters, units, and clock/time relationships;
- parallel versus serial operations;
- control versus data paths;
- known constraints and unresolved assumptions.

For RTL-derived figures:
- identify module instances, ports, assignments, state machines, and hierarchy;
- follow actual signal connectivity rather than module names alone;
- distinguish combinational and sequential logic;
- preserve bit widths, signedness, reset polarity, clock edge, and handshake semantics;
- do not infer a physical floorplan from RTL unless asked;
- show only the abstraction level requested (system, module, datapath, or gate level).

For RS/ECC figures:
- distinguish code construction, encoding, syndrome generation, error-location search,
  error-magnitude calculation, correction, and verification;
- keep symbol width, codeword length, message length, parity count, field, primitive polynomial,
  and correction capability explicit when supplied;
- distinguish a general RS decoder from a shortened/single-symbol or application-specific decoder;
- do not insert Berlekamp–Massey, Chien search, Forney evaluation, inverse LUTs, or other blocks
  unless they belong to the specified architecture;
- mark GF multiplication, constant multiplication, XOR, lookup, comparison, and reduction
  operations accurately.

### 3. Select the visual grammar

Use the defaults in `references/ieee-figure-design-rules.md` and
`references/color-and-typography.md`. Do not force all figure types into the same appearance.

Default approach:
- hardware architecture and logic: white background, dark outlines, restrained blue fills,
  limited orange emphasis, and red only for error/exception paths;
- timing and mathematical illustrations: primarily monochrome, with color only to identify
  selected signals or cases;
- performance plots: clear categorical palette, explicit units, readable axes and legends;
- multi-panel figures: consistent panel labels, spacing, type scale, and color semantics.

### 4. Choose a reproducible output format

Prefer editable vector and source outputs:

| Figure type | Preferred source | Publication output |
|---|---|---|
| Architecture / block diagram | SVG, Graphviz DOT, Mermaid, or PPTX | SVG + PDF |
| Algorithm flowchart | Mermaid or Graphviz | SVG + PDF |
| Timing diagram | SVG or waveform-generation script | SVG + PDF |
| Performance plot | Python + Matplotlib + CSV | PDF + SVG + PNG preview |
| Mathematical illustration | SVG, TikZ, or LaTeX | PDF + SVG |
| Table | LaTeX tabular source or CSV-driven script | LaTeX / PDF / SVG |

Choose the tool that preserves editability and correctness. Do not use a raster-only image
generator when the user requires exact labels, editable geometry, or data fidelity.

### 5. Compose the figure

- Determine final physical width first: single-column, double-column, or custom.
- Build a clear reading order (usually left-to-right for datapaths and top-to-bottom for
  algorithms).
- Group related modules and show hierarchy without excessive nested boxes.
- Align module edges and distribute whitespace deliberately.
- Route connectors orthogonally where practical; avoid crossings and ambiguous junctions.
- Put signal names and bus widths close to the relevant wire.
- Keep text horizontal unless a technical convention requires otherwise.
- Use a consistent visual distinction for data, control, clock/reset, error, and optional paths.
- Use the least color needed to communicate meaning.

### 6. Generate source and publication assets

Deliver, where applicable:
- editable source file (SVG / DOT / Mermaid / Python / TikZ / PPTX);
- vector publication file (PDF and/or SVG);
- high-resolution PNG preview (normally 300–600 dpi for raster export);
- any data file needed to reproduce a plot;
- short notes describing assumptions and how to edit/regenerate the figure.

For plots, include the exact input data and script. Never silently alter or normalize values.
If normalization is used, state the baseline and formula in the figure or caption.

### 7. Validate before delivery

Use `references/quality-checklist.md`. At minimum verify:
- all labels, subscripts, superscripts, symbols, and units;
- every arrow's source, destination, and direction;
- every bus width and module name against the source;
- panel labels and caption references;
- no clipped text, overlapping objects, accidental line crossings, or tiny labels;
- color contrast and grayscale distinguishability;
- readability at the actual target column width;
- SVG/PDF opens correctly and the source regenerates the output.

If the environment cannot render or execute a format, say so; do not claim a successful test.

## Interaction rules

- If all essential technical facts are present, proceed without asking preference questions.
- If one essential fact is missing, ask one concise question.
- If assumptions are unavoidable, list them before or alongside the deliverable.
- Do not ask the user to restate information already present in supplied files or the conversation.
- When refining an existing figure, preserve its scientific meaning and identify any proposed
  semantic change separately from purely visual edits.

## Repository references

Consult only the references relevant to the current task:

- `references/paper-style-analysis.md` — observations from the supplied papers.
- `references/ieee-figure-design-rules.md` — common visual system and design tokens.
- `references/color-and-typography.md` — palette, type, strokes, and print-size defaults.
- `references/figure-type-guidelines.md` — architecture, flowchart, timing, plot, table, and
  mathematical figure rules.
- `references/quality-checklist.md` — pre-delivery checks.

Templates and examples are under `templates/` and `examples/`.
