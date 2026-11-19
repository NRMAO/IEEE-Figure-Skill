# IEEE Figure Design Rules

These are reusable design recommendations synthesized from the supplied papers. They are not a
substitute for the target IEEE journal's author instructions.

## 1. Design principles

1. **One figure, one primary message.** A figure may contain subpanels, but the reader should be
   able to state its purpose in one sentence.
2. **Technical semantics first.** Shape, color, line style, and position must reflect the system.
3. **Use the minimum visual vocabulary.** Reuse a small set of module shapes, connector styles,
   and color tokens.
4. **Design at final size.** Check the figure at its intended single-column or double-column width.
5. **Prefer vector output.** Keep text and lines as vectors whenever possible.
6. **Use progressive detail.** Separate system overview, detailed datapath, and algorithm sequence
   when one drawing becomes crowded.
7. **Make grayscale safe.** Color must not be the only way to distinguish critical categories.

## 2. Layout and reading order

### Architecture and datapath
- Default to left-to-right for data movement; use top-to-bottom for hierarchical or staged flows.
- Place primary inputs on the left and primary outputs on the right.
- Keep the dominant datapath visually continuous.
- Place control/status signals above or below the datapath, not through its center.
- Use grouping boundaries for modules that share a function or clock domain.
- Use consistent alignment and spacing; align repeated lanes and replicated processing elements.
- Put bus widths near the bus, e.g. `16-bit`, `N symbols`, or `[15:0]`.
- If a bus branches, show an explicit junction; do not rely on visual proximity.

### Algorithm and process
- Use one main direction, normally top-to-bottom.
- Use process rectangles for operations, decision diamonds only for genuine branches, and
  terminal shapes for start/end.
- Label both branches of a decision (e.g. Yes/No, valid/invalid).
- Avoid long return arrows crossing the whole diagram; use compact loop routing.
- Keep the algorithm's mathematical operation and the hardware block name distinct when needed.

### Multi-panel figures
- Use panel labels `(a)`, `(b)`, `(c)` consistently, preferably at the top-left of each panel.
- Keep panels aligned and use equal plot dimensions when comparing the same metric.
- Share a legend when the same encoding applies to every panel.
- Use separate legends only when the encoding changes.
- Do not shrink each panel so far that its labels become unreadable.

## 3. Diagram grammar

| Meaning | Recommended representation |
|---|---|
| Functional module | Rectangle with concise title |
| Major subsystem | Light-outline grouping box or subtle tinted region |
| Decision | Diamond with labeled outgoing branches |
| Register / state | Rectangle with clock or state annotation |
| Memory / table | Rectangle with stacked-page or table hint, if useful |
| XOR | XOR symbol or clearly labeled `⊕` block |
| GF multiply | `×` or `GF multiply` block; annotate field/constant |
| Comparator | `==` / comparator block; label compared values |
| MUX | Standard trapezoid or labeled `MUX` rectangle |
| Clock | Distinct clock line/style; do not confuse with data |
| Reset | Explicit polarity and active level |
| Error / exception path | Red accent plus label; do not rely on red alone |
| Optional / bypass path | Dashed line with explicit label |

Use standard symbols where they improve recognition, but do not introduce ambiguous or unfamiliar
symbol conventions without a legend.

## 4. Connector and line rules

- Use solid arrows for primary data/control flow.
- Use dashed arrows for optional, bypass, or configuration paths only when defined.
- Use a distinct but restrained line style for clock/reset when needed.
- Use orthogonal routing for block diagrams where possible.
- Avoid connector crossings. If unavoidable, use a clear bridge/jump convention and preserve
  unambiguous junction semantics.
- Label a signal once near its source or destination unless repetition is needed to disambiguate.
- Arrowheads must be visible at final print size.
- Avoid using a connector line as a visual divider.

## 5. Color semantics

Default semantic mapping:
- normal data / main datapath: blue;
- auxiliary or shared processing: teal;
- proposed/optimized block or key contribution: orange;
- error/exception/invalid condition: red;
- neutral/reference/baseline: gray;
- parity/check symbols: green only if used consistently and explained.

These are defaults, not fixed rules. If the source paper or user's existing figures establish a
different mapping, preserve that mapping throughout the project.

## 6. Plot rules

- Every axis must have a metric name and unit where applicable.
- Use a legend only when more than one series/category needs identification.
- Keep line widths and marker sizes readable at final size.
- Use markers and line styles in addition to color for important series.
- Add error bars or confidence intervals only when supported by the source data.
- Bar charts should normally start at zero; if a truncated axis is scientifically necessary, make
  the break conspicuous and explain it.
- Use logarithmic axes only when the data span orders of magnitude or the analysis requires it.
- Keep the same color-to-method mapping across related panels.
- Do not combine metrics with incompatible units on one axis. Use separate panels or clearly
  labeled secondary axes only when justified.
- For normalized metrics, state the baseline and normalization formula.

## 7. Tables

- Prefer sparse horizontal rules and avoid heavy vertical gridlines unless the data structure
  genuinely requires them.
- Align numeric values by decimal point or right edge.
- Include units in column headings.
- Use bold or restrained tint to highlight the best value; define whether higher or lower is better.
- Preserve significant digits and statistical notation.
- Do not color every cell.

## 8. Captions and panel references

- Caption text should explain what is shown, define non-obvious abbreviations, and identify panels.
- Do not repeat every label already visible in the figure.
- Keep panel labels consistent between the figure and caption.
- Ensure all subfigures referenced in the caption exist and appear in the intended order.

## 9. IEEE layout adaptation

- Confirm the target publication's column width, font requirements, and file-format rules.
- If not supplied, use an approximate single-column width of 3.5 in (89 mm) and double-column width
  of 7.16 in (182 mm) as starting points only; verify against the specific template.
- Avoid resizing a wide figure to single-column width if doing so makes text illegible.
- For dense hardware architecture, consider a double-column figure or split the overview and detail.
