# Color and Typography

## 1. Default palette

The palette below is a **new project palette** informed by the restrained blue/teal/orange accents
seen in several supplied papers. It is not an exact extraction from any one paper.

| Token | HEX | Use |
|---|---|---|
| Ink | `#202A35` | Main text, outlines, axes |
| Neutral | `#667085` | Secondary labels, baseline/reference |
| Light gray | `#F2F4F7` | Neutral module fill |
| Blue | `#2468A2` | Main data path / primary module |
| Blue tint | `#EAF2F8` | Primary module background |
| Teal | `#238477` | Auxiliary/shared processing |
| Teal tint | `#E8F4F1` | Auxiliary module background |
| Orange | `#D9822B` | Proposed block / emphasis |
| Orange tint | `#FFF2E3` | Highlight background |
| Red | `#B54747` | Error, invalid, exception |
| Red tint | `#FCEEEE` | Error region background |
| Green | `#4D8A63` | Parity/check or positive result, if semantically defined |
| Green tint | `#EDF5EF` | Positive-result background |
| White | `#FFFFFF` | Canvas |

### Plot palette

For categorical plots, use a colorblind-conscious set and preserve the mapping across panels:

- Blue `#0072B2`
- Vermilion `#D55E00`
- Bluish green `#009E73`
- Orange `#E69F00`
- Sky blue `#56B4E9`
- Reddish purple `#CC79A7`
- Dark gray `#4D4D4D`

Do not use all colors in one chart unless the number of categories requires them. For two-series
comparisons, blue/orange is usually sufficient. For baseline vs proposed, use neutral gray vs
blue or orange.

## 2. Contrast and grayscale

- Use dark text on light fills.
- Do not place small text on saturated color blocks.
- Keep adjacent module fills visibly different, but use outlines and labels as additional cues.
- Check a grayscale export. If categories collapse into the same gray, add line style, hatch,
  marker, or label distinctions.
- Reserve red for errors or exceptions; avoid using red as a generic decoration.

## 3. Typography defaults

These are recommended starting values, not mandatory IEEE rules:

| Element | Starting point at final size |
|---|---:|
| Main module label | 8–9 pt |
| Secondary module text | 7–8 pt |
| Axis labels | 8–9 pt |
| Tick labels | 7–8 pt |
| Panel label | 9 pt bold |
| Figure annotations | 7–8 pt |

- Use one sans-serif family for diagram labels (e.g. Arial, Helvetica, or a metrically compatible
  sans-serif) unless the journal or project requires another.
- Use a consistent serif/math font for equations when the chosen renderer supports it.
- Keep module labels in sentence case or concise title case; avoid inconsistent capitalization.
- Use italic for scalar mathematical variables and upright text for descriptive words.
- Preserve exact subscripts, superscripts, Greek letters, and bit indices.
- Avoid font sizes below 6.5 pt at final print size unless unavoidable and permitted by the venue.
- Do not assume that a PDF's embedded font name equals the visual font family; inspect metadata or
  font embedding when exact identification matters.

## 4. Line and shape defaults

Recommended starting values:
- module outline: 0.8–1.0 pt;
- primary signal line: 0.9–1.2 pt;
- secondary/annotation line: 0.6–0.8 pt;
- plot axes: 0.7–0.9 pt;
- gridline: 0.35–0.5 pt, light gray;
- corner radius: modest (4–7 px in SVG at a 1000 px-wide canvas).

Avoid excessively rounded UI-style cards. Academic diagrams should look like technical figures,
not application dashboards.

## 5. Consistency

Store the palette as reusable tokens in source code. Never manually choose a new shade for the same
semantic role in each figure. When inheriting an existing paper's color system, record the mapping
and apply it consistently across all related figures.
