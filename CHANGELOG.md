# Changelog

## 0.4.0 — 2026-11-19

- Added Reference-to-Figure workflow for extracting reusable visual design tokens from user-provided images, paper figures, PDFs, SVGs, and slides.
- Added an evidence-labelled JSON style-profile schema and example, including confidence notes for estimated fonts, colors, dimensions, and geometry.
- Added Matplotlib style-profile validation and mapping helpers.
- Added a non-destructive Python figure-project scaffolder with an editable CSV-driven line/scatter/bar plotting starter.
- Added reference-analysis guidance, reuse/copyright boundaries, and prompts for AI-generated figure-specific Python source.
- Added automated tests for style-profile validation, project scaffolding, overwrite protection, and a real Matplotlib rendering smoke test.
- Added an optional plotting dependency and included it in continuous integration.
- Updated the English and Simplified Chinese READMEs with the new workflow.

## 0.3.0 — 2026-11-19

- Added a runnable figure-preflight CLI for SVG, PDF, PNG, and TIFF files.
- Added Chromium-based SVG text-boundary checks and PDF text/page-boundary checks.
- Added raster DPI checks, PDF embedded-image effective-DPI checks, and PDF font-embedding inspection.
- Added manifest-driven caption, panel-label, abbreviation, symbol, color-meaning, legend-label, and source-credit checks.
- Added perceptual palette, grayscale-separation, color-vision-deficiency, and declared text-contrast screening.
- Added a configurable IEEE baseline profile and venue-specific profile workflow.
- Added unit/browser tests and GitHub Actions continuous integration with JSON preflight artifacts.
- Documented that automated preflight is a screening tool, not scientific validation or a guarantee of IEEE acceptance.

## 0.2.0 — 2026-11-19

- Repositioned the project as a domain-neutral IEEE academic figure Skill.
- Removed HBM, RS, and chiplet interconnects as the default scope of the main instructions.
- Added cross-domain paper research covering biomedical sensing, robotics, power/control, signal processing, remote sensing, antennas, AI, and industrial automation.
- Added explicit evidence levels to distinguish full-text inspection from abstract-only references.
- Added official IEEE publication baseline guidance with venue-specific caveats.
- Added domain routing, figure-type guidance, visualization ethics, and an expanded quality checklist.
- Added original cross-domain SVG examples and an antenna polar-plot template.
- Retained the original hardware-focused literature and HBM/RS examples as optional specialty references.
- No source-paper PDFs or copied publisher figures are included.

## 0.1.0 — 2026-11-19

- Initial hardware-centric Skill and figure design system.
- Added architecture, flowchart, timing, and performance-plot templates.
- Added original RS encoder and HBM SSEC decoder examples.
- Added CSV-driven Matplotlib examples and a validation checklist.
