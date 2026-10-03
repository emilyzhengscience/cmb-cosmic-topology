# Finding Patterns in the Cosmic Microwave Background

**Student:** Emily Zheng  
**Scope:** One Planck map, one randomization test, one optional logistic-regression extension.

**Research question:** Are neighboring CMB temperatures more structured than expected if the same observed temperatures were randomly rearranged?

Inspired by Janna Levin and collaborators' work on CMB spatial correlations. This is **not** a test of whether the universe is finite.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Follow `data/README.md` to obtain a real Planck FITS map and preferably a matching foreground/confidence mask.

```bash
python 01_view_cmb.py
python 02_compare_random.py
python 03_machine_learning.py  # optional
```

Results are saved in `figures/`.

## What each file does

- `01_view_cmb.py`: view the map and histogram.
- `02_compare_random.py`: shuffle only unmasked pixels 100 times and compare a neighbor-similarity statistic. The permutation test has a minimum attainable one-sided p-value of 1/101.
- `03_machine_learning.py`: optional Logistic Regression, using **non-overlapping sky regions** and a region-level train/test split. Mean and SD are identical for the paired real/shuffled regions by design; the spatial feature is expected to carry the signal. ML accuracy is a demonstration of this feature, not independent cosmological evidence.
- `cmb_utils.py`: shared FITS loading, masking, neighboring-pixel pairs, and plotting.

## Interpretation cautions

A raw HEALPix neighbor score depends on angular resolution and smoothing. Shuffle tests deliberately destroy angular structure; detecting that difference does **not** test a particular cosmic topology. Planck noise, foregrounds, masks, and sky-region dependence can affect results. Report the exact map product, mask, units, NSIDE, and analysis settings.

**Reference:** Levin et al., *How the Universe Got Its Spots*, Physical Review D 58, 123006 (1998).
