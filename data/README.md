# Data setup

1. Obtain a public Planck component-separated CMB temperature HEALPix FITS map (e.g., SMICA) from https://pla.esac.esa.int/ .

If you are at project root, go to 'data' first by:
cd data

#download the data, it is about 384M.
wget -c \
https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb/COM_CMB_IQU-smica-nosz_2048_R3.00_full.fits \
-O planck_cmb.fits


2. Read the product's documentation. Confirm that **field 0 is the CMB temperature** and record its units. Some Planck FITS products have multiple fields, and not every product uses the same temperature units.
3. Rename/copy the map to `data/planck_cmb.fits`.
4. Recommended: obtain a compatible Planck confidence/foreground mask at the **same original NSIDE and pixel ordering**, with values 0 (masked) to 1 (unmasked), and save it as `data/planck_mask.fits`. The loader keeps mask values > 0.9. If no mask is supplied, the project cannot adequately exclude foreground-contaminated regions; treat results as illustrative.
5. The scripts degrade maps to NSIDE 64 for speed, preserving the mask as far as possible. Check product ordering (RING/NESTED) and confirm the FITS file is read correctly.
