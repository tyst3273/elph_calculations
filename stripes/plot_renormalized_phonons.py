import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'elph_out.hdf5'

with h5py.File(input_file,'r') as db:
        freqs = db['frequencies'][...]
        new_freqs = db['renormalized_phonon_frequencies'][...]
        fwhm = db['phonon_fwhm'][...]
        if 'qpts_distances' in db.keys():
            qpts_dist = db['qpts_distances'][...]
            qpts_verts = db['qpts_vert_distances'][...]

num_bands = freqs.shape[1]
num_qpts = freqs.shape[0]
qpts = np.arange(num_qpts)

fig, ax = plt.subplots(figsize=(6,8))

qpts_verts /= qpts_dist.max()
qpts_dist /= qpts_dist.max()

for ii in range(num_bands):

    hi = new_freqs[:,ii]+fwhm[:,ii]/2
    lo = new_freqs[:,ii]-fwhm[:,ii]/2
    ax.plot(qpts_dist,new_freqs[:,ii],marker='o',ms=0,c='g',lw=1,ls=(0,(2,1)))
    ax.plot(qpts_dist,hi,marker='o',ms=0,c='g',lw=1,ls='-')
    ax.plot(qpts_dist,lo,marker='o',ms=0,c='g',lw=1,ls='-')
    ax.fill_between(qpts_dist,lo,hi,color='g',alpha=0.5,linewidth=0)

    ax.plot(qpts_dist,freqs[:,ii],marker='o',ms=0,c='m',lw=1,ls='-')

for v in qpts_verts:
    ax.plot([v,v],[0,freqs.max()*2],ms=0,c=(0.5,0.5,0.5),lw=0.5,ls='--')

ax.set_xlabel('qpts...')
ax.set_ylabel('Energy [t]')
ax.axis([0,1,0,freqs.max()*1.1])
#ax.axis([0,1,0.16,0.22])

ax.set_title(input_file)
plt.show()
