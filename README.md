# IEEE-Figure-Skill

**A domain-neutral Agent Skill for publication-ready scientific figures in IEEE-style research.**

The project is designed for researchers across engineering, computing, physical sciences, and biomedical fields. It does not assume that every paper should look like a hardware block diagram. It first identifies the scientific purpose of a figure, then selects an appropriate visual grammar.

## What it helps create

- System and architecture diagrams
- Algorithms, workflows, state machines, and sequence diagrams
- AI/ML model architectures and data pipelines
- Experimental setups and measurement geometries
- Scientific illustrations and conceptual mechanisms
- Quantitative plots and statistical graphics
- Microscopy, medical-image, and remote-sensing panels
- Spatial maps, robot trajectories, and antenna patterns
- Multi-panel figures, tables, and mathematical illustrations

## Research domains

The Skill includes domain adapters for:

1. Circuits, electronics, and computing
2. Communications and signal processing
3. Artificial intelligence and computer vision
4. Biomedical engineering and life sciences
5. Robotics, automation, and control
6. Power systems and energy
7. Antennas and electromagnetics
8. Remote sensing and geospatial science
9. Materials and physical sciences

These are starting domains, not a claim that every subfield has already been comprehensively surveyed.

## Design philosophy

- **Scientific meaning before decoration.**
- **Figure type before color palette.**
- **Editable source before flattened artwork**, where practical.
- **Venue instructions before generic defaults.**
- **Evidence before inference.**
- **Accessibility and reproducibility are part of figure quality.**

There is no single universal IEEE figure style. Different research communities use different visual grammars, and the target journal or conference may publish its own artwork instructions.

## Install and use

1. Clone this repository or download the ZIP archive.
2. Copy the repository root folder into the skills directory supported by your agent. If the platform requires a lowercase skill folder, rename the folder to ieee-figure-skill.
3. Make sure the agent can read SKILL.md and the referenced files under references/.
4. Ask the agent to create or refine a figure.

Example requests:

- “Use IEEE-Figure-Skill to turn this method description into a clear, editable system architecture.”
- “Analyze these paper figures and separate observed design patterns from your recommendations.”
- “Create a publication-ready multi-panel figure from these CSV files. Preserve all values and units.”
- “Create a medical-image panel layout with consistent scale bars and ROI labels. Do not alter the underlying image evidence.”
- “Turn this robotics pipeline into a system overview and a separate state diagram.”
- “Generate a polar radiation-pattern plot from the supplied measurement data.”
- “Inspect this source code and draw only the data flow that is supported by the implementation.”

## Repository structure

- SKILL.md — main domain-neutral instructions.
- references/ieee-publication-baseline.md — IEEE author guidance and submission caveats.
- references/ieee-paper-corpus.md — cross-domain IEEE literature examples and evidence levels.
- references/domain-routing-matrix.md — domain-specific visual grammar.
- references/figure-type-guidelines.md — detailed figure-type guidance.
- references/color-and-typography.md — accessible design principles.
- references/visualization-ethics.md — scientific data and image integrity.
- references/quality-checklist.md — pre-delivery validation.
- references/paper-style-analysis.md — original hardware-focused seed analysis, retained as an optional specialty reference.
- templates/ — reusable diagram and plotting templates.
- examples/ — original illustrative examples across several domains.

## Publication requirements

The official IEEE author guidance provides useful baseline information on vector artwork, raster resolution, and column widths. However, always check the target publication's current instructions: requirements can vary by journal, conference, article type, and submission system.

Official resources:
- IEEE Author Center — Create Graphics for Your Article: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/
- IEEE Author Center — Resolution and Size: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/
- Proceedings of the IEEE — Guidelines for Figures and Tables: https://proceedingsoftheieee.ieee.org/resources/guidelines-for-figures-and-tables/

## Copyright and research integrity

The repository stores bibliographic references, high-level observations, original examples, and editable templates. It does not redistribute the source papers or reproduce their copyrighted figures. The original HBM/RS examples from the first version remain optional hardware-domain examples; they no longer define the Skill's default scope.

Repository: https://github.com/NRMAO/IEEE-Figure-Skill
