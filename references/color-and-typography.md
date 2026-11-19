# Color and Typography

## 1. No universal palette

There is no single palette that should be imposed on all IEEE figures. Select colors based on the data, field conventions, accessibility, and consistency across the paper.

- Monochrome is often the clearest choice for dense schematics, equations, and logic diagrams.
- Color can identify groups, stages, signal classes, image masks, or competing methods.
- Use a restrained palette and reserve strong emphasis colors for meaningful distinctions.
- Do not use color as the only way to encode an important category.

## 2. Accessible categorical colors

For general categorical plots, a colorblind-conscious palette can be a starting point:

- Blue: #0072B2
- Vermilion: #D55E00
- Bluish green: #009E73
- Orange: #E69F00
- Sky blue: #56B4E9
- Reddish purple: #CC79A7
- Dark gray: #4D4D4D

This is an optional starting palette, not an IEEE requirement. Use fewer colors where possible. For many categories, combine color with line style, marker, hatch, direct labels, or panel separation.

Avoid relying on red/green distinctions. Check the figure in grayscale and, when practical, with a color-vision-deficiency simulator.

## 3. Continuous color scales

For heatmaps, segmentation confidence, microscopy intensities, field maps, and spatial densities:

- Use a sequential scale for low-to-high values.
- Use a diverging scale only when there is a meaningful center or reference value.
- Use a categorical palette for discrete classes.
- Include a colorbar with units or a clear label.
- Use the same scale across panels when direct comparison is intended.
- Avoid rainbow maps for quantitative values when they create false boundaries or uneven perceptual steps.

## 4. Typography

- Follow the target publication's current font and size instructions.
- Use a consistent type family and hierarchy across all figures in the paper.
- Keep labels concise and readable at the final physical size.
- Use italics for variables when mathematically appropriate, not for arbitrary emphasis.
- Preserve Greek letters, subscripts, superscripts, units, and symbol case.
- Avoid mixing unrelated font families or using decorative typefaces.
- Do not treat one recommended point size as universal across all IEEE venues.

Proceedings of the IEEE gives approximately 9–10 pt as a typography reference in its figure guidance. This is not a universal rule for every IEEE publication; check the target venue.

## 5. Lines, markers, and shapes

- Make lines and markers distinguishable at final print size.
- Use marker shapes and line styles as secondary encodings.
- Use consistent stroke weights for related diagrams.
- Avoid overly thin axes, light gray labels, or pale lines that disappear when printed.
- Do not add gradients, shadows, or pseudo-3D effects unless they encode a real scientific property.

## 6. Domain-specific exceptions

- Microscopy and medical images may require a fixed intensity or modality-specific display convention.
- Antenna patterns and electromagnetic field plots may use field-specific conventions and units.
- Circuit schematics may be more readable in monochrome.
- Maps may need a color scheme that distinguishes land cover, elevation, or confidence.
- Multi-panel comparisons must preserve the same semantic color mapping across the paper.

When the user's existing paper has an established palette, preserve it unless the user requests a change.
