import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

import matplotlib as mpl

mpl.rc('text', usetex=True)
mpl.rcParams['text.latex.preamble'] = r"\usepackage{bm}"

fig, ax = plt.subplots(figsize=(6,6))

input_file = 'neutrons.hdf5'

args = sys.argv
if len(args) > 1:
    input_file = sys.argv[1]

with h5py.File(input_file,'r') as db:
    form_factors = db['form_factors'][...]
    structure_factors = db['structure_factors'][...]
    sqw = db['dynamic_structure_factors'][...] 
    energy = db['neutron_energy_transfer'][...]
    freqs = db['frequencies'][...]
    num_qpts = db['num_qpts'][...]
    if 'qpts_distances' in db.keys():
        qpts_dist = db['qpts_distances'][...]
        qpts_verts = db['qpts_vert_distances'][...]
        qpts_path = db['qpts_path'][...]

num_modes = freqs.shape[1]
num_qpts = freqs.shape[0]
freqs = freqs.squeeze()

sqw = sqw.sum(axis=1)
sqw /= sqw.max()

qpts = np.arange(num_qpts)

qpts_verts /= qpts_dist.max()
qpts_dist /= qpts_dist.max()

vmax = 2.5e-4 #0.025 #1.0
extent = [0,1,energy.min(),energy.max()]
ax.imshow(sqw.T,cmap='hot',vmin=0,vmax=vmax,aspect='auto',origin='lower',
            interpolation='none',extent=extent)
    
for ii in range(num_modes):
    ax.plot(qpts_dist,freqs[:,ii],marker='o',ms=0,c='g',lw=1,ls=(0,(2,1))) 

for v in qpts_verts:
    ax.plot([v,v],[0,energy.max()],ms=0,c=(0.5,0.5,0.5),lw=1,ls='--')

#ax[0].axis([0,1,0,2.5])
ax.set_ylim([0,freqs.max()*1.1])
ax.set_xticks(qpts_verts)

ticks = []
for ii in range(qpts_verts.size):
    vert = qpts_path[ii]
    Q = f'({vert[0]:g},{vert[1]:g})'
    ticks.append(Q)

ax.set_xticklabels(ticks)
ax.set_ylabel(r'$\omega_{\bm{q}\nu}$',fontsize='x-large',rotation='horizontal',labelpad=15)

#plt.savefig('neutrons.pdf',dpi=300,bbox_inches='tight')
plt.show()

