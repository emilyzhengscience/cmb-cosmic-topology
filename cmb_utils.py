"""Small, shared helpers for Emily's CMB data-analysis project."""
from pathlib import Path
import numpy as np
import healpy as hp

DATA = Path(__file__).resolve().parent / 'data' / 'planck_cmb.fits'
FIGURES = Path(__file__).resolve().parent / 'figures'
NSIDE = 64  # Keep calculations manageable on a laptop.


def load_cmb(path=DATA, target_nside=NSIDE):
    """Read a Planck HEALPix temperature map; retain valid pixels only.

    IMPORTANT: Check the FITS column and unit of the downloaded product.
    Optionally put a matching Planck mask in data/planck_mask.fits.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f'Missing {path}. See data/README.md')
    raw = np.asarray(hp.read_map(str(path), field=0, dtype=np.float64), dtype=float)
    original_nside = hp.get_nside(raw)
    valid = np.isfinite(raw) & (raw != hp.UNSEEN) & (np.abs(raw) < 1e20)
    mask_file = path.parent / 'planck_mask.fits'
    if mask_file.exists():
        mask = np.asarray(hp.read_map(str(mask_file), field=0), dtype=float)
        if hp.get_nside(mask) != original_nside:
            raise ValueError('CMB map and mask must have matching NSIDE')
        valid &= np.isfinite(mask) & (mask > 0.9)
    # Degrade using a weighted average, so invalid pixels cannot pollute results.
    if original_nside != target_nside:
        weight = hp.ud_grade(valid.astype(float), target_nside, power=0)
        total = hp.ud_grade(np.where(valid, raw, 0.0), target_nside, power=0)
        valid = weight > 0.95
        raw = np.divide(total, weight, out=np.zeros_like(total), where=weight > 0)
    raw[~valid] = hp.UNSEEN
    return raw, valid


def neighbor_pairs(nside, valid):
    """Unique HEALPix adjacent pixel pairs; masked pixels are excluded."""
    neighbors = hp.get_all_neighbours(nside, np.arange(len(valid)))
    left = np.broadcast_to(np.arange(len(valid)), neighbors.shape)
    good = neighbors >= 0
    a, b = left[good], neighbors[good]
    keep = (a < b) & valid[a] & valid[b]
    return a[keep], b[keep]


def neighbor_score(values, pairs):
    """Dimensionless neighbor covariance / pixel variance; higher means smoother."""
    a, b = pairs
    if len(a) == 0:
        return np.nan
    valid = np.isfinite(values) & (values != hp.UNSEEN)
    centered = values[valid] - np.mean(values[valid])
    variance = np.mean(centered ** 2)
    if variance < 1e-30:
        return np.nan
    mean = np.mean(values[valid])
    return float(np.mean((values[a] - mean) * (values[b] - mean)) / variance)


def save_figure(name):
    import matplotlib.pyplot as plt
    FIGURES.mkdir(exist_ok=True)
    path = FIGURES / name
    plt.savefig(path, dpi=160, bbox_inches='tight')
    print('Saved:', path)
