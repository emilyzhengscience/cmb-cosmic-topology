"""Week 1: Inspect real Planck CMB temperature data."""
import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
from cmb_utils import load_cmb, save_figure

cmb, valid = load_cmb()
t = cmb[valid]
print('Valid pixels:', len(t))
print('Mean:', np.mean(t))
print('Standard deviation:', np.std(t))
print('Minimum / maximum:', np.min(t), np.max(t))
print('Check the FITS product documentation for temperature units.')

hp.mollview(cmb, title='Planck CMB temperature fluctuations (masked)', unit='FITS map units')
save_figure('01_planck_map.png')
plt.close('all')

plt.figure(figsize=(7, 4))
plt.hist(t, bins=60, edgecolor='white')
plt.xlabel('Temperature fluctuation (FITS map units)')
plt.ylabel('Number of pixels')
plt.title('Distribution of Planck CMB temperature fluctuations')
save_figure('02_temperature_histogram.png')
plt.close('all')
