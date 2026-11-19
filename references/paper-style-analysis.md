> **Scope note (v0.2.0):** This file records the original hardware- and memory-focused seed literature from v0.1.0. It is retained as an optional specialty case study, not as the default visual style or scope of IEEE-Figure-Skill. For the expanded cross-domain IEEE corpus, use references/ieee-paper-corpus.md. Some papers in this original seed set are not IEEE publications; their publisher/venue status is identified in the entries below.

# Paper Style Analysis

## Scope and method

Eight unique papers were reviewed from the nine uploaded PDFs. The two copies of the Kwon et al.
2026 paper were treated as one source. Figure-bearing pages were visually inspected; captions and
surrounding text were used to identify each figure's purpose. Page numbers below refer to the PDF
page numbers (not necessarily the printed journal page numbers).

This is a **visual analysis**, not an official IEEE style specification. Font family, point size,
stroke width, and exact HEX values are not asserted unless directly measurable. Color descriptions
are qualitative; any suggested palette in the design-system reference is a new reusable palette,
not a claim that every source paper used those exact values.

---

## 1. Kwon et al., 2026 — Hardware-Efficient RS SSEC Decoder

**Venue:** IEEE Transactions on Very Large Scale Integration (VLSI) Systems, vol. 34, no. 8,
Aug. 2026. **DOI:** `10.1109/TVLSI.2026.3692208`.

**Figure locations and content**
- PDF p. 2: Fig. 1 general SSEC RS decoding process; Fig. 2 conventional LUT-based decoder;
  Fig. 3 general LUT vs. composite-field GF inverse; Fig. 4 proposed SSEC decoding process.
- PDF p. 3: Fig. 5 error-location vector generation; Fig. 6 proposed error-vector generation.

**Observed visual language**
- Predominantly monochrome, white background, thin dark outlines, simple rectangular functional
  blocks, conventional logic symbols, and direct signal/math labels.
- Arrows and wires carry the explanation; decoration is minimal.
- The figures are compact and designed to fit a dense two-column journal layout.
- Mathematical symbols are integrated into block labels and signal paths rather than moved into
  decorative callouts.
- Fig. 3 uses paired subfigures (a)/(b) to compare two implementations; Fig. 5/6 decompose the
  proposed hardware into understandable functional stages.

**Reusable lessons**
- Best reference for RS decoder datapaths, GF arithmetic blocks, LUT comparison, and one-hot
  error-location logic.
- Use a small number of high-information blocks and explicit signal names.
- Prefer monochrome for dense hardware logic; use color only when it clarifies a functional
  distinction.
- Separate conceptual decoding flow from detailed hardware realization.

**Caution**
- The paper is specifically for RS(19,17) single-symbol correction. Do not generalize its
  comparison-based search architecture to arbitrary multi-symbol RS decoders without checking
  the code parameters and derivation.

---

## 2. Hamburg et al., 2024 — Unraveling Codes for DRAM

**Source:** arXiv:2401.10688v2 (May 27, 2024), Rambus Inc. preprint. This is not an IEEE journal
publication in the supplied PDF.

**Figure locations and content**
- PDF p. 4: Fig. 1 interleaving with three subcodes.
- PDF p. 5: Fig. 2 DDR5 bit-to-symbol assignments; Fig. 3 unraveling with two interleaved codes.
- PDF p. 6: Fig. 4 comparison of code configurations, with best or near-best values highlighted.
- PDF p. 11: Fig. 5 high-reliability code parameters and failure probabilities.

**Observed visual language**
- Matrix-like codeword layouts and symbol-position diagrams are used to explain abstract code
  transformations.
- Fig. 2 explicitly assigns blue to user data, green to metadata, and red to parity. The colors
  encode data semantics rather than decoration.
- Tables use restrained rules and selective green highlighting to direct attention to the best
  or near-best entries.
- Diagrams are mostly geometric and label-driven, with repeated alignment across rows and columns.

**Reusable lessons**
- Use consistent semantic colors for data, metadata, parity, and protection regions.
- For interleaving or codeword mapping, use aligned grids with position labels and clear legends.
- Highlight only the most important table entries; avoid coloring every cell.
- Use side-by-side alternatives when explaining different mappings.

---

## 3. Jung and Erez, 2023 — Component-Level DRAM Fault Model

**Venue:** 56th IEEE/ACM International Symposium on Microarchitecture (MICRO 2023).
**DOI:** `10.1145/3613424.3614294`. ACM conference paper.

**Figure locations and content**
- PDF p. 3: Fig. 1 DRAM mat structure; Fig. 2 bank-per-subbank column remapping logic.
- PDF p. 4: Fig. 3 examples of mat-level error patterns.
- PDF p. 5: Fig. 4 multi-row error patterns.
- PDF p. 6–7: Fig. 5 multi-column error patterns; Fig. 6 total-variation-distance statistics;
  Fig. 7 address protection for on-die ECC.
- PDF p. 9–11: Figs. 8–11 DUE/SDC probabilities, ECC comparisons, and component-failure
  contributions.

**Observed visual language**
- Combines structural hardware diagrams with data-heavy reliability plots.
- Error maps use two-dimensional row/column coordinates, with subfigures for different fault
  patterns and vendors/components.
- Statistical plots use bars, vertical uncertainty/error indicators, and grouped comparisons.
- Chart panels have compact labels and legends; color is used to separate categories, while axes
  and data marks remain visually dominant.
- Multi-panel arrangements are important because comparisons are organized by fault class,
  memory type, or vendor.

**Reusable lessons**
- For spatial or address-distribution data, use a true 2D map rather than a generic bar chart.
- Show uncertainty with error bars or intervals when the data supports them.
- Keep panel scales and axis ranges comparable when the intent is direct comparison.
- In grouped bars, use a stable mapping from color to ECC scheme across every panel.
- Keep architecture figures and statistical figures visually related but not identical.

---

## 4. Kim and No, 2026 — Spotty and Adjacent Symbol Error Correction

**Venue:** Physical Communication, vol. 76 (2026), article 103067.
**DOI:** `10.1016/j.phycom.2026.103067`. This is an Elsevier journal paper, not an IEEE publication.

**Figure locations and content**
- PDF p. 3: Fig. 1 spotty and adjacent symbol error in a 2D array.
- PDF p. 6: Fig. 2 adjacency illustration.
- PDF p. 8: Figs. 3–4 matrix reduction and error-pattern placement.
- PDF p. 9: Figs. 5–6 parity overhead comparisons.
- PDF p. 10: Fig. 7 frame-error-rate comparison.
- PDF p. 12: Fig. 8 overall low-complexity syndrome decoder description.

**Observed visual language**
- Error-pattern illustrations use grids, bit/symbol blocks, and limited contrasting fills to show
  affected versus unaffected positions.
- Mathematical transformation diagrams use matrices, arrows, and boxed regions.
- Performance charts use multiple line styles and colors to distinguish code families.
- The frame-error-rate plot uses logarithmic axes; this is appropriate to the plotted probability
  range rather than a general styling choice.
- The decoder overview is a compact, labeled block diagram.

**Reusable lessons**
- Use grid-based illustrations for burst, spotty, and adjacent error patterns.
- Combine color with position, outline, or hatch pattern so meaning survives grayscale printing.
- Use log axes only when the metric spans orders of magnitude and label them clearly.
- Use different line styles as a second encoding channel in multi-series charts.

---

## 5. Lim et al., 2025 — Two-Tiered ECC Configuration for HBM

**Venue:** IEEE Transactions on Circuits and Systems II: Express Briefs, vol. 72, no. 9,
Sep. 2025. **DOI:** `10.1109/TCSII.2025.3593226`.

**Figure locations and content**
- PDF p. 2: Fig. 1 two-tiered ECC configuration in HBM.
- PDF p. 3: Fig. 2 OD-ECC decoder error-correction logic; Fig. 3 error-correction algorithm.
- PDF p. 4: hardware-overhead and correction-capability comparison tables.

**Observed visual language**
- Predominantly monochrome, compact, and information-dense.
- The HBM overview combines a simplified stack/physical structure with data-path and ECC
  processing blocks.
- Decoder logic and algorithm flow are shown as separate figures: one emphasizes hardware
  structure, the other emphasizes procedural order.
- Tables use simple row/column organization and minimal decoration.

**Reusable lessons**
- Separate physical/system placement from internal decoder logic.
- Use a dedicated algorithm flowchart when the processing sequence is too complex for the
  architecture diagram.
- For dense two-column figures, prefer a small number of clearly labeled blocks over elaborate
  pictorial elements.

---

## 6. Shin and Kim, 2025 — ROSE for HBM3

**Venue:** 2025 International Conference on Electronics, Information, and Communication (ICEIC).
**DOI:** `10.1109/ICEIC64972.2025.10879768`.

**Figure locations and content**
- PDF p. 2: Fig. 1 overview of an eight-core-die HBM3 stack.
- PDF p. 3: Fig. 2 RS H-matrix example; Fig. 3 ROSE decoder block diagram.

**Observed visual language**
- The HBM stack uses a restrained colored 3D/perspective illustration to communicate physical
  organization.
- The decoder uses a small set of pale colored module fills to distinguish functional regions.
- Blue/cyan is prominent; red/pink and green are used as secondary distinctions.
- Mathematical matrix content remains mostly monochrome.

**Reusable lessons**
- A 3D stack view can be useful for system placement, but should not replace a precise datapath
  diagram.
- Use pale fills with dark labels and outlines; avoid saturated fills behind small text.
- Keep matrix/formula figures separate from architecture overviews.

---

## 7. Shin and Park, 2025 — DBB-ECC for HBM3

**Venue:** IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems,
vol. 44, no. 8, Aug. 2025. **DOI:** `10.1109/TCAD.2025.3544964`.

**Figure locations and content**
- PDF p. 2: Fig. 1 single-bit error in a 16-bit symbol; Fig. 2 random two-bit error location
  types and syndrome patterns.
- PDF p. 3: Fig. 3 three-panel random double-bit error decoding process.
- PDF p. 4: Fig. 4 DBB-ECC decoder block diagram, DBE locator, and syndrome splitter.

**Observed visual language**
- Primarily black-and-white logic and bit-position diagrams.
- Error bits or selected positions are emphasized with red marks/crosses.
- The three-panel process figure uses repeated structure to compare cases (a), (b), and (c).
- Fig. 4 nests the high-level decoder and two detailed sub-blocks; the hierarchy is explicit.
- Tables are compact and mostly monochrome.

**Reusable lessons**
- For bit-level error patterns, use fixed-width bit cells and explicit bit indices.
- Highlight only the erroneous/selected bits; retain a stable positional layout across cases.
- Use aligned panels for algorithm cases so readers can compare changes directly.
- Show the decoder overview first, then expand the complex submodules.

---

## 8. Zhu et al., 2026 — HBM-CASO

**Venue:** 2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA).
**DOI:** `10.1109/ISCA66397.2026.00026`.

**Figure locations and content**
- PDF p. 3: Fig. 1 HBM organization, array/data layout, and code-space comparison.
- PDF p. 4: Fig. 2 evolution of HBM protection strategies.
- PDF p. 5: Fig. 3 baseline and HBM-CASO codeword organization.
- PDF p. 7–8: Figs. 4–5 available modes, codeword organization, and error-correction flow.
- PDF p. 9: Fig. 6 H matrices under baseline/R-mode/G-mode.
- PDF p. 12–13: Figs. 7–11 reliability and performance/power results.

**Observed visual language**
- Uses a richer but controlled color system than the compact IEEE Transactions briefs.
- Blue is prominent for memory/data structures; orange is used for selected processing units or
  emphasized regions; additional colors distinguish different codeword/data classes.
- System diagrams combine physical layout, logical organization, and explanatory callouts.
- Several figures use subpanels (a)–(d) with a common visual grammar.
- Evaluation figures include line charts, grouped bars, normalized performance, and power overhead.
- Figure 6 uses matrix-like visualizations to compare code structures.

**Reusable lessons**
- For multi-level memory organizations, combine a physical overview with a separate logical
  codeword/data-layout figure.
- Maintain stable colors for the same ECC mode across the paper.
- Use multi-panel figures to compare baseline and proposed modes under the same coordinate system.
- Avoid putting every implementation detail into the first system overview; progressively disclose
  the structure.

---

## Cross-paper synthesis

### Strongest references by task

| Task | Best source references |
|---|---|
| RS SSEC decoder logic and GF datapath | Kwon et al. 2026 |
| HBM physical/system organization | Lim et al. 2025; Shin & Kim 2025; Zhu et al. 2026 |
| Bit-level and symbol-level error patterns | Shin & Park 2025; Kim & No 2026 |
| Codeword/interleaving/mapping diagrams | Hamburg et al. 2024; Zhu et al. 2026 |
| Reliability maps and uncertainty plots | Jung & Erez 2023 |
| Multi-metric performance/reliability figures | Jung & Erez 2023; Zhu et al. 2026 |
| Compact logic and algorithm diagrams | Kwon et al. 2026; Lim et al. 2025; Shin & Park 2025 |

### Overall conclusions

1. Hardware logic figures are often most effective in monochrome; color is optional, not mandatory.
2. Color should encode stable semantics (data/parity, normal/error, baseline/proposed), not simply
   decorate modules.
3. Dense logic figures need explicit labels and carefully routed connectors more than pictorial
   styling.
4. System-level HBM diagrams benefit from layered disclosure: physical organization, codeword
   mapping, then decoder/dataflow.
5. Reliability and PPA charts need consistent legends, explicit units, comparable axes, and
   uncertainty indicators when available.
6. The same paper may use different visual grammars for architecture, bit patterns, matrices, and
   quantitative plots. The Skill must select style by figure type.
