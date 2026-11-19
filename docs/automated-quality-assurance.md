# Automated Figure Quality Assurance

This guide describes the automated preflight layer added to IEEE-Figure-Skill. It combines deterministic file inspection, browser-based geometry checks, manifest-driven checks, and a required human/AI review stage.

## 1. Design principle

**The program checks measurable properties; the AI and researcher judge scientific meaning.**

The preflight tool is a screening system, not an IEEE certification engine. It cannot guarantee acceptance, infer every journal-specific rule, or decide whether a figure truthfully represents the underlying science.

## 2. What is checked

| Check area | Automated method | Main limitations |
|---|---|---|
| File format | Compare file extension with the selected profile | EPS/PS are recognized but not deeply parsed in this version |
| SVG syntax | Parse XML and validate root/viewBox | Well-formed XML does not prove visual correctness |
| SVG text overflow | Render with Chromium and measure transformed text bounding boxes against the root viewBox | External fonts may be unavailable; nested clipping paths and all text collisions are not fully assessed |
| PDF text clipping | Read PDF text-span bounding boxes and compare with page bounds | Does not identify every visual collision or clipped glyph caused by unusual masks |
| Raster resolution | Read PNG/TIFF DPI metadata or compute effective DPI from manifest print dimensions | Missing physical dimensions or metadata prevent a reliable DPI decision |
| PDF embedded raster resolution | Compare image pixel dimensions with their physical placement on the PDF page | Image transformations and unusual masks can complicate interpretation; inspect final output too |
| PDF fonts | Inspect font resources and embedded font streams | Outlined text has no font resource; no font objects does not prove that the PDF is correct |
| Color palette | Compare manifest-declared colors in CIE76 Lab space, grayscale luminance, and simulated color-vision deficiencies | A palette check cannot understand whether colors encode the correct scientific categories |
| Text contrast | Compute foreground/background contrast ratio for declared text samples | WCAG-style contrast thresholds are screening heuristics, not IEEE figure requirements |
| Caption completeness | Check figure number, panel labels, declared abbreviations, symbols, color meanings, required terms, and source credit in the manifest | Does not prove that the caption explains the scientific result accurately or completely |
| Legend/axis labels | Check manifest-declared labels against extractable SVG/PDF text | Raster-only labels are not OCR-checked |
| Venue requirements | Apply a configurable JSON profile | Users must maintain a profile for their actual journal/conference and verify current instructions |

## 3. Install

Python 3.10 or newer is required.

    python -m pip install -e ".[browser,test]"
    python -m playwright install chromium

The project dependencies include Pillow, PyMuPDF, NumPy, and colorspacious. Playwright is an optional extra used for rendered SVG text geometry. If Chromium is unavailable, the tool reports that the browser check could not run rather than silently claiming that text overflow was checked.

## 4. Run the preflight tool

Run against an SVG or PDF with a manifest:

    python tools/figure_preflight.py --manifest manifests/figure-manifest.example.json --profile profiles/ieee-baseline.json --report build/figure-preflight.json

The file path in the example manifest is resolved relative to the manifest's directory. You can override it:

    python tools/figure_preflight.py --figure path/to/figure.pdf --manifest path/to/figure-manifest.json --report build/figure-preflight.json

For a quick file-only inspection without a manifest:

    python tools/figure_preflight.py --figure path/to/figure.svg

This still checks the file and, when available, SVG geometry. Caption, semantic palette, and declared text-contrast checks are skipped because the necessary metadata was not supplied.

Use strict mode to return a non-zero exit code for warnings as well as errors:

    python tools/figure_preflight.py --manifest figure-manifest.json --strict

Exit codes:

- 0: no errors (warnings may still exist unless --strict is used).
- 1: one or more errors, or warnings in strict mode.
- 2: invalid command input, manifest, or profile.

The optional JSON report contains a status, counts, measured metrics, and individual findings. Severity levels are error, warning, and info.

## 5. Manifest format

Start from manifests/figure-manifest.example.json. Important fields include:

- file: figure path, relative to the manifest or absolute.
- figure_number: expected figure number.
- caption: complete caption text as intended for the manuscript.
- panels: panel labels that should appear in both the figure and caption.
- abbreviations, symbols, color_encodings: terms and definitions that should be explained in the caption.
- legend_labels, required_figure_terms: labels expected to appear in extractable SVG/PDF text.
- target_width_in, target_height_in: final physical dimensions used for effective raster DPI and SVG text-size screening.
- artwork_type: color_grayscale or black_white_line_art.
- palette: semantic categories and their exact hex colors. Add only colors that encode distinctions readers must identify.
- text_samples: foreground/background color pairs for labels that need a contrast check.
- source_reused and source_credit: identify adapted/reused content and its credit line. Permission must be checked separately.

Do not add every decorative color to palette. The palette checker is most useful when it receives the small set of colors that represent data series, experimental groups, cell classes, states, or other meaningful categories.

## 6. Venue profiles

profiles/ieee-baseline.json encodes a general screening baseline derived from public IEEE Author Center material:

- accepted submission formats: PS, EPS, PDF, PNG, TIFF;
- one-column width reference: 3.5 in;
- two-column width reference: 7.16 in;
- maximum height reference: 8.8 in;
- color/grayscale raster guidance: greater than 300 dpi;
- black-and-white line-art guidance: greater than 600 dpi.

SVG is listed as an editable working-source format in this profile, not as an accepted final graphics-submission format. Export to a format accepted by the target venue.

Copy the profile and adjust it for the specific journal or conference. Do not overwrite the shared baseline with a venue-specific exception. A venue may have different width, height, file-size, color, or figure-handling requirements.

Official starting points:

- IEEE Author Center — Resolution and Size: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/
- IEEE Author Center — File Formatting: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/file-formatting/
- IEEE Author Center — Create Graphics for Your Article: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/
- Proceedings of the IEEE — Guidelines for Figures and Tables: https://proceedingsoftheieee.ieee.org/resources/guidelines-for-figures-and-tables/

## 7. Color accessibility logic

The checker uses three complementary signals:

1. CIE76 ΔE in Lab space to flag pairs of declared category colors that are perceptually close under the basic color-difference model.
2. Relative luminance separation to flag pairs that may become difficult to distinguish in grayscale.
3. Optional full-severity protanomaly, deuteranomaly, and tritanomaly simulations through colorspacious.

The default thresholds are screening heuristics. They are not official IEEE limits and should not be treated as universal perceptual cutoffs. Always inspect the actual figure in grayscale and with a color-vision-deficiency simulation, and use marker shapes, line styles, hatching, direct labels, or patterns as additional cues.

Text contrast is checked only for foreground/background pairs explicitly declared in the manifest. The default 4.5:1 ratio is a WCAG-inspired screening heuristic; it is not a formal IEEE figure acceptance threshold and may not be appropriate for every graphical element.

IEEE's own graphics guidance recommends checking grayscale legibility and avoiding dependence on red/green, blue/green, and yellow/red distinctions alone. See the official Author Center link above.

## 8. Caption completeness logic

The manifest makes the checks explicit. If the figure uses panels (a) and (b), for example, declare those labels. If it uses ROI, provide the exact expansion required in the caption. If line colors identify experimental groups, declare the group/color meanings.

The tool checks whether these declared items are present in the caption and whether panel/legend labels are present in extractable SVG/PDF text. It does not decide whether the caption correctly summarizes the scientific finding, identifies the experimental design, or provides enough context to interpret the data. The AI review stage must compare the caption with the actual figure and the paper's methods/results.

## 9. Human and AI review still required

Before submission, review:

- scientific correctness, data provenance, statistical interpretation, and causal claims;
- whether every plotted series, panel, symbol, unit, and legend matches the source data;
- whether the caption accurately describes what is shown and does not overstate the result;
- whether the figure is cited in the manuscript body and numbering is consistent;
- image manipulation, cropping, registration, permissions, and third-party credit lines;
- actual print-size legibility and whether the figure remains understandable in grayscale;
- the current target journal/conference instructions and submission-system requirements.

Never interpret a PASS result as proof that the figure is scientifically valid or guaranteed to be accepted.

## 10. Continuous integration

The GitHub Actions workflow runs unit tests and browser-based SVG preflight on the repository's original examples for pushes and pull requests. It stores machine-readable reports as a workflow artifact. This protects the repository's own templates; users should also run the same tool on their actual paper figures and provide a manifest.
