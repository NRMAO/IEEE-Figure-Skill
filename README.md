# IEEE-Figure-Skill

An AI Agent Skill for creating publication-ready technical figures for IEEE-style research papers,
with a focus on RS/ECC, HBM/DRAM, chiplet interconnects, and FPGA/ASIC hardware architecture.

## What it does

- Extracts reusable figure-design principles from supplied papers.
- Converts architecture descriptions, RTL, equations, and algorithms into technical diagrams.
- Creates editable SVG, Mermaid, Graphviz, Python/Matplotlib, TikZ, or PPTX sources as appropriate.
- Produces vector PDF/SVG outputs and PNG previews.
- Generates quantitative plots from supplied CSV/Excel data without inventing measurements.
- Checks technical connectivity, labels, print-size legibility, and visual consistency.

## Install / use

1. Copy the `ieee-figure-skill/` directory into the skills directory supported by your agent.
2. Ensure the agent can read `SKILL.md` and the referenced files under `references/`.
3. Ask the agent to create or refine a figure, for example:
   - "Use the IEEE Figure Skill to draw a block-level RS(19,17) SSEC decoder from this architecture description."
   - "Analyze the figures in this PDF and summarize the visual design rules."
   - "Use this CSV to generate area, delay, and power comparison plots."
   - "Inspect this RTL and draw the module hierarchy and datapath. Do not infer connections that are not present."

The exact skill installation path depends on the agent platform. The skill follows the common
Agent Skills convention: a directory containing a `SKILL.md` file with YAML frontmatter.

## Design philosophy

The default hardware-architecture style is restrained and technical: white background, dark
outlines, compact labels, carefully routed arrows, muted blue module fills, and limited orange
emphasis. Monochrome remains a first-class option and is often preferable for dense logic diagrams.

The figure type determines the visual grammar. A timing diagram, a block diagram, and a
performance plot should not be forced into one template.

## Repository structure

```text
IEEE-Figure-Skill/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── references/
│   ├── paper-style-analysis.md
│   ├── ieee-figure-design-rules.md
│   ├── color-and-typography.md
│   ├── figure-type-guidelines.md
│   └── quality-checklist.md
├── templates/
│   ├── architecture-diagram/
│   ├── flowchart/
│   ├── timing-diagram/
│   └── performance-plots/
└── examples/
    ├── architecture-example/
    ├── algorithm-example/
    └── performance-example/
```

## Paper sources and copyright

The style analysis records bibliographic metadata, figure topics, and high-level visual observations.
It does not include the uploaded PDFs or copies of their figures. The example diagrams are original
illustrations and are not intended to reproduce any paper's figure.

## Important limitations

- No universal "IEEE figure style" overrides the target journal's author instructions.
- Exact fonts, point sizes, and colors in rasterized PDFs may be difficult to identify. Approximate
  observations are labelled as such.
- A technically correct RTL-derived diagram requires the relevant source code and complete
  connectivity. Module names alone are not enough.
- Performance comparisons require real input data and comparable measurement conditions.

Repository: https://github.com/NRMAO/IEEE-Figure-Skill (public, branch `main`).
