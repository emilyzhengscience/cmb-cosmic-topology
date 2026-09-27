# How the Universe Got Its Spots

## Exploring Cosmic Topology with the Cosmic Microwave Background

**Student:** Emily Zheng  
**Project Type:** Computational Physics / Cosmology  
**Duration:** 4 weeks

---

## Project Overview

Is the universe infinite, or could it be finite but so large that we cannot easily detect its global structure?

This project explores whether the **Cosmic Microwave Background (CMB)** can contain information about the global shape, or **topology**, of the universe.

The project is inspired by Janna Levin's *How the Universe Got Its Spots* and research on cosmic topology and CMB temperature correlations.

The central idea is that a universe can be **locally flat but globally finite**. If space has a finite topology, light may effectively encounter repeated regions of space, potentially producing characteristic correlations in the CMB.

Using public CMB data, numerical simulations, statistical analysis, and a simple machine-learning experiment, this project investigates how such signatures might be detected.

---

## Research Question

> **Can statistical patterns in CMB temperature fluctuations distinguish a standard cosmological model from simplified models representing a finite, periodic universe?**

A secondary question is:

> **As the characteristic size of a finite universe increases, when does its CMB pattern become difficult to distinguish from that of an effectively infinite universe?**

---

## Background

The Cosmic Microwave Background is radiation originating from the early universe, approximately 380,000 years after the Big Bang.

Its temperature is extremely uniform, but small fluctuations occur across the sky:

$$T(\theta,\phi)=T_0+\Delta T(\theta,\phi)$$

with approximately

$$\frac{\Delta T}{T}\sim10^{-5}$$

These tiny temperature variations form the familiar hot and cold "spots" in CMB maps.

They contain information about the physical conditions and structure of the early universe.

### CMB and Spherical Harmonics

Because the CMB is observed across the celestial sphere, its temperature fluctuations can be represented using spherical harmonics:

$$\frac{\Delta T}{T}(\theta,\phi)=\sum_{\ell,m}a_{\ell m}Y_{\ell m}(\theta,\phi)$$

The angular power spectrum is

$$C_\ell=\frac{1}{2\ell+1}\sum_m |a_{\ell m}|^2$$

The values of $C_\ell$ describe how much temperature variation exists at different angular scales.

---

## Geometry vs. Topology

An important idea in this project is that **geometry and topology are different**.

Ordinary infinite Euclidean space can be represented as

$$\mathbb{R}^3$$

But it is also possible to construct a finite space that is locally flat by identifying periodically separated points:

$$(x,y,z)\sim(x+n_xL,\;y+n_yL,\;z+n_zL)$$

where $n_x$, $n_y$, and $n_z$ are integers and $L$ represents the characteristic size of the finite space.

This produces a simplified three-dimensional torus-like topology.

Locally, such a universe can still appear flat.

Globally, however, it is finite.

Therefore,

$$\text{local geometry}\neq\text{global topology}$$

If the universe has this type of topology, periodicity could produce additional correlations between apparently different regions of the CMB sky.

---

## Hypothesis

If the universe has a finite topology with a characteristic size comparable to the observable region, periodicity should introduce additional correlations into simulated CMB temperature patterns.

Therefore, simplified finite-universe simulations should be statistically distinguishable from ordinary CMB-like simulations when the topology scale is sufficiently small.

As the size of the finite space increases, these signatures should weaken.

Eventually, the observable region should contain too little information to distinguish a very large finite universe from an infinite universe.

---

# Project Method

The project contains three main components.

## 1. Explore Real CMB Data

Publicly available CMB data from the **Planck mission** will be used to study the temperature fluctuations of the real sky.

Python will be used to:

- load and visualize a CMB temperature map;
- examine hot and cold temperature fluctuations;
- study the angular power spectrum;
- calculate or examine large-angle correlations.

This provides an observational connection between the theoretical problem and the actual universe.

---

## 2. Simulate Finite and Infinite Universes

Python will be used to generate simplified CMB-like random temperature fields.

Two classes of simulations will be compared.

### Standard Model

A random CMB-like field representing an effectively infinite universe.

### Finite Periodic Model

A field generated with periodic boundary conditions representing a simplified finite topology.

Several characteristic topology sizes $L$ will be investigated.

For example:

$$L/D=0.5,\;0.75,\;1.0,\;1.5,\;2.0$$

where $D$ represents an observational scale used in the simulation.

For each simulation, statistical properties will be measured.

One useful quantity is the angular correlation function:

$$C(\theta)=\left\langle\Delta T(\hat n_1)\Delta T(\hat n_2)\right\rangle$$

where

$$\hat n_1\cdot\hat n_2=\cos\theta$$

The correlation functions and power spectra of the different simulated universes will then be compared.

---

## 3. Machine-Learning Experiment

A simple machine-learning classifier will be trained to determine whether statistical information from a simulated CMB map came from:

$$0=\text{standard model}$$

or

$$1=\text{finite periodic model}$$

Possible input features include low-order power-spectrum values,

$$C_2,C_3,\ldots,C_{20}$$

together with selected correlation statistics.

The project will begin with an interpretable classifier such as:

- logistic regression;
- random forest.

A large neural network is not required.

The main result will be a graph showing

$$\text{classification accuracy versus finite-universe scale }L/D$$

If the finite universe becomes sufficiently large, its observable properties should increasingly resemble those of the standard model.

The classification accuracy should therefore approach random guessing:

$$P(\mathrm{correct})\rightarrow0.5$$

---

# Four-Week Plan

## Week 1 — CMB Physics and Real Data

Learn the basic physics of:

- the Cosmic Microwave Background;
- temperature anisotropies;
- spherical harmonics;
- angular power spectra;
- geometry versus topology;
- finite and infinite cosmological models.

Download or access public Planck CMB data.

Create Python code to visualize the CMB and examine its basic statistical properties.

**Goal:** Produce the first real-CMB plots and understand what the CMB spots represent physically.

---

## Week 2 — Finite-Space Simulation

Develop a simplified CMB-like random-field simulation.

Introduce periodic boundary conditions representing a finite space.

Generate simulations for several values of $L/D$.

Calculate correlation functions and compare the resulting patterns.

**Goal:** Demonstrate computationally that topology can change observable statistical correlations.

---

## Week 3 — Statistical Analysis and Machine Learning

Generate a larger collection of simulated universes.

Extract numerical features such as

$$C_2,C_3,\ldots,C_{20}$$

and selected correlation statistics.

Train a simple classifier to distinguish standard simulations from finite-topology simulations.

Measure classification performance for different values of $L/D$.

**Goal:** Determine when the topology becomes difficult to detect.

---

## Week 4 — Interpretation and Final Report

Compare the simulated results with selected properties of the real Planck CMB.

Analyze:

- what the simulations demonstrate;
- what the machine-learning model detects;
- how detectability changes with topology scale;
- what conclusions cannot be drawn from this simplified experiment.

Prepare the final figures, report, presentation, and GitHub documentation.

**Goal:** Produce a reproducible computational physics project with clearly stated conclusions and limitations.

---

# Expected Results

For relatively small periodic spaces, the finite-topology simulations are expected to contain stronger recognizable correlations.

The classifier should therefore distinguish the two simulated models better than random guessing:

$$P(\mathrm{correct})>0.5$$

As $L$ increases, the finite topology should become increasingly difficult to observe.

Conceptually,

$$L\rightarrow\infty$$

should make the finite model observationally approach the effectively infinite model.

The project therefore investigates an important scientific limitation:

> **A universe can be finite even if the observable universe does not contain enough information for us to detect its global topology.**

---

# Scope and Limitations

This project does **not** attempt to prove whether the real universe is finite or infinite.

A rigorous observational search for cosmic topology requires advanced treatment of:

- cosmological parameter estimation;
- foreground contamination;
- instrumental effects;
- sky masks;
- full-sky statistics;
- topology-specific CMB simulations;
- observational selection effects.

Instead, this project addresses a smaller and testable question:

> **Can a simplified computational experiment demonstrate how finite topology could create detectable statistical information in CMB-like patterns, and how that information becomes harder to detect as the topology scale increases?**

The Planck data provide a connection to the real universe, but the machine-learning classifier will not be interpreted as proof of the topology of the actual universe.

---

# Tools

The project will primarily use:

- Python
- Jupyter Notebook
- NumPy
- SciPy
- Matplotlib
- Healpy / HEALPix
- scikit-learn
- public Planck CMB data
- Git / GitHub

---

# Repository Structure

```text
cmb-cosmic-topology/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│   └── README.md
│
├── notebooks/
│   ├── 01_real_CMB.ipynb
│   ├── 02_finite_space_simulation.ipynb
│   ├── 03_correlation_analysis.ipynb
│   └── 04_ML_classifier.ipynb
│
├── src/
│   ├── simulation.py
│   ├── correlations.py
│   └── features.py
│
├── figures/
│
└── docs/
    └── project_proposal.md
```

Large Planck data files will not be committed directly to the repository. Instructions for obtaining the public data will be provided in `data/README.md`.

---

# Project Goals

By the end of the project, the goal is to be able to explain the chain

$$\text{cosmic topology}\rightarrow\text{allowed spatial patterns}\rightarrow\text{CMB correlations}\rightarrow\text{observable signatures}$$

and demonstrate this relationship computationally.

The project combines **physics, mathematics, astronomical data, numerical simulation, and machine learning** to explore a fundamental question:

> **What can the oldest light in the universe tell us about the shape of space itself?**

---

## References

1. Levin, J. *How the Universe Got Its Spots: Diary of a Finite Time in a Finite Space*. Anchor Books.

2. Levin, J., Scannapieco, E., de Gasperis, G., Silk, J., & Barrow, J. D. "How the Universe Got Its Spots." *Physical Review D* **58**, 123006.

3. Levin, J. "Topology and the Cosmic Microwave Background." *Physics Reports* **365**, 251–333.

4. Planck Collaboration. Planck mission cosmological results and public CMB data products, European Space Agency.

---

## License

This project is released under the **MIT License**.

---

*This is a student computational research project. The simulations are intentionally simplified and should not be interpreted as a professional observational constraint on the topology of the universe.*
