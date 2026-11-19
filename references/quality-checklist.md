# Quality Checklist

Use this checklist before delivering any figure.

## Technical correctness
- [ ] Figure purpose matches the user's request.
- [ ] Every module and signal is supported by RTL, equations, data, or explicit assumptions.
- [ ] Arrow direction and junction semantics are correct.
- [ ] Bus widths, symbol indices, code parameters, and field notation are correct.
- [ ] Pipeline/register boundaries and clock/reset polarity are preserved.
- [ ] No algorithmic stage has been inserted or removed without evidence.
- [ ] All numerical data, units, and significant digits match the source.

## Visual quality
- [ ] Main reading order is obvious.
- [ ] Modules and panels are aligned.
- [ ] Spacing is consistent.
- [ ] Connectors do not cross unnecessarily.
- [ ] Text is horizontal and legible.
- [ ] Colors encode meaning and have adequate contrast.
- [ ] The figure remains understandable in grayscale.
- [ ] No unnecessary gradients, shadows, textures, or decorative icons.
- [ ] Legend and panel labels are consistent.

## Publication readiness
- [ ] Final width matches the target single-/double-column layout.
- [ ] Text remains legible at actual print size.
- [ ] No clipped labels, equations, arrows, or borders.
- [ ] Caption and panel references agree.
- [ ] Vector output opens correctly.
- [ ] Raster preview is sufficiently high resolution.
- [ ] Editable source is included where requested.

## Reproducibility
- [ ] Plot source data is included.
- [ ] Plot script executes without errors.
- [ ] Dependencies and regeneration instructions are stated.
- [ ] Synthetic/example data is explicitly labelled.
- [ ] No source-paper PDF or copied figure has been bundled.
