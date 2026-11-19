# Domain Routing Matrix

Use this matrix after classifying the scientific purpose of the figure. It is a routing aid, not a fixed style guide.

| Domain | Common figure families | Visual grammar and critical checks |
|---|---|---|
| Circuits, electronics, and computing | Schematics, system architecture, datapaths, timing, memory maps | Use conventional symbols; preserve signal direction, widths, active levels, clocks, reset polarity, pipeline boundaries, and interface names. |
| Communications and signal processing | Waveforms, spectra, constellations, filter responses, link architecture, Pareto plots | Label sampling rate, frequency/time units, normalization, phase convention, and signal-processing order. |
| AI, machine learning, and computer vision | Neural-network architecture, training pipeline, attention/feature maps, confusion matrix, ROC/PR, ablation | Distinguish data, model blocks, training/inference, predictions, and evaluation. Define color scales and metrics. |
| Biomedical engineering and life sciences | Experimental flow, device/sensor design, microscopy, pathology, cell maps, medical imaging, survival/forest plots | Preserve cohort definitions, sample sizes, image provenance, ROI, scale bars, orientation, statistical tests, and uncertainty. |
| Robotics, automation, and control | Robot architecture, sensor fusion, coordinate frames, trajectories, state machines, sequence diagrams | Label coordinate frames and transformations; distinguish local/global maps, measured/planned paths, and control/measurement arrows. |
| Power and energy | Single-line diagrams, microgrid topology, converter circuits, control loops, operating-state diagrams, efficiency curves | Distinguish physical power flow from information/control flow; label voltage/current/power units and operating conditions. |
| Antennas and electromagnetics | Dimensioned antenna geometry, arrays, current/field maps, S-parameters, polar radiation patterns | State frequency, polarization, coordinate axes, reference plane, gain units, and whether data are simulated or measured. |
| Remote sensing and geospatial science | Map panels, image segmentation, change detection, spatial masks, trajectories, image-text fusion | Preserve map projection, north direction, scale, resolution, acquisition time, spatial extent, and class-mask semantics. |
| Materials and physical sciences | Crystal structures, microscopy, diffraction, spectra, phase maps, stress-strain plots | Preserve sample identity, orientation, scale bars, acquisition conditions, physical units, and phase/region definitions. This domain is included as a general adapter but is less represented in the current IEEE case corpus. |
| Software and information systems | Component diagrams, data-flow, deployment, protocol sequence, state machines | Distinguish logical components from deployment nodes, control flow from data flow, and synchronous from asynchronous messages. |

## Choosing the right visual grammar

### If the figure explains structure

Use a system diagram, schematic, or model architecture. Show boundaries, components, and directed relationships. Do not add implementation detail that the source does not support.

### If the figure explains a process

Use a flowchart, state machine, sequence diagram, or experimental workflow. Select the diagram based on whether the message is order, state, interaction, or protocol.

### If the figure explains measured results

Use a plot suited to the data type. Keep axes, units, sample size, uncertainty, and statistical definitions explicit.

### If the figure explains spatial evidence

Use maps, image panels, microscopy, masks, trajectories, or field maps. Preserve coordinate systems, scale, and image provenance.

### If the figure compares alternatives

Use aligned panels with consistent scales, labels, and visual encodings. A reader should be able to compare the alternatives without mentally recalibrating each panel.

## Do not over-generalize

- Do not use the same palette for all research domains.
- Do not use a generic flowchart to replace a real circuit schematic.
- Do not use a bar chart for data whose spatial arrangement is the scientific result.
- Do not use a heatmap when the underlying values are categorical unless the legend makes the encoding clear.
- Do not convert photographs, microscopy, or medical images into vector cartoons when the image evidence itself matters.
