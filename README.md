# Finding Patterns in the Cosmic Microwave Background

## A Simple Data Analysis Inspired by Janna Levin

**Student:** Emily Zheng  
**Project Type:** Physics / Data Analysis / Machine Learning  
**Duration:** About 4 weeks

---

## Project Idea

The Cosmic Microwave Background (CMB) is the oldest light we can observe in the universe.

CMB maps contain tiny temperature variations that appear as hot and cold spots across the sky.

Janna Levin and collaborators studied whether the **spatial relationships between these spots** could contain information about the structure and topology of the universe.

The full theory of cosmic topology is beyond the scope of this project.

Instead, this project asks a much simpler question:

> **Does the real CMB contain measurable spatial patterns that are different from a randomized CMB map?**

We will investigate this question using public Planck CMB data, simple statistics, and a small machine-learning experiment.

---

# Main Idea

Suppose we take the real CMB temperature map and randomly move its temperature values to different locations.

The real and randomized maps will still contain exactly the same temperature values.

Therefore, they will have approximately the same:

- mean;
- standard deviation;
- temperature distribution;
- histogram.

But the randomized map will no longer have the original spatial arrangement.

This gives us a simple experiment:

```text
Real CMB
same temperature values
real spatial arrangement

        vs.

Randomized CMB
same temperature values
random spatial arrangement
```

If the two maps behave differently, the difference must come from their **spatial arrangement**, not from their overall temperature distribution.

---

# Research Question

> **Does the spatial arrangement of CMB temperature fluctuations contain measurable information?**

More specifically:

> **Are neighboring temperatures in the real CMB more structured than we would expect if the same temperature values were randomly arranged?**

---

# Hypothesis

If the real CMB contains spatial structure, nearby temperature measurements should show relationships that disappear when the temperature locations are randomized.

Therefore:

> **Neighboring temperatures in the real CMB should show different similarity from neighboring temperatures in randomized CMB maps.**

---

# Data

The project will use public CMB temperature data from the **Planck mission**.

A CMB map contains temperature measurements across the sky.

Large Planck data files will not be stored directly in this repository.

---

# Experiment 1 — Explore the CMB

First, we will load and visualize the real Planck CMB data.

We will calculate simple statistics such as:

- mean;
- standard deviation;
- minimum and maximum;
- temperature histogram.

### Output

**Figure 1:** Real Planck CMB map

**Figure 2:** CMB temperature histogram

The purpose of this step is simply to understand the data.

---

# Experiment 2 — Real vs. Randomized CMB

Next, we will randomly shuffle the locations of the CMB temperature values.

For example:

```text
Real:

Location A → 12
Location B → -5
Location C → 8


Randomized:

Location A → 8
Location B → 12
Location C → -5
```

The temperature values have not changed.

Only their locations have changed.

We will verify that the real and randomized maps still have the same temperature histogram.

Then we will measure how similar neighboring temperatures are.

The exact similarity statistic will be kept simple and clearly defined in the analysis.

We will calculate:

```text
neighbor similarity of real CMB
```

and compare it with:

```text
neighbor similarity of randomized CMB
```

---

# Randomization Test

One randomized map could produce an unusual result simply by chance.

Therefore, we will repeat the randomization many times.

For example:

```text
Randomization 1   → similarity S1
Randomization 2   → similarity S2
Randomization 3   → similarity S3
...
Randomization 100 → similarity S100
```

This produces a distribution showing what we would expect from randomly arranged temperature values.

We can then compare the real CMB result with this random distribution.

### Output

**Figure 3:** Real CMB vs. randomized CMB

**Figure 4:** Distribution of neighbor similarity from randomized maps, with the real CMB result marked on the same graph

This is the main experiment of the project.

---

# Experiment 3 — Simple Machine Learning

As a small extension, we will test whether a simple machine-learning model can recognize information contained in spatial relationships.

We will use a simple model such as:

**Logistic Regression**

The model will try to distinguish data from:

```text
1 = real CMB spatial arrangement
0 = randomized spatial arrangement
```

We will compare two versions of the model.

### Model A — Basic Statistics

Use features such as:

```text
mean
standard deviation
```

### Model B — Add Spatial Information

Use:

```text
mean
standard deviation
neighbor similarity
```

We will compare the classification accuracy of the two models.

If adding neighbor similarity improves classification, this provides another way to show that spatial arrangement contains information.

### Output

**Figure 5:** Machine-learning accuracy with and without the spatial feature

---

# Four-Week Plan

## Week 1

Learn what the CMB is.

Download and load the Planck data.

Display the CMB map and calculate basic statistics.

---

## Week 2

Create randomized CMB maps.

Define and calculate neighbor similarity.

Repeat the randomization many times.

Compare the real CMB with the randomized results.

---

## Week 3

Create a small machine-learning dataset.

Train a Logistic Regression model.

Compare classification with and without spatial information.

---

## Week 4

Create final figures.

Interpret the results.

Write the project report.

---

# Expected Results

We expect the real and randomized CMB maps to have the same overall temperature distribution because they contain the same temperature values.

However, their spatial relationships may be different.

If the real CMB neighbor-similarity value is unusual compared with randomized maps, this would show that:

> **The arrangement of CMB temperatures contains information that cannot be seen from the temperature histogram alone.**

If adding spatial information also improves machine-learning classification, it would provide a second demonstration of the same idea.

---

# What Would a Negative Result Mean?

The expected result may not occur.

If the selected neighbor-similarity measurement does not distinguish the real CMB from randomized maps, that is still a valid result.

It would mean that this particular measurement did not detect spatial structure in the data.

It would **not** disprove Janna Levin's research or show that the universe has no nontrivial topology.

---

# Connection to Janna Levin's Work

Janna Levin and collaborators investigated a much deeper question:

> Could spatial correlations in the CMB contain information about the global topology of the universe?

This project does **not** attempt to answer that question directly.

Instead, it investigates a simpler idea underlying that research:

> **Does spatial arrangement itself contain measurable information in the CMB?**

This allows us to explore an idea motivated by modern cosmology without requiring advanced mathematics or a theoretical model of cosmic topology.

---

# Tools

- Python
- Jupyter Notebook
- NumPy
- Matplotlib
- Healpy
- scikit-learn
- Planck public CMB data

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
│   ├── 01_view_CMB.ipynb
│   ├── 02_real_vs_random.ipynb
│   └── 03_simple_ML.ipynb
│
├── figures/
│
└── docs/
    └── project_report.md
```

---

# Final Goal

The project should be able to answer one clear question:

> **What information disappears when we keep the CMB temperatures but destroy their spatial arrangement?**

The goal is not to prove a theory about the shape of the universe.

The goal is to use real astronomical data to understand why **spatial patterns and correlations matter** when scientists study the CMB.

---

## References

1. Levin, J., Scannapieco, E., de Gasperis, G., Silk, J., & Barrow, J. D.  
   **"How the Universe Got Its Spots."**  
   *Physical Review D*, 58, 123006 (1998).

2. Levin, J.  
   **"Topology and the Cosmic Microwave Background."**  
   *Physics Reports*, 365, 251–333 (2002).

3. Levin, J.  
   *How the Universe Got Its Spots: Diary of a Finite Time in a Finite Space.*

4. Planck Collaboration.  
   Planck mission CMB data products.

---

*This is a student data-analysis project inspired by research on CMB spatial correlations. It does not attempt to determine the topology of the universe.*
