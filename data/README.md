# Data setup

1. Obtain a public Planck component-separated CMB temperature HEALPix FITS map (e.g., SMICA) from https://pla.esac.esa.int/ .
2. Read the product's documentation. Confirm that **field 0 is the CMB temperature** and record its units. Some Planck FITS products have multiple fields, and not every product uses the same temperature units.
3. Rename/copy the map to `data/planck_cmb.fits`.
4. Recommended: obtain a compatible Planck confidence/foreground mask at the **same original NSIDE and pixel ordering**, with values 0 (masked) to 1 (unmasked), and save it as `data/planck_mask.fits`. The loader keeps mask values > 0.9. If no mask is supplied, the project cannot adequately exclude foreground-contaminated regions; treat results as illustrative.
5. The scripts degrade maps to NSIDE 64 for speed, preserving the mask as far as possible. Check product ordering (RING/NESTED) and confirm the FITS file is read correctly.

Never describe simulated/shuffled data as a second real observation. This experiment tests spatial arrangement, not Levin's topology hypothesis.
