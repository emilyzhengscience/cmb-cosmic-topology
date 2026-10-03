"""Week 3 (optional): Logistic regression on separate, non-overlapping sky regions.

A sanity-check classifier, NOT a test of the universe's topology.
Each region contributes one real and one independently shuffled sample.
Train/test splitting happens by region, not by individual sample.
"""
import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from cmb_utils import load_cmb, save_figure

rng = np.random.default_rng(42)
cmb, valid = load_cmb()
nside = hp.get_nside(cmb)
if nside < 16:
    raise ValueError('Use NSIDE >= 16 for region-based analysis.')
# Nested HEALPix ordering makes non-overlapping parent regions easy to define.
nested = hp.reorder(cmb, r2n=True)
valid_nested = hp.reorder(valid.astype(float), r2n=True) > 0.5
parent_nside = 4
pixels_per_region = (nside // parent_nside) ** 2
n_regions = hp.nside2npix(parent_nside)


def region_features(values, region_valid, region_nside, region_pixel_ids):
    """Mean, SD, and neighboring similarity within one parent sky region."""
    # Neighbor IDs are global NESTED pixel IDs.
    all_neighbors = hp.get_all_neighbours(region_nside, region_pixel_ids, nest=True)
    a = np.broadcast_to(region_pixel_ids, all_neighbors.shape)
    ok = all_neighbors >= 0
    a, b = a[ok], all_neighbors[ok]
    # Only pairs whose two endpoints lie in this same region and are valid.
    start, stop = region_pixel_ids[0], region_pixel_ids[-1] + 1
    keep = (a < b) & (b >= start) & (b < stop)
    a, b = a[keep], b[keep]
    keep = region_valid[a - start] & region_valid[b - start]
    a, b = a[keep] - start, b[keep] - start
    t = values[region_valid]
    mean, sd = float(t.mean()), float(t.std())
    if len(a) < 20 or sd < 1e-15:
        return None
    spatial = float(np.mean((values[a] - mean) * (values[b] - mean)) / sd**2)
    return [mean, sd, spatial]

features, labels, groups = [], [], []
for region in range(n_regions):
    start = region * pixels_per_region
    ids = np.arange(start, start + pixels_per_region)
    vals = nested[ids].copy()
    good = valid_nested[ids]
    if good.sum() < 0.95 * pixels_per_region:
        continue
    real = region_features(vals, good, nside, ids)
    shuffled = vals.copy()
    shuffled[good] = rng.permutation(vals[good])
    random = region_features(shuffled, good, nside, ids)
    if real is None or random is None:
        continue
    features.extend([real, random])
    labels.extend([1, 0])
    groups.extend([region, region])

X = np.asarray(features)
y = np.asarray(labels)
groups = np.asarray(groups)
unique_groups = np.unique(groups)
if len(unique_groups) < 20:
    raise ValueError('Not enough valid sky regions. Check the Planck map and mask.')
train_groups, test_groups = train_test_split(unique_groups, test_size=0.3, random_state=42)
train = np.isin(groups, train_groups)
test = np.isin(groups, test_groups)
print('Independent training regions:', len(train_groups))
print('Independent test regions:', len(test_groups))

accuracies = []
for columns, title in [([0, 1], 'Mean + standard deviation'),
                       ([0, 1, 2], 'Mean + SD + neighbor similarity')]:
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
    model.fit(X[train][:, columns], y[train])
    prediction = model.predict(X[test][:, columns])
    accuracy = accuracy_score(y[test], prediction)
    accuracies.append(accuracy)
    print(f'{title}: accuracy = {accuracy:.3f}')

plt.figure(figsize=(7, 4))
plt.bar(['Basic statistics', 'Add spatial feature'], accuracies)
plt.axhline(0.5, linestyle='--', label='Chance baseline')
plt.ylim(0, 1)
plt.ylabel('Test accuracy (unseen sky regions)')
plt.title('Does neighboring similarity add information?')
plt.legend()
save_figure('05_ml_comparison.png')
plt.close('all')
print('NOTE: one observed sky; test regions are not independent universes.')
