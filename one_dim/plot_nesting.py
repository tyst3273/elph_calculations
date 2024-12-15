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
        band_resolved_nesting = db['nesting_function'][...]
        if 'qpts_distances' in db.keys():
            qpts_dist = db['qpts_distances'][...]
            qpts_verts = db['qpts_vert_distances'][...]
            qpts_verts /= qpts_dist.max()
            qpts_dist /= qpts_dist.max()
            one_dim = True
        else:
            qpts_mesh = db['qpts_mesh'][...]
            one_dim = False


shape = band_resolved_nesting.shape
num_qpts = shape[0]
num_bands = shape[1]

qpts = np.arange(num_qpts)


nesting = np.zeros(num_qpts)
for ii in range(num_bands):
    for jj in range(num_bands):
        nesting[:] += band_resolved_nesting[:,ii,jj]

fig, ax = plt.subplots(figsize=(6,6))

if one_dim:
    ax.plot(qpts_dist,nesting,marker='o',ms=2,lw=1,ls='-',c='m')    
    for v in qpts_verts:
        ax.plot([v,v],[0,nesting.max()],lw=1,ls=':',c=(0.5,0.5,0.5))

else:
    nesting.shape = qpts_mesh
    vmax = nesting.max()*0.5
    extent = [0,1,0,1]
    ax.imshow(nesting,cmap='magma',vmin=0,vmax=vmax,aspect='auto',origin='lower',
          interpolation='none',extent=extent)


ax.set_title(input_file)
plt.show()
