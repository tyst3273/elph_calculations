import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'electrons_out.hdf5'

with h5py.File(input_file,'r') as db:
        fermi_surface = db['fermi_surface'][...]
        if not 'kpts_mesh' in db.keys():
            exit('do calculation on mesh instead')
        kpts_mesh = db['kpts_mesh'][...]

shape = fermi_surface.shape
num_kpts = shape[0]
num_bands = shape[1]
num_spin = shape[2]

fermi_surface = fermi_surface.sum(axis=(1,2))
fermi_surface.shape = kpts_mesh

fig, ax = plt.subplots(figsize=(6,6))

vmax = fermi_surface.max()*0.1
extent = [0,1,0,1]
ax.imshow(fermi_surface,cmap='Greys',vmin=0,vmax=vmax,aspect='auto',origin='lower',
    interpolation='none',extent=extent)

ax.set_title(input_file)
plt.show()


