# Cross-Domain IEEE Paper Corpus

## Purpose and limits

This corpus broadens the original hardware-centric seed set. It samples IEEE journals across biomedical engineering, robotics, power and control, signal processing, remote sensing, antennas, AI, and industrial systems.

It is a **representative visual casebook**, not a systematic review of all IEEE publications. Papers are selected because their methods or reported results expose useful figure families.

### Evidence labels

- **A — Full text inspected:** an accessible published paper or author manuscript was inspected for figure captions, structure, and selected figure pages.
- **B — Text/caption evidence:** accessible paper text or figure descriptions were inspected, but complete visual rendering was not consistently available.
- **C — Metadata/abstract only:** the bibliographic record and abstract were inspected. No detailed claim is made about the paper's visual style.

The repository contains no source-paper PDFs or copied paper figures. Links below point to the publisher record, DOI, or an author/institutional copy where available.

---

## A. Full-text or figure-level case studies

### 1. Biomedical sensing and instrumentation

**Sarah Tonello et al., “Design and in vitro Characterization of a Wearable Multisensing System for Hydration Monitoring.”**  
IEEE Transactions on Instrumentation and Measurement, vol. 73, 2024.  
DOI: https://doi.org/10.1109/TIM.2024.3369161  
IEEE record: https://ieeexplore.ieee.org/document/10452315/  
Accessible author/institutional version: https://research.unipd.it/handle/11577/3511215  
Evidence: **A — full text and figure descriptions inspected.** The accessible article identifies a CC BY 4.0 license.

**Useful figure families observed**
- Physical device and sensor layout (Fig. 1).
- Cross-sectional sensing geometry and field-line illustration (Fig. 2).
- Equivalent electrical circuits (Figs. 3–4).
- End-to-end system architecture from user/wearable to wireless receiver, cloud, and caregiver (Fig. 5).
- Detailed hardware-level readout architecture (Fig. 6).
- Stacked logarithmic-frequency response plots for different hydration conditions (Figs. 7–8).

**Transferable lessons**
- A single research paper can legitimately mix photographs, physical illustrations, circuit schematics, system diagrams, and quantitative plots.
- Use a physical cross-section when the measurement mechanism depends on spatial penetration or tissue layers.
- Keep system-level architecture separate from detailed electronics.
- For frequency-response plots, preserve logarithmic axes, units, and the mapping between conditions and line styles/colors.

### 2. Power systems, distributed control, and IoT

**Hao Tu et al., “An IoT-Based Framework for Distributed Generic Microgrid Controllers.”**  
IEEE Transactions on Control Systems Technology, vol. 32, no. 5, pp. 1692–1705, 2024.  
DOI: https://doi.org/10.1109/TCST.2024.3378989  
IEEE record: https://ieeexplore.ieee.org/document/10483264/  
Accessible author version: https://www.freedm.ncsu.edu/wp-content/uploads/2023/09/DistributedMgController_elsarticle-2.pdf  
Evidence: **A — full author manuscript inspected.**

**Useful figure families observed**
- Controller functions and distributed microgrid overview (Fig. 1).
- Communication graph among distributed energy-resource nodes (Fig. 2).
- IoT-based controller architecture and message interactions (Fig. 3).
- State-machine logic for grid-connected, islanded, and transition states (Fig. 4).
- Sequence diagrams for grid-connected operation, islanding, and reconnecting (Figs. 5–9).
- Physical/network test-system topology (Fig. 10).

**Transferable lessons**
- Separate the physical energy system, the controller architecture, and the software communication model.
- Use state diagrams for mutually exclusive operating states and sequence diagrams for time-ordered interactions.
- Label communication edges and message types; an unlabeled network graph is not enough.
- Use one system overview followed by focused detail figures.

### 3. Communications and signal processing

**Shixiong Wang et al., “Robust Waveform Design for Integrated Sensing and Communication.”**  
IEEE Transactions on Signal Processing, vol. 72, pp. 3122–3138, 2024.  
DOI: https://doi.org/10.1109/TSP.2024.3410142  
IEEE record: https://ieeexplore.ieee.org/document/10549948/  
Accessible accepted author version: https://bear-wangsx.github.io/files/publications/2024/%5BWang%202024%20TSP%5D%20Robust%20Waveform%20Design%20for%20ISAC.pdf  
Evidence: **A — accepted manuscript and selected figure pages inspected.** The accessible copy identifies itself as an accepted author version, not the final typeset version.

**Useful figure families observed**
- Conceptual Pareto frontier for two competing performance objectives (Fig. 1).
- Nominal versus uncertain performance-frontier illustrations (Fig. 2).
- Objective-function landscape with upper/lower bounds (Fig. 3).
- Real-world-style system scenario and map/satellite panels (Fig. 4).
- Beam-pattern comparisons (Fig. 5).
- Multi-panel box plots showing distributions under different design settings (Fig. 6).

**Transferable lessons**
- Conceptual plots should label the meaning of the axes, ideal point, frontier, and operating extremes.
- Use separate panels for different operating conditions while preserving comparable scales.
- Box plots are useful when the result is a distribution over repeated trials, not a single deterministic value.
- Keep nominal estimates visually distinct from measured or simulated distributions.

### 4. Robotics and multi-agent systems

**Pierre-Yves Lajoie and Giovanni Beltrame, “Swarm-SLAM: Sparse Decentralized Collaborative Simultaneous Localization and Mapping Framework for Multi-Robot Systems.”**  
IEEE Robotics and Automation Letters, vol. 9, no. 1, pp. 475–482, 2024.  
DOI: https://doi.org/10.1109/LRA.2023.3333742  
IEEE record: https://ieeexplore.ieee.org/document/10321649/  
Accessible author preprint: https://arxiv.org/pdf/2301.06230.pdf  
Project documentation: https://lajoiepy.github.io/cslam_documentation/html/index.html  
Evidence: **A — author preprint and figure pages inspected.** The paper's IEEE publication record was cross-checked; the inspected PDF is the arXiv author version.

**Useful figure families observed**
- Repeated multi-robot system architecture with external sensors, front-end processing, back-end optimization, and communication interfaces (Fig. 1).
- Multi-robot pose-graph/trajectory visualization comparing candidate-selection strategies (Fig. 2).
- Tables comparing supported sensors and system properties.

**Transferable lessons**
- Repeat a common visual grammar for each robot/agent so readers can compare peers.
- Distinguish local processing from inter-agent communication and global optimization.
- For spatial results, show trajectories or pose graphs in a spatial coordinate frame rather than replacing them with generic bar charts.
- A system overview and a spatial-results figure answer different questions and should remain separate.

### 5. Remote sensing and multimodal segmentation

**Zhenghang Yuan et al., “RRSIS: Referring Remote Sensing Image Segmentation.”**  
IEEE Transactions on Geoscience and Remote Sensing, vol. 62, 2024.  
DOI: https://doi.org/10.1109/TGRS.2024.3369720  
IEEE record: https://ieeexplore.ieee.org/document/10458079/  
Author's institutional thesis containing the published article in an appendix: https://mediatum.ub.tum.de/doc/1776138/document.pdf  
Evidence: **A — article text and figure captions inspected in the institutional thesis appendix.** The inspected source is a thesis-hosted copy of the IEEE article, not the publisher's typeset PDF.

**Useful figure families observed**
- Qualitative examples pairing an image with a referring expression and target region/mask.
- Overall vision-language segmentation architecture (Fig. 4 of the article).
- Dataset examples and segmentation outputs.
- Comparative visual results for small, scattered, and spatially described targets.

**Transferable lessons**
- For multimodal tasks, show each input modality explicitly before the fusion stage.
- Keep image, language, feature-fusion, and mask-generation stages distinct.
- Qualitative examples need consistent image crops, mask overlays, and readable text prompts.
- Map-like and image-like results require scale, orientation, and spatial context when relevant.

### 6. Antennas and electromagnetics

**Asif Khan, Yejun He, and Zhi Ning Chen, “A Dual-Band Quad-Port Circularly Polarized MIMO Antenna Based on a Modified Jerusalem-Cross Absorber for Wireless Communication Systems.”**  
IEEE Transactions on Antennas and Propagation, vol. 72, no. 1, 2024.  
DOI: https://doi.org/10.1109/TAP.2023.3326285  
Accessible author-hosted paper: https://ceie.szu.edu.cn/heyejun/paper/TAPAsif1.pdf  
Evidence: **A — full author-hosted paper and figure descriptions inspected.** The publisher's copyright statement applies; the repository contains only analysis notes, not the PDF or figures.

**Useful figure families observed**
- Dimensioned antenna geometry (Fig. 1).
- Design-evolution panels combined with reflection-coefficient and axial-ratio plots (Fig. 2).
- Multi-panel array geometry at different element-rotation angles (Fig. 3).
- Four-panel S-parameter comparisons (Fig. 4).
- Multi-panel mutual-coupling plots (Fig. 5).
- Parametric spacing comparisons (Fig. 6).
- Absorber unit-cell evolution and equivalent-circuit discussion (Fig. 7 onward).

**Transferable lessons**
- Keep dimensioned geometry separate from frequency-response evidence unless the comparison is the message.
- In dense multi-series plots, use both color and line style; maintain a consistent legend across panels.
- Label frequency units, S-parameter notation, polarization, and measurement/simulation identity.
- Use consistent views and scales when comparing geometric iterations.

---

## B. Additional IEEE papers for wider coverage

The following papers broaden the bibliography. They are useful candidate references, but the evidence level is not sufficient to claim detailed visual-style inspection.

### 7. Medical image computing

**Enjun Zhu et al., “MP-Net: A Multi-Center Privacy-Preserving Network for Medical Image Segmentation.”**  
IEEE Transactions on Medical Imaging, vol. 43, no. 7, pp. 2718–2729, 2024.  
DOI: https://doi.org/10.1109/TMI.2024.3377248  
IEEE record: https://ieeexplore.ieee.org/document/10472537/  
PubMed record: https://pubmed.ncbi.nlm.nih.gov/38478456/  
Evidence: **C — metadata and abstract only.** The abstract describes encryption, segmentation, and decryption networks evaluated on cardiac MRI and CTPA datasets. No detailed figure-style claims are made here.

### 8. Functional ultrasound and biomedical signal analysis

**Aybuke Erol et al., “Evoked Component Analysis (ECA): Decomposing the Functional Ultrasound Signal with GLM-Regularization.”**  
IEEE Transactions on Biomedical Engineering, vol. 71, no. 10, pp. 2823–2832, 2024.  
DOI: https://doi.org/10.1109/TBME.2024.3395154  
Institutional record: https://research.tudelft.nl/en/publications/evoked-component-analysis-eca-decomposing-the-functional-ultrasou/  
Evidence: **C — abstract and bibliographic record inspected; full-text file retrieval was unavailable in this review.** This paper is a useful candidate for functional-imaging, spatial/temporal factorization, and statistical-result figures, but no figure style is asserted.

### 9. AI and edge computing

**Joanna Komorniczak et al., “Certainty-Based Neural Network Architecture Selection Framework for TinyML Systems.”**  
IEEE Access, vol. 12, pp. 155632–155643, 2024.  
DOI: https://doi.org/10.1109/ACCESS.2024.3482111  
IEEE record: https://ieeexplore.ieee.org/document/10719985/  
Evidence: **C — IEEE metadata, abstract, and a publisher-generated figure summary inspected.** The paper studies the trade-off between inference time and recognition quality while selecting among neural-network architectures. Treat model-selection and time-varying performance figures as candidate figure families, not as detailed visual observations.

### 10. Industrial automation and robotics

**Alessandro Bozzi et al., “A Platoon-Based Approach for AGV Scheduling and Trajectory Planning in Fully Automated Production Systems.”**  
IEEE Transactions on Industrial Informatics, vol. 21, no. 1, pp. 594–603, 2025.  
DOI: https://doi.org/10.1109/TII.2024.3455413  
IEEE record: https://ieeexplore.ieee.org/document/10716253/  
Evidence: **C — IEEE metadata and abstract inspected; IEEE Xplore identifies a Creative Commons license, but the full paper figures were not inspected here.** The paper is a candidate reference for factory layouts, vehicle scheduling, trajectories, and resource-allocation workflows.

### 11. Power electronics and predictive control

**Wenjie Wu et al., “Data-Enabled Finite State Predictive Control for Power Converters via Adaline Neural Network.”**  
IEEE Transactions on Industrial Electronics, vol. 72, no. 3, pp. 2244–2253, 2025.  
DOI: https://doi.org/10.1109/TIE.2024.3413837  
IEEE record: https://ieeexplore.ieee.org/document/10643335/  
Evidence: **C — metadata and abstract inspected.** Candidate figure families include converter topology, predictive-control flow, and simulation/experimental comparisons. No detailed figure-style claim is made.

### 12. Metasurface antennas and automated electromagnetic design

**Lucia Teodorani et al., “Generalized Deterministic Automated Design of Metasurface Antennas With 3-D Feeding Structures.”**  
IEEE Transactions on Antennas and Propagation, vol. 72, no. 11, pp. 8135–8150, 2024.  
DOI: https://doi.org/10.1109/TAP.2024.3457149  
IEEE record: https://ieeexplore.ieee.org/document/10684076/  
Evidence: **C — IEEE metadata and abstract inspected.** IEEE Xplore identifies a Creative Commons license. Candidate figure families include metasurface geometry, 3-D feeding structures, current/field distributions, and design optimization.

### 13. Remote-sensing network architecture

**“Hierarchical Shared Architecture Search for Real-Time Semantic Segmentation of Remote Sensing Images.”**  
IEEE Transactions on Geoscience and Remote Sensing, vol. 62, 2024.  
DOI: https://doi.org/10.1109/TGRS.2024.3373493  
IEEE record: https://ieeexplore.ieee.org/document/10460490/  
Evidence: **C — metadata and abstract inspected.** The abstract identifies a lightweight backbone and multiscale feature-fusion module. This is a candidate for neural-network architecture and segmentation-evaluation figure examples.

---

## C. Cross-domain figure lessons

The full-text cases demonstrate that research figures differ by scientific question:

| Research domain | Figure families especially useful for learning |
|---|---|
| Biomedical sensing | Device photos, sensor geometry, equivalent circuits, system architecture, frequency-response plots |
| Power and control | Electrical/system topology, communication graphs, state machines, sequence diagrams |
| Signal processing | Mathematical concept plots, Pareto frontiers, beam patterns, box plots, scenario maps |
| Robotics | Repeated agent architecture, sensor fusion, pose graphs, trajectories, spatial comparisons |
| Remote sensing | Image/text pairs, segmentation masks, model architecture, qualitative spatial results |
| Antennas and EM | Dimensioned geometry, design iterations, S-parameter plots, radiation patterns, field/current maps |
| AI/ML | Model architecture, data pipeline, model selection, ablation and metric comparisons |
| Industrial automation | Factory layout, resource scheduling, trajectory and process-flow diagrams |

The main design conclusion is not that all these fields share one color palette or one diagram style. They share higher-level quality requirements—correctness, clarity, readable labels, consistent encoding, accessibility, and venue-compliant export—while the scientific visual grammar remains task-specific.

## D. Source and copyright policy

- Use papers to learn visual structure and figure conventions, not to copy their artwork.
- Do not upload the source PDFs or complete publisher figures to this public repository.
- Recreate only original diagrams and templates; do not trace a paper figure and present it as original.
- Label the manuscript version and evidence level when a publisher PDF is not available.
- A Creative Commons label does not automatically mean every third-party image inside a paper can be reused. Check the specific credit line and license.
