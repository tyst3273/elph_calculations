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

# sum over bands
fermi_surface = fermi_surface.sum(axis=1) 

up = fermi_surface[:,0].reshape(kpts_mesh).squeeze()
down = fermi_surface[:,1].reshape(kpts_mesh).squeeze()

fig, ax = plt.subplots(1,2,figsize=(10,4))

extent = [0,1,0,1]
vmax = max(up.max(),down.max())*0.1

ax[0].imshow(up,cmap='Reds',vmin=0,vmax=vmax,aspect='auto',origin='lower',
    interpolation='none',extent=extent)
ax[1].imshow(down,cmap='Blues',vmin=0,vmax=vmax,aspect='auto',origin='lower',
    interpolation='none',extent=extent)

fig.suptitle(input_file)
plt.show()


