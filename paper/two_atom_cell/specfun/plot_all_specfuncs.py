
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
gs = plt.GridSpec(2, 3, hspace = 0.25, wspace = 0.1, width_ratios=[1,1,0.6])
fm0 = fig.add_subplot(gs[0,1])
fm1 = fig.add_subplot(gs[1,1])

pm0 = fig.add_subplot(gs[0,0])
pm1 = fig.add_subplot(gs[1,0])

el0 = fig.add_subplot(gs[0,2])
el1 = fig.add_subplot(gs[1,2])

vmin = 1e-5
vmax = 0.01
c = (1.0,0.0,0.0)

# -------------------

f = 'specfun/fm_U_15.00_N_0.40.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
fm0.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

num_bands = freqs.shape[1]
for ii in range(num_bands):
    fm0.plot(qpts,freqs[:,ii],marker='o',ms=0,c=c,lw=0.75,ls=(0,(2,1)))

# -------------------

f = 'specfun/fm_U_15.00_N_0.50.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
im = fm1.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

num_bands = freqs.shape[1]
for ii in range(num_bands):
    fm1.plot(qpts,freqs[:,ii],marker='o',ms=0,c=c,lw=0.75,ls=(0,(2,1)))

# -------------------

f = 'specfun/pm_U_0.00_N_0.80.hdf5'
# f = 'specfun/pm_U_0.00_N_0.50.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
pm0.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

num_bands = freqs.shape[1]
for ii in range(num_bands):
    pm0.plot(qpts,freqs[:,ii],marker='o',ms=0,c=c,lw=0.75,ls=(0,(2,1)))

# -------------------

f = 'specfun/pm_U_0.00_N_1.00.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
im = pm1.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

num_bands = freqs.shape[1]
for ii in range(num_bands):
    pm1.plot(qpts,freqs[:,ii],marker='o',ms=0,c=c,lw=0.75,ls=(0,(2,1)))

# -------------------

# cbar = fig.colorbar(im,ax=[pm0,pm1],location='top',extend='both',aspect=40,pad=0.01)

for v in qpts_verts:
    pm0.axvline(v,lw=0.5,ls=':',c='w')
    pm1.axvline(v,lw=0.5,ls=':',c='w')
    fm0.axvline(v,lw=0.5,ls=':',c='w')
    fm1.axvline(v,lw=0.5,ls=':',c='w')

# -------------------

f = f'../electrons/bands/fm_U_15.00_N_0.50.hdf5'
with h5py.File(f,'r') as db:
    evals = db['eigenvalues'][...].squeeze() * el_conv
    kpts = db['kpts_vert_distances'][...]
    kpts_verts = db['kpts_vert_distances'][...]
    ef = db['fermi_energy'][...] * el_conv
    # print(db.keys())
    # kpts = db['kpts_rlu'][...]

num_kpts, num_spin = evals.shape

kpts /= kpts.max()
kpts_verts /= kpts_verts.max()

kpts = np.linspace(0,1,num_kpts)

el0.plot(kpts,evals[...,0],c='r',lw=2)
el0.plot(kpts,evals[...,1],c='b',lw=2)
el0.axhline(ef,lw=0.75,ls='--',c='m')
for v in kpts_verts:
    el0.axvline(v,lw=0.5,ls=':',c=(0.25,0.25,0.25))

# -----------------------------------------

f = f'../electrons/nscf/fm_U_15.00_N_0.50.hdf5'
with h5py.File(f,'r') as db:
    fermi_surface = db['fermi_surface'][...]
    if not 'kpts_mesh' in db.keys():                
        exit('do calculation on mesh instead')
    kpts_mesh = db['kpts_mesh'][...]
    kpts = db['kpts_rlu'][...]

    ef = db['fermi_energy'][...] * el_conv

shape = fermi_surface.shape
num_kpts = shape[0]
num_bands = shape[1]
num_spin = shape[2]

fermi_surface = fermi_surface.squeeze()
fermi_surface /= fermi_surface.max()

print(np.nanmax(fermi_surface))

x, y = get_points(fermi_surface[...,0],kpts) # spin up
el1.scatter(x,y,s=0.5,c='r',alpha=0.75)

x, y = get_points(fermi_surface[...,1],kpts) # spin down
el1.scatter(x,y,s=0.5,c='b',alpha=0.75)

# ---------------------------

# ax[1].annotate('n=0.1',xycoords='data',textcoords='data',xy=(-0.45,0.45),xytext=(-0.075,0.0),
#             arrowprops=dict(arrowstyle='-|>',lw=1,color='k'),fontsize=10)
# ax[1].annotate('',xycoords='data',textcoords='data',xy=(-0.41,0.41),xytext=(-0.09,0.09),
#             arrowprops=dict(arrowstyle='->',lw=1,color='k'),fontsize=10)
# ax[1].annotate('n=0.05',xycoords='data',xy=(-0.1,0.025),fontsize=10,fontweight='bold')
# ax[1].annotate('n=0.50',xycoords='data',xy=(-0.2,0.25),fontsize=10,fontweight='bold')
# ax[1].annotate('n=0.95',xycoords='data',xy=(-0.475,0.425),fontsize=10,fontweight='bold')

# ax[1].plot(-0.09,0.09,marker='o',ms=4,mec='k',mfc='k')
# ax[1].plot(-0.41,0.41,marker='o',ms=4,mec='k',mfc='k')
# ax[1].plot(-0.25,0.25,marker='o',ms=4,mec='k',mfc='k')

for _ax in [fm0,fm1,pm0,pm1,el0,el1]:
    for axis in ['top','bottom','left','right']:
        _ax.spines[axis].set_linewidth(1.5)
    # _ax.minorticks_on()
    _ax.tick_params(which='both',width=1,labelsize=10) #,direction='in')
    _ax.tick_params(which='major',length=5)
    _ax.tick_params(which='minor',length=2)
    _ax.set_rasterization_zorder = 1000000000

el0.yaxis.tick_right()
el1.yaxis.tick_right()
el0.yaxis.label_position = 'right'
el1.yaxis.label_position = 'right'

fm0.axis([0,1,62,80])
fm1.axis([0,1,62,80])
pm0.axis([0,1,62,80])
pm1.axis([0,1,62,80])
el0.axis([0,1,-2,4.5])
el1.axis([-0.5,0.5,-0.5,0.5])

fm0.set_yticklabels([])
fm1.set_yticklabels([])

fm0.set_xticks(qpts_verts)
fm0.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
fm1.set_xticks(qpts_verts)
fm1.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])

pm0.set_xticks(qpts_verts)
pm0.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
pm1.set_xticks(qpts_verts)
pm1.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])

pm0.set_ylabel('Energy [meV]',fontsize=10,labelpad=5)
pm1.set_ylabel('Energy [meV]',fontsize=10,labelpad=5)

el0.set_xticks(qpts_verts)
el0.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
el1.set_xticks([-0.5,0,0.5])
el1.set_yticks([-0.5,0,0.5])
el0.set_ylabel('Energy [eV]',fontsize=10,labelpad=20)
el1.set_ylabel('k [rlu]',fontsize=10,labelpad=10)
el1.set_xlabel('h [rlu]',fontsize=10,labelpad=5)

fm0.annotate(f'(c)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
fm1.annotate(f'(d)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
pm0.annotate(f'(a)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
pm1.annotate(f'(b)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
el0.annotate(f'(e)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='k')
el1.annotate(f'(f)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='k')

fm0.annotate(f'FM, U=15, n=0.20',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
fm1.annotate(f'FM, U=15, n=0.25',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')

pm0.annotate(f'PM, U=0, n=0.40',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
pm1.annotate(f'PM, U=0, n=0.50',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')

el0.set_title(f'FM, U=15, n=0.25',fontsize=10)


plt.savefig(f'prim_specfuns.png',dpi=300,bbox_inches='tight')
plt.show()
plt.close()

