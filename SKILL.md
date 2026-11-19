---
name: ieee-figure-skill
description: >
  Design, generate, inspect, and refine publication-ready scientific figures for IEEE-style
  journals and conferences across engineering, computing, physical sciences, and biomedical
  research. Use for system diagrams, algorithms, neural-network architectures, experimental
  setups, scientific plots, microscopy and medical-image panels, maps, trajectories, antenna
  patterns, circuits, and multi-panel figures from prose, equations, code, or data.
---

# IEEE Academic Figure Skill

## Mission

Create scientifically faithful, readable, reproducible, and publication-ready figures for IEEE-style research. This Skill is domain-neutral: it does not assume a particular discipline, paper topic, software package, color palette, or diagram layout.

**The figure's scientific purpose determines its visual grammar.** A neural-network architecture, microscopy panel, circuit schematic, radiation pattern, map, and statistical plot should not be forced into one visual style.

Priority order:

1. Scientific and technical correctness.
2. Clarity of the message and correct visual encoding.
3. Legibility at the final publication size.
4. Accessibility and reproducibility.
5. Aesthetic consistency.

Never alter scientific meaning, measured values, image evidence, mathematical relationships, or system connectivity merely to make a figure look cleaner.

## When to use

Use this Skill when a user asks to:

- create, redraw, or improve an IEEE-style research figure;
- convert research prose, equations, algorithms, source code, or experimental methods into a figure;
- create a system architecture, process workflow, model/network architecture, state machine, sequence diagram, or experimental setup;
- visualize numerical results, statistics, time series, spectra, performance, uncertainty, or ablation studies;
- prepare scientific image panels, microscopy composites, medical-image visualizations, maps, trajectories, or spatial plots;
- analyze figure design patterns from supplied or publicly accessible research papers;
- prepare editable figure sources and publication-ready exports.

Do not use it for decorative illustrations, logos, marketing graphics, or slide artwork unless the user explicitly requests a research-paper figure.

## Core workflow

### 1. Understand the figure request

Identify:

- the one-sentence scientific message;
- the intended reader and research domain;
- the figure type and level of detail;
- the source of truth (paper, equations, code, raw data, image, protocol, or user description);
- the target journal/conference and its current artwork instructions;
- target physical width (single column, double column, or custom);
- required editable source and final formats;
- whether the figure is conceptual, illustrative, or data-driven.

If one essential fact is missing, ask one focused question. Do not make users complete a long preference questionnaire when reasonable defaults are available.

### 2. Classify the visual task

Choose one primary family and any secondary families:

- **Architecture and system diagrams:** hardware, software, networks, devices, infrastructure, and multi-agent systems.
- **Algorithms and processes:** flowcharts, state machines, sequence diagrams, experimental workflows, and protocols.
- **Model and data pipelines:** machine-learning networks, feature fusion, training/inference, and data processing.
- **Experimental setup and geometry:** apparatus, measurement configuration, coordinate frames, and instrumentation.
- **Scientific illustrations:** physical mechanisms, biological structures, materials, field distributions, and conceptual models.
- **Quantitative plots:** line, scatter, bar, box, violin, histogram, heatmap, ROC/PR, survival, polar, and uncertainty plots.
- **Spatial and image figures:** microscopy, pathology, medical imaging, remote sensing, maps, segmentation, and trajectories.
- **Tables and mathematical figures:** exact-value summaries, equations, matrices, and derivation illustrations.
- **Multi-panel composites:** coordinated combinations of the above.

Read the relevant sections of references/figure-type-guidelines.md and references/domain-routing-matrix.md.

### 3. Extract the scientific model

Before drawing, create a concise specification:

- inputs, outputs, entities, variables, and transformations;
- modules, states, events, and directed connections;
- dimensions, units, coordinate systems, scale bars, and sampling conditions;
- parallel, sequential, feedback, and optional relationships;
- data groups, sample sizes, statistical tests, and uncertainty definitions;
- image source, acquisition method, ROI, orientation, and registration status;
- assumptions, unknowns, and evidence that supports each element.

For code-derived figures, inspect actual ports, assignments, function calls, data structures, and control flow. Do not infer a connection from a module name alone.

For data-derived figures, use the supplied data as the source of truth. Preserve missing values, sample sizes, units, statistical definitions, and relevant outliers. Do not invent measurements, error bars, confidence intervals, or statistical significance.

For image-derived figures, preserve the original image evidence. Distinguish permitted visualization adjustments from scientific alteration. Consult references/visualization-ethics.md.

### 4. Select the correct visual grammar

Use the domain routing matrix to select shapes, marks, connectors, labels, colors, and layout.

General rules:

- one primary message per figure;
- a clear reading order;
- consistent visual encoding across related panels;
- labels close to the object or signal they identify;
- units on axes and dimensions on physical drawings;
- explicit legends, scale bars, coordinate frames, and map references where needed;
- no unexplained symbols, ambiguous arrows, or decorative effects that compete with evidence;
- color is never the only cue for a critical distinction;
- use monochrome when it communicates the content more clearly.

Do not apply a fixed blue/orange/teal palette to every field. A palette is a tool, not a universal IEEE style.

### 5. Choose an editable and reproducible format

Select the format that best preserves scientific meaning and editability.

| Figure task | Useful source formats | Common publication exports |
|---|---|---|
| Architecture / block diagram | SVG, Graphviz DOT, Mermaid, PPTX | PDF, SVG, EPS |
| Workflow / state / sequence | Mermaid, Graphviz, SVG | PDF, SVG, EPS |
| Neural-network architecture | SVG, PPTX, Graphviz, Python | PDF, SVG |
| Quantitative plots | Python/Matplotlib, MATLAB, R, CSV | PDF, SVG, EPS, TIFF/PNG |
| Microscopy / medical-image composite | Python, ImageJ/Fiji, QuPath, SVG | TIFF, PNG, PDF |
| Spatial / geospatial figure | Python, GIS tools, SVG | PDF, SVG, TIFF |
| Antenna / field / polar plot | MATLAB, Python, CSV, SVG | PDF, EPS, SVG |
| Tables / equations | LaTeX, CSV, Python | LaTeX, PDF |

Prefer vector formats for diagrams, line art, plots, and text. Use raster formats when the scientific content itself is raster imagery, such as microscopy, photographs, or medical scans.

Do not use a raster-only image generator when exact text, editable geometry, source code, or data fidelity is required.

### 6. Compose at final size

- Determine the final column width before arranging content.
- Use a grid and consistent alignment.
- Keep enough whitespace around labels, symbols, legends, and panel boundaries.
- Avoid connector crossings and ambiguous junctions.
- Keep text readable after the figure is reduced to its intended print size.
- Use panel labels consistently, such as (a), (b), and (c).
- Keep repeated group colors and marker meanings stable across related figures.
- Do not compress a complex figure into one panel if separate panels would communicate the science more clearly.

### 7. Export and validate

Deliver, where appropriate:

- editable source;
- vector publication export;
- high-resolution raster export if required;
- input data and regeneration script for data-driven figures;
- a brief note describing assumptions and non-obvious visual encodings.

Use references/quality-checklist.md before delivery. Check the actual target venue's instructions rather than assuming all IEEE publications use identical requirements.

### 8. Run automated preflight when a file can be inspected

When the repository's preflight utility is available, run it on the exported figure rather than relying only on a visual impression:

    python tools/figure_preflight.py --manifest path/to/figure-manifest.json --profile profiles/ieee-baseline.json --report build/figure-preflight.json

Use a manifest to provide the final caption, figure/panel numbering, abbreviation and symbol definitions, color meanings, legend/axis labels, target physical dimensions, artwork type, semantic palette, text foreground/background samples, and source-credit information.

Interpret findings carefully:

- **Errors** identify objective failures such as missing files, unsupported final formats, invalid SVG, or missing required caption/credit metadata.
- **Warnings** identify likely issues such as text outside the SVG/PDF page, low effective raster DPI, small text, unembedded PDF fonts, similar category colors, low contrast, or incomplete declared caption items.
- **Info** identifies checks that were skipped or require human interpretation.

For SVG, use the Chromium-based text bounding-box check. For PDF, inspect text bounds, font resources, and embedded raster resolution. For PNG/TIFF, inspect pixel dimensions and DPI; raster text clipping is not automatically inferred. Color and caption checks are driven by explicit manifest declarations.

A PASS is not proof of scientific validity or guaranteed IEEE acceptance. The AI must still compare the rendered figure and caption against the source paper, data, methods, and actual target venue instructions. If the browser or a parser is unavailable, state that the corresponding check was not completed; never claim it passed.

See docs/automated-quality-assurance.md for installation, profile customization, the manifest schema, CI behavior, and known limitations.

## Domain adapters

The Skill is general-purpose, but it must adapt to the science:

- **Circuits, electronics, and computing:** preserve signal direction, bus widths, timing, register boundaries, interface semantics, and actual module connectivity.
- **Communications and signal processing:** preserve units, sampling rates, frequency/time axes, phase conventions, signal paths, modulation, and spectral interpretation.
- **AI and computer vision:** distinguish training from inference, model blocks from data, feature maps from predictions, and quantitative metrics from qualitative examples.
- **Biomedical and life sciences:** preserve sample identity, cohort/group definitions, image provenance, scale bars, ROI, spatial registration, and statistical meaning.
- **Robotics and control:** preserve coordinate frames, sensor locations, transformations, trajectories, state transitions, and feedback direction.
- **Power and energy:** distinguish electrical topology from control logic, label voltage/current/power units, and preserve operating states and protection paths.
- **Antennas and electromagnetics:** preserve geometry, coordinate axes, polarization, frequency, gain units, reference planes, and simulation-versus-measurement identity.
- **Remote sensing and geospatial science:** preserve map projection, spatial extent, north direction, scale, resolution, acquisition date, and class-mask semantics.
- **Materials and physical sciences:** preserve material phases, crystallographic orientation, microscopy scale bars, acquisition conditions, and measurement provenance.

The examples and paper corpus are representative starting points, not an exhaustive survey of every IEEE field.

## Literature and evidence discipline

When analyzing research papers:

1. Prefer the final published IEEE version when legally and technically accessible.
2. An accepted manuscript or author preprint may be used, but label the version accurately.
3. Separate **visually inspected full text**, **text/caption inspected**, and **metadata/abstract only** evidence.
4. Do not infer figure style from a title or abstract alone.
5. Distinguish an observed design choice from a recommendation derived from it.
6. Do not claim that a visual choice is an IEEE-wide rule unless the official author instructions say so.
7. Do not bundle publisher PDFs, copied figures, or restricted third-party images in a public repository.

See references/ieee-paper-corpus.md and references/ieee-publication-baseline.md.

## Interaction rules

- If the user's supplied source is sufficient, proceed without asking them to repeat information.
- If a source file is missing or unreadable, say which part could not be inspected.
- If a visual is conceptual, label it as conceptual.
- If a diagram contains inferred elements, list those assumptions.
- When editing an existing figure, preserve the scientific meaning and report any proposed semantic change separately from visual edits.
- Never claim a file was rendered, tested, or validated unless that check actually succeeded.

## Repository references

- references/ieee-publication-baseline.md — official IEEE baseline guidance and venue-specific caveats.
- references/ieee-paper-corpus.md — cross-domain IEEE paper examples and evidence levels.
- references/domain-routing-matrix.md — how to adapt figure grammar to research domains.
- references/figure-type-guidelines.md — detailed guidance by figure type.
- references/color-and-typography.md — accessible color and typography principles.
- references/visualization-ethics.md — data, image, and scientific-integrity rules.
- references/quality-checklist.md — final quality checks.
- docs/automated-quality-assurance.md — automated preflight workflow and limitations.
- tools/figure_preflight.py — automated file, caption, color, and venue-profile checks.
- references/paper-style-analysis.md — original hardware-focused seed corpus retained as one optional specialty case study.

Templates and examples are under templates/ and examples/.
