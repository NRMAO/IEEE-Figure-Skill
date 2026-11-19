# Validation Report

Date: 2026-11-19

## Scope update

The repository has been broadened from a hardware/memory-focused seed project into a domain-neutral IEEE academic figure Skill.

The main Skill now covers architecture, algorithms, model/data pipelines, experimental setups, scientific illustrations, quantitative plots, microscopy/medical images, maps/trajectories, and multi-panel composites.

## Literature research

The cross-domain paper corpus includes IEEE journal papers from:
- IEEE Transactions on Instrumentation and Measurement
- IEEE Transactions on Control Systems Technology
- IEEE Transactions on Signal Processing
- IEEE Robotics and Automation Letters
- IEEE Transactions on Geoscience and Remote Sensing
- IEEE Transactions on Antennas and Propagation
- IEEE Transactions on Medical Imaging
- IEEE Transactions on Biomedical Engineering
- IEEE Access
- IEEE Transactions on Industrial Informatics
- IEEE Transactions on Industrial Electronics

Evidence levels are explicitly stated. Six papers received full-text or figure-level inspection; additional papers are metadata/abstract-level candidates and are not described as visually inspected.

## Official publication guidance

The repository now links to the IEEE Author Center's graphics guidance and Proceedings of the IEEE figure/table guidance. The documentation distinguishes official baseline guidance from general recommendations and repeatedly instructs users to check the target publication's current author instructions.

## Repository and content checks

- Main SKILL.md is domain-neutral and no longer treats HBM, RS, DRAM, or chiplet interconnects as the default scope.
- Original HBM/RS examples and the initial hardware-focused analysis are retained only as optional specialty material.
- Cross-domain examples are original illustrations, not copies or traced versions of paper figures.
- Source-paper PDFs are not bundled.
- Synthetic example geometry is labelled as conceptual.
- The antenna polar-plot template requires real user-supplied data; it contains no fabricated measurement series.

## Limitations

- The paper corpus is representative, not exhaustive or systematic.
- Full-text visual inspection is uneven across domains; papers with metadata-only evidence are labelled accordingly.
- Materials and physical-science figure guidance is included as a domain adapter, but the current IEEE paper corpus has limited direct materials-science coverage.
- The Mermaid source examples are not claimed as rendered unless a rendering test is separately recorded.
- No claim is made that the Skill has been installed into a particular agent runtime; installation paths differ by platform.


## Automated quality assurance (v0.3.0)

Implemented a runnable preflight pipeline with the following checks:

- SVG XML parsing and Chromium-based text bounding-box inspection against the SVG viewBox.
- PDF page dimensions, text-span bounds, font-size screening, embedded image effective DPI, and font-resource embedding inspection.
- PNG/TIFF dimensions and DPI metadata/effective DPI from declared print dimensions.
- Manifest-driven caption completeness checks for figure number, panel labels, abbreviations, symbols, color meanings, required terms, and source credits.
- Manifest-driven semantic palette checks using CIE76 color distance, grayscale luminance separation, and optional colorspacious color-vision-deficiency simulation.
- Declared text foreground/background contrast screening.
- Configurable file-format, dimension, and resolution profile.

The code includes a unit/browser test suite and a GitHub Actions workflow that runs tests and preflights the repository's SVG examples, uploading JSON reports as workflow artifacts. The profile distinguishes accepted IEEE submission formats from SVG editable source files.

## Validation limitations

- The automated checks do not establish scientific validity, correct statistical interpretation, caption semantics, image integrity, permissions, or guaranteed journal acceptance.
- SVG text geometry depends on the browser and available fonts; complex clipping paths, text collisions, and external fonts may require manual inspection.
- Raster-only text clipping is not OCR-checked.
- EPS/PS are recognized as accepted formats but are not deeply parsed by this version.
- Color-distance, grayscale, and WCAG-inspired text-contrast thresholds are screening heuristics, not official IEEE acceptance thresholds.
- Venue-specific instructions must be checked and represented in a customized profile.
