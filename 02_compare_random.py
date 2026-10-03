"""Week 2: A simple, reproducible permutation test of spatial arrangement."""
import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
from cmb_utils import load_cmb, neighbor_pairs, neighbor_score, save_figure

N_SHUFFLES = 100
rng = np.random.default_rng(42)
cmb, valid = load_cmb()
pairs = neighbor_pairs(hp.get_nside(cmb), valid)
real_score = neighbor_score(cmb, pairs)
print('Real neighbor score:', real_score)

random_scores = []
for _ in range(N_SHUFFLES):
    shuffled = cmb.copy()
    shuffled[valid] = rng.permutation(cmb[valid])  # Keep the mask fixed.
    random_scores.append(neighbor_score(shuffled, pairs))
random_scores = np.asarray(random_scores)

# One-sided randomization p-value; direction specified before seeing results.
p_value = (1 + np.sum(random_scores >= real_score)) / (N_SHUFFLES + 1)
print('Mean randomized score:', random_scores.mean())
print('One-sided permutation p-value:', p_value)
print('Histogram exactly preserved:', np.array_equal(np.sort(cmb[valid]), np.sort(shuffled[valid])))

hp.mollview(shuffled, title='Shuffled temperatures (same values, different positions)')
save_figure('03_shuffled_map.png')
plt.close('all')

plt.figure(figsize=(7, 4))
plt.hist(random_scores, bins=20, edgecolor='white', label='Shuffled maps')
plt.axvline(real_score, linewidth=2, label='Real Planck map')
plt.xlabel('Neighbor score (higher = stronger neighboring similarity)')
plt.ylabel('Number of shuffled maps')
plt.legend()
plt.title('Permutation test: real vs. shuffled')
save_figure('04_permutation_test.png')
plt.close('all')
