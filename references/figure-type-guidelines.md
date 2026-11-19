# Figure-Type Guidelines

## Architecture / system overview

Purpose: communicate where major components sit and how information moves.

- Start with the system boundary and the reader's point of view.
- Separate physical components (dies, channels, banks, TSVs) from logical functions (ECC,
  controller, encoder, decoder).
- Use nested grouping only when hierarchy is real.
- Label data paths, parity paths, clocks, control, and interfaces.
- If the physical and logical views are both important, use separate panels.
- Avoid perspective 3D effects unless physical stacking is the message.

## Block diagram / datapath

Purpose: expose functional modules and their directed connections.

- Show all required modules and only the relevant interconnects.
- Distinguish combinational blocks from registers/pipeline stages.
- Mark replicated/parallel lanes with `×N` or lane indices.
- Show bus widths and signal names.
- Do not compress a multi-stage pipeline into a single box if latency/staging is important.
- Do not assume shared hardware merely because two operations are mathematically related.

## Algorithm flowchart

Purpose: show sequence, decisions, and iteration.

- Use a single main direction.
- Each decision has named branches.
- Keep formulas inside or beside the operation they define.
- Separate the algorithmic process from the corresponding hardware implementation.
- If a loop is important, show the loop condition and exit.
- Include input/output nodes.

## Dataflow / codeword / memory mapping

Purpose: explain where bits, symbols, parity, or metadata are placed.

- Use aligned grids and fixed cell sizes.
- Label row/column, symbol index, DQ, byte, channel, bank, or pseudo-channel dimensions.
- Use semantic fills and a legend.
- Highlight changed positions in the proposed design while keeping the baseline layout visible.
- When showing interleaving, show the mapping from original index to destination lane explicitly.

## Circuit / logic-gate structure

Purpose: communicate actual gate-level or near-gate-level logic.

- Use recognized logic symbols when possible.
- Label inputs, outputs, constants, and polarity.
- Keep fan-in/fan-out visible.
- Use explicit junction dots when wires connect.
- Avoid crossings and ambiguous overlaps.
- If the diagram is conceptual rather than transistor/gate accurate, label it as such.

## Timing / waveform diagram

Purpose: show temporal relationships.

- Use one horizontal time scale shared by all signals.
- Align transitions vertically when simultaneous.
- Label clock edges and relevant timing points.
- Distinguish high, low, unknown, and high-impedance states if present.
- Show setup/hold windows only when specified.
- Preserve active-low notation and reset polarity.
- Do not infer cycle counts from prose unless explicitly stated.

## Performance / PPA / reliability plots

Purpose: compare measured or simulated outcomes.

- Plot one metric per axis.
- Use units in axis labels.
- Keep method colors stable across panels.
- Use paired/grouped bars for discrete categories; lines for continuous sweeps.
- Include confidence/error bars only if available.
- Use logarithmic scales for orders-of-magnitude comparisons when appropriate.
- State whether lower or higher is better in labels/captions.
- For PPA, area, delay, power, throughput, and energy should normally be separate panels or
  clearly separated plots; do not combine incomparable units.
- Do not imply causality from a correlation plot.

## Table

Purpose: provide exact values in a compact form.

- Align numeric columns.
- Include units in headers.
- Keep decimal precision consistent.
- Highlight only meaningful best/worst values.
- Add footnotes for abbreviations and conditions.

## Mathematical / error-pattern illustration

Purpose: make a mathematical relation or error geometry visible.

- Keep notation consistent with the paper's equations.
- Use grid cells for bit/symbol positions.
- Highlight error locations without obscuring indices.
- Show transformations with arrows and intermediate states.
- Add a small legend if color/hatching is not self-evident.
- Do not replace a proof or equation with an oversimplified cartoon.
