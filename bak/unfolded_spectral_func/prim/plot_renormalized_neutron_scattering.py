import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

import matplotlib as mpl

mpl.rc('text', usetex=True)
mpl.rcParams['text.latex.preamble'] = r"\usepackage{bm}"

def get_specfun(energy,freqs,real,imag,adiabatic,eta):

    _shape = real.shape
    _num_qpts = _shape[1]
    _num_modes = _shape[2]

    b = np.zeros(_shape,dtype=float)

    for ii in range(_num_qpts):
        for jj in range(_num_modes):

            wq = freqs[ii,jj]
            g = imag[:,ii,jj]

            d = real[:,ii,jj]
            d0 = adiabatic[ii,jj]

            #g = 0.0
            #d = d0
            #d -= d0
            #d = 0.0

            b[:,ii,jj] = -2*wq * (2*wq*g - 2*energy*eta) / \
                    ( (energy**2 - wq**2 - 2*wq*d)**2 + (2*wq*g - 2*energy*eta)**2 )

    b = np.nan_to_num(b,nan=0.0)

    return b

def get_qpt_strs(qpts):
    qpt_strs = np.zeros(qpts.shape[0],dtype=object)
    for ii in range(qpts.shape[0]):
        _q = qpts[ii,:]
        qpt_strs[ii] = f'{_q[0]: 5.3f}, {_q[1]: 5.3f}, {_q[2]: 5.3f}'
    return qpt_strs


fig, ax = plt.subplots(figsize=(6,6))

with h5py.File('neutrons.hdf5','r') as db:
    form_factors = db['form_factors'][...]
    structure_factors = db['structure_factors'][...]
    freqs = db['frequencies'][...]
    qpts = np.abs(db['qpts_rlu'][...]).round(2)
    num_qpts = db['num_qpts'][...]
    if 'qpts_distances' in db.keys():
        qpts_dist = db['qpts_distances'][...]
        qpts_verts = db['qpts_vert_distances'][...]
        qpts_path = db['qpts_path'][...]

with h5py.File('renormalization.hdf5','r') as db:
        _real = db['phonon_self_energy_real'][...].squeeze()
        _imag = db['phonon_self_energy_imag'][...].squeeze()
        _adiabatic = db['phonon_self_energy_adiabatic'][...].squeeze()
        energy = db['phonon_self_energy_energy'][...]
        _freqs = db['frequencies'][...]
        #new_freqs = db['renormalized_phonon_frequencies'][...]
        #fwhm = db['phonon_fwhm'][...]
        qpts_specfun = db['qpts_rlu'][...].round(2)

qpts_verts /= qpts_dist.max()
qpts_dist /= qpts_dist.max()

num_bands = freqs.shape[1]
num_qpts = freqs.shape[0]

# [energy, qpts, modes]
spec_func = get_specfun(energy,_freqs,_real,_imag,_adiabatic,1e-3)

qpts = get_qpt_strs(qpts)
qpts_specfun = get_qpt_strs(qpts_specfun)

renorm_specfun = np.zeros((energy.size,num_qpts),dtype=float)

for ii in range(num_qpts):
    for jj in range(num_bands):
        
        _ind = np.flatnonzero(qpts_specfun == qpts[ii])
        if _ind.size == 0:
            continue
        renorm_specfun[:,ii] += spec_func[:,_ind[0],jj]*form_factors[ii,jj]

#vmax = 2.5e-4 #0.025 #1.0
vmax = renorm_specfun.max()*0.1
extent = [0,1,energy.min(),energy.max()]
ax.imshow(renorm_specfun,cmap='hot',vmin=0,vmax=vmax,aspect='auto',origin='lower',
            interpolation='none',extent=extent)

for ii in range(num_bands):
    ax.plot(qpts_dist,freqs[:,ii],marker='o',ms=0,c='g',lw=1,ls=(0,(2,1)))

for v in qpts_verts:
    ax.plot([v,v],[0,energy.max()],ms=0,c=(0.5,0.5,0.5),lw=1,ls='--')

#ax[0].axis([0,1,0,2.5])
ax.set_ylim([0,energy.max()])
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









