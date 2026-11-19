# Reference-to-Figure: extract a visual style and generate editable Python

This workflow lets a user provide one or more visual references and ask the Skill to create a new scientific figure using the reference's reusable design language.

**The AI performs the visual analysis. The Python utilities preserve the extracted style as a portable profile and scaffold a reproducible project.** The scaffold does not replace the AI's figure-specific reasoning or generate scientific content by itself.

## 1. What users can provide

Depending on the AI runtime's file-inspection capabilities, references may include:

- PNG, JPEG, or TIFF figure images and crops;
- a PDF paper or a PDF containing the selected figure;
- SVG vector figures;
- PPTX slides or exported slide images;
- several reference figures that share a preferred visual language.

If a PDF contains many figures, identify the relevant page and figure number. Render the actual figure region before analysing visual properties. A paper title, abstract, or caption alone is not enough to infer its visual style.

The user should also provide the **target scientific content**, such as a method description, equation, source code, experimental data, or original image. A reference figure describes appearance; it is not the source of truth for a new study's scientific claims.

## 2. AI extraction workflow

1. **Inspect the reference.** Confirm which figure or panel is being used. Record whether the full visual was inspected, only text/caption was inspected, or the value is an estimate.
2. **Classify its visual grammar.** Identify architecture, workflow, quantitative plot, scientific illustration, image panel, table, or multi-panel composition.
3. **Extract design tokens.** Record canvas ratio and background, typography hierarchy, palette roles, line and marker styles, borders, arrows, gridlines, whitespace, alignment, legend placement, and panel labels.
4. **Separate observations from estimates.** Embedded font metadata or measured geometry may be observed; a font guessed by appearance or a HEX value sampled from a compressed screenshot is an estimate.
5. **Resolve multiple references.** Record shared traits as the preferred style. Keep one-off choices separate. Do not average visibly conflicting references into an arbitrary hybrid.
6. **Create a style profile.** Use the JSON schema and example in this folder. Preserve provenance, confidence, and extraction notes.
7. **Understand the target science independently.** Extract the target's entities, data, labels, units, relationships, transformations, and constraints from its actual source.
8. **Generate a new figure.** Apply the extracted style only where it suits the target figure family. Preserve the scientific content and create editable source code.
9. **Render, inspect, and revise.** Run the generated script, inspect the actual output, and use the repository's figure preflight checks where applicable.

See <code>references/reference-style-extraction.md</code> for the detailed extraction checklist and reuse boundaries.

## 3. Style profile

The profile is a portable design-token record, not a copy of the source figure. It includes:

| Section | Typical fields |
|---|---|
| <code>source_references</code> | File names, reference description, inspection level |
| <code>canvas</code> | Width, height, aspect ratio, background |
| <code>typography</code> | Font family/fallbacks, title, axis, tick, and legend sizes |
| <code>palette</code> | Primary, secondary, accent, neutral, text, background, category colors |
| <code>geometry</code> | Line widths, axis widths, marker size, grid width |
| <code>layout</code> | Legend position, grid direction, spine visibility, whitespace, panel-label position |
| <code>export</code> | PDF/SVG/PNG/TIFF formats, raster DPI, transparent background |
| <code>extraction</code> | Evidence level, confidence, notes about uncertainty |

The machine-readable schema is <code>templates/reference-to-figure/style-profile.schema.json</code>; a complete starter profile is <code>templates/reference-to-figure/style-profile.example.json</code>.

The schema supports additional figure-specific fields. A profile extracted for a microscopy composite may include scale-bar and image-panel rules; an architecture profile may include connector and module-shape conventions. Do not force every property into Matplotlib rcParams.

## 4. Create an editable Python project

Python 3.10 or newer is required. Clone the repository, then install the optional Matplotlib dependency:

~~~bash
python -m pip install -e ".[plotting]"
~~~

Ask the Skill-enabled AI to inspect the reference and write <code>reference-style-profile.json</code> using the repository schema. Then scaffold a project:

~~~bash
python tools/create_figure_project.py \
  --profile path/to/reference-style-profile.json \
  --output my-figure-project
~~~

The command validates the profile and creates:

~~~text
my-figure-project/
├── README.md
├── reference-style-profile.json
├── figure_style.py
├── generate_figure.py
├── data/
│   └── .gitkeep
└── output/
    └── .gitkeep
~~~

The starter <code>generate_figure.py</code> reads a user-supplied CSV and supports line, scatter, and bar plots. Example:

~~~bash
cd my-figure-project
python generate_figure.py data/my-results.csv \
  --x time --y response --group cohort --kind line \
  --xlabel "Time (s)" --ylabel "Response (a.u.)"
~~~

It exports the formats declared in the style profile. The starter reads actual CSV values and does not create fabricated measurements.

For other figure families, the AI should adapt or replace the starter script with figure-specific Python:
- **Architecture and flowcharts:** Matplotlib patches or Graphviz with explicit node/edge definitions.
- **Multi-panel figures:** Matplotlib GridSpec with shared typography and panel spacing.
- **Microscopy and medical-image panels:** image-processing/compositing code that retains original source files and records any permitted display transforms.
- **Spatial figures:** suitable coordinate-aware plotting libraries, with projection, scale, and coordinate metadata preserved.
- **Tables and mathematical illustrations:** Matplotlib, LaTeX/TikZ, or another editable vector-capable format.

The style helper is copied into the project as <code>figure_style.py</code> so the generated script remains self-contained relative to the project folder.

## 5. Recommended AI prompt

~~~text
Use IEEE-Figure-Skill in Reference-to-Figure mode.

I have supplied:
1. A visual reference figure that defines the style I like.
2. My own scientific content/data/code that must determine the new figure's meaning.

First inspect the reference and extract its reusable visual features. Separate directly observed properties from visual estimates, and record confidence for uncertain values. Create a reference-style-profile.json that follows the repository schema.

Then analyse my scientific content independently. Choose the correct figure type, adapt the extracted style without copying the reference figure's exact composition or content, and generate an editable Python source file. Use my real data only; do not invent values.

Run the Python script, inspect the rendered output, and report any remaining layout or scientific ambiguities. Deliver the style profile, Python source, run instructions, and appropriate PDF/SVG/PNG exports.
~~~

## 6. Multiple references and style conflicts

When the user supplies multiple references:
- identify which properties recur across references;
- distinguish a shared design system from figure-type-specific conventions;
- preserve deliberate differences where different figure types require them;
- ask the user to choose a primary reference only if conflicting visual directions cannot be reconciled without changing the intended result.

A quantitative plot and a biomedical mechanism illustration may share typography and color roles while using very different geometry. Reuse the common design tokens, not the entire layout.

## 7. Copyright, integrity, and limitations

- Extract general design principles and visual tokens; do not reproduce a publisher's figure, exact arrangement, wording, icons, or distinctive artwork.
- Do not copy data, scientific claims, labels, or annotations from the style reference into the target figure unless they are independently part of the user's target content.
- Do not remove or alter scientific evidence to imitate a visual style.
- Keep reference files in the user's working project. Do not upload them to this public repository unless the user explicitly asks and has the right to share them.
- Report when a reference could not be visually inspected. Never present estimated colors, fonts, dimensions, or line widths as exact measurements.
- The project scaffolder validates a JSON profile and creates editable starter files; it does not itself perform image recognition or generate a scientifically correct figure.
- The generated Python script must be run and its output inspected. A successful script execution does not prove scientific validity or journal compliance.
