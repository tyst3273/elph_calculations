
import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize
import sys

import colormaps as cmaps
cmap = cmaps.amethyst

conv = 3/8 * 1000 # meV
el_conv = 3/8

# conv = 1.0

# --------------------------------------------------------------------------------------------------

def get_points(fs,kpts):
    inds = np.flatnonzero(fs > 0.3)
    x = kpts[inds,0]
    y = kpts[inds,1]
    return x, y

# --------------------------------------------------------------------------------------------------

def get_specfun(energy,freqs,real,imag,adiabatic,eta):

    shape = real.shape
    num_qpts = shape[1]
    num_modes = shape[2]

    b = np.zeros(shape,dtype=float)

    for ii in range(num_qpts):
        for jj in range(num_modes):

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

# --------------------------------------------------------------------------------------------------

def get_data(input_file):

    with h5py.File(input_file,'r') as db:
        real = db['phonon_self_energy_real'][...].squeeze()
        imag = db['phonon_self_energy_imag'][...].squeeze()
        adiabatic = db['phonon_self_energy_adiabatic'][...].squeeze()
        spec_func = db['phonon_spectral_function'][...].sum(axis=-1).squeeze()
        energy = db['phonon_self_energy_energy'][...]
        freqs = db['frequencies'][...]
        new_freqs = db['renormalized_phonon_frequencies'][...]
        fwhm = db['phonon_fwhm'][...]
        if 'qpts_distances' in db.keys():
            qpts_dist = db['qpts_distances'][...]
            qpts_verts = db['qpts_vert_distances'][...]

    print(spec_func.shape)

    qpts_verts /= qpts_verts.max()
    qpts = qpts_dist / qpts_dist.max()
    # num_bands = freqs.shape[1]
    # num_qpts = freqs.shape[0]

    spec_func = get_specfun(energy,freqs,real,imag,adiabatic,1e-5)
    spec_func = spec_func.sum(axis=-1) # sum over spins ?
    spec_func /= spec_func.max()

    energy *= conv
    freqs *= conv
    new_freqs *= conv
    fwhm *= conv

    return spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts

# --------------------------------------------------------------------------------------------------

fig = plt.figure(figsize=(9,4))
gs = plt.GridSpec(2, 3, hspace = 0.25, wspace = 0.1, width_ratios=[1,1,1])
ax0 = fig.add_subplot(gs[0,0])
ax1 = fig.add_subplot(gs[1,0])

ax2 = fig.add_subplot(gs[0,1])
ax3 = fig.add_subplot(gs[1,1])

ax4 = fig.add_subplot(gs[0,2])
ax5 = fig.add_subplot(gs[1,2])

vmin = 1e-5
vmax = 0.01
c = (1.0,0.0,0.0)

# -------------------

f = 'specfun/afm_U_0.50_N_2.00.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
ax0.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

# -------------------

f = 'specfun/afm_U_2.00_N_2.00.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
im = ax1.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

# -------------------

f = 'specfun/afm_U_2.00_N_1.90.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
ax2.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

# -------------------

f = 'specfun/afm_U_3.00_N_1.80.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
im = ax3.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    
# -------------------

f = 'specfun/fim_U_10.00_N_1.80.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
ax4.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

# -------------------

f = 'specfun/afm_U_0.80_N_2.00.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
im = ax5.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

# -------------------

for v in qpts_verts:
    ax0.axvline(v,lw=0.5,ls=':',c='w')
    ax1.axvline(v,lw=0.5,ls=':',c='w')
    ax2.axvline(v,lw=0.5,ls=':',c='w')
    ax3.axvline(v,lw=0.5,ls=':',c='w')
    ax4.axvline(v,lw=0.5,ls=':',c='w')
    ax5.axvline(v,lw=0.5,ls=':',c='w')

# -------------------

f = '/home/ty/research/repos/elph_calculations/paper/prim/specfun/specfun/pm_U_0.00_N_1.00.hdf5'
_, _, freqs, _, _, qpts, _ = get_data(f)

num_bands = freqs.shape[1]
for ii in range(num_bands):
    ax0.plot(qpts,freqs[:,ii],marker='o',ms=0,c=c,lw=0.75,ls=(0,(2,1)))
    
# ---------------------------

for _ax in [ax0,ax1,ax2,ax3,ax4,ax5]:
    for axis in ['top','bottom','left','right']:
        _ax.spines[axis].set_linewidth(1.5)
    # _ax.minorticks_on()
    _ax.tick_params(which='both',width=1,labelsize=10) #,direction='in')
    _ax.tick_params(which='major',length=5)
    _ax.tick_params(which='minor',length=2)
    _ax.set_rasterization_zorder = 1000000000

ax0.axis([0,1,62,80])
ax1.axis([0,1,62,80])
ax2.axis([0,1,62,80])
ax3.axis([0,1,62,80])
ax4.axis([0,1,62,80])
ax5.axis([0,1,62,80])

ax2.set_yticklabels([])
ax3.set_yticklabels([])
ax4.set_yticklabels([])
ax5.set_yticklabels([])

ax0.set_xticks(qpts_verts)
ax2.set_xticks(qpts_verts)
ax4.set_xticks(qpts_verts)

ax1.set_xticks(qpts_verts)
ax1.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
ax3.set_xticks(qpts_verts)
ax3.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
ax5.set_xticks(qpts_verts)
ax5.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])

ax0.set_ylabel('Energy [meV]',fontsize=10,labelpad=5)
ax1.set_ylabel('Energy [meV]',fontsize=10,labelpad=5)

# ax0.annotate(f'(c)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
# ax1.annotate(f'(d)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
# ax2.annotate(f'(a)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
# ax3.annotate(f'(b)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
# ax4.annotate(f'(e)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='k')
# ax5.annotate(f'(f)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='k')

# ax0.annotate(f'FM, U=15, n=0.20',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
# ax1.annotate(f'FM, U=15, n=0.25',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')

# ax2.annotate(f'PM, U=0, n=0.40',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
# ax3.annotate(f'PM, U=0, n=0.50',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')

# ax4.set_title(f'FM, U=15, n=0.25',fontsize=10)

# plt.savefig(f'afm_cell_specfuns.png',dpi=300,bbox_inches='tight')
plt.show()
plt.close()

