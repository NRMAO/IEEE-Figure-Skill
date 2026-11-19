# Validation report

Date: 2026-11-19

## Local package checks

- Reviewed figure-bearing pages of eight unique supplied papers (nine PDF uploads; the Kwon 2026
  paper appeared twice).
- Recorded figure locations, subject matter, and observed visual patterns in
  `references/paper-style-analysis.md`.
- Confirmed the package contains no source-paper PDF files and no copied paper figures.
- Parsed authored SVG files as XML.
- Rendered the original RS encoder concept and Kwon-derived SSEC decoder flow to PNG; exported the
  decoder flow to PDF.
- Executed `examples/performance-example/plot_sample.py` successfully with the bundled
  demonstration CSV. The script generated PDF, SVG, and PNG outputs for each platform/metric group.
- Confirmed the example CSV keeps ASIC metrics and FPGA metrics separate.
- Confirmed the Python plot scripts compile.

## Remote repository checks

- Confirmed `NRMAO/IEEE-Figure-Skill` exists, is public, and uses `main` as its default branch.
- Confirmed the connected account has push/admin permissions.
- Initialized the empty repository with a first commit and prepared the complete source tree for
  upload. Final commit/ref and remote file verification are recorded after the push completes.

## Not yet verified

- Mermaid flowchart sources were checked as text but not rendered in this environment.
- No RTL-specific encoder architecture was validated because no encoder RTL or complete
  implementation specification was included. The RS encoder SVG is explicitly conceptual.
- No claim is made that the Skill has been installed into a particular agent runtime; installation
  paths differ by platform.

## Demonstration data warning

The values in `examples/performance-example/sample_metrics.csv` are synthetic demonstration
values. They are not results from the uploaded papers or from the user's experiments.
