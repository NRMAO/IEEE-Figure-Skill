# Reference Style Extraction Rubric

Use this checklist whenever the user supplies a reference figure, image, PDF page, SVG, or slide.

## 1. Evidence levels

Every extracted property must be traceable to an evidence level:

| Evidence label | Meaning | Example |
|---|---|---|
| <code>observed</code> | Directly visible or present in source metadata | White background; PDF reports an embedded font family |
| <code>measured</code> | Measured from the original file or rendered geometry | Canvas aspect ratio; SVG stroke width; pixel-sampled color |
| <code>visually_estimated</code> | Estimated from appearance, compression, or screenshot | Approximate HEX color; likely font family |
| <code>unknown</code> | Cannot be determined from available material | Exact font size in a flattened screenshot |

Do not convert a visual estimate into an exact claim. If the source is a screenshot or a downsampled image, note that sampled colors may differ from the original artwork.

## 2. Reference inspection

- Confirm the exact reference file and figure/panel the user intends.
- For a paper PDF, render the page and inspect the actual figure, not only its caption.
- Inspect at both full-page and enlarged/cropped scale when possible.
- Record whether the image is a native vector, a raster export, or a screenshot if that can be determined.
- For multi-panel figures, inspect the full composition and representative individual panels.
- If the file is inaccessible, password-protected, corrupted, or not visually inspectable in the current runtime, say so.

## 3. Extraction dimensions

### Canvas and composition
- aspect ratio and approximate physical dimensions;
- background and panel background;
- number of panels, panel arrangement, gutters, margins, whitespace;
- reading order, alignment, grouping, and visual hierarchy.

### Typography
- font family only when known; otherwise record a ranked fallback or <code>unknown</code>;
- title, subtitle, panel label, axis, tick, legend, annotation, and caption hierarchy;
- font weight, capitalization, mathematical notation, superscripts, subscripts, and symbol treatment;
- distinguish embedded metadata/measured sizes from estimates.

### Color
- semantic roles: primary, secondary, accent, neutral, text, background, grid;
- approximate or sampled HEX values and where each is used;
- category-to-color mapping;
- grayscale and color-vision-deficiency distinguishability;
- whether color is redundant with line style, marker, hatch, or label.

### Geometry and marks
- module/plot borders, corner treatment, stroke widths, arrows and arrowheads;
- connector routing, line styles, marker shape/size, gridline treatment;
- spacing between elements and consistency across repeated components.

### Legends, labels, and annotations
- legend location and frame;
- axis names and units, scale bars, coordinate axes, north arrows, reference markers;
- panel labels such as (a), (b), (c);
- callouts, leader lines, abbreviations, symbols, and caption conventions.

## 4. Multi-reference synthesis

Create three lists:
1. **Shared traits:** repeated across most references and suitable for a reusable profile.
2. **Type-specific traits:** useful only for a particular figure family.
3. **Reference-specific traits:** unique details that should not be generalized.

Do not average conflicting styles blindly. If two references have incompatible typography or visual density, retain separate profiles or ask which reference should take priority.

## 5. Style profile quality

The profile should:
- follow <code>templates/reference-to-figure/style-profile.schema.json</code>;
- use <code>templates/reference-to-figure/style-profile.example.json</code> as a starter;
- record source file names without embedding copyrighted source images;
- include confidence and uncertainty notes;
- avoid invented precision;
- separate universal design tokens from figure-family-specific tokens;
- be portable and reusable across future figures.

## 6. Reuse boundary

The style profile may capture high-level design choices such as palette roles, typography hierarchy, line weights, whitespace, panel rhythm, and legend placement.

It must not be used to reproduce the reference's exact scientific content, data, wording, unique icons, distinctive artwork, or full composition. The new figure must be independently designed around the user's target science. When a reference is a published figure, avoid close tracing or near-duplicate layouts.

## 7. Final review

Before delivery, compare the new figure with:
- the user's scientific source of truth;
- the extracted style profile;
- the intended figure family;
- the target publication's current instructions.

Report which style properties were reused, which were adapted, and which could not be reliably extracted.
