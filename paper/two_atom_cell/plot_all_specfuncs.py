
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

def plot_fs(fs_file,prim_fs_file,ax):

    with h5py.File(prim_fs_file,'r') as db:

        prl = db['reciprocal_lattice_vectors'][...]

    with h5py.File(fs_file,'r') as db:

        eigs = db['eigenvalues'][...]
        ef = db['fermi_energy'][...]
        scrl = db['reciprocal_lattice_vectors'][...]
        mapped_kpts = db['_mapped_kpts'][...]

    trans = np.linalg.inv( prl.T ) @ scrl.T

    inds, fs_weights = get_weights(eigs[...,0],ef) 
    if inds.size !=0 :
        ax.scatter(mapped_kpts[inds,0],mapped_kpts[inds,1],s=0.5,c='r',
                      alpha=fs_weights[inds],zorder=100)
    
        for xx in [-1,0,1]:
            for yy in [-1,0,1]:
                dk = np.array([xx,yy,0])
                dk = trans @ dk
                ax.scatter(mapped_kpts[inds,0]+dk[0],mapped_kpts[inds,1]+dk[1],s=0.5,c='r',
                      alpha=fs_weights[inds],zorder=100)
                
    inds, fs_weights = get_weights(eigs[...,1],ef) 
    if inds.size !=0 :
        ax.scatter(mapped_kpts[inds,0],mapped_kpts[inds,1],s=0.5,c='b',
                      alpha=fs_weights[inds],zorder=100)
        
        for xx in [-1,0,1]:
            for yy in [-1,0,1]:
                dk = np.array([xx,yy,0])
                dk = trans @ dk
                ax.scatter(mapped_kpts[inds,0]+dk[0],mapped_kpts[inds,1]+dk[1],s=0.5,c='b',
                      alpha=fs_weights[inds],zorder=100)

# --------------------------------------------------------------------------------------------------

def plot_electron_bands(bands_file,ax):

    with h5py.File(bands_file,'r') as db:
        evals = db['eigenvalues'][...] #* conv
        dist = db['kpts_vert_distances'][...]
        ef = db['fermi_energy'][...] #* conv
        weights = db['_unfolding_weights'][...]

    norm_weights = ( weights / weights.max() ) ** 1.2

    num_kpts, num_bands, num_spin = evals.shape

    dist /= dist.max()
    kpts = np.linspace(0,1,num_kpts)

    ax.axhline(ef,lw=0.75,ls=(0,(4,2)),c='k')

    for ii in range(num_bands):
        _s = 1
        ax.scatter(kpts[::_s],evals[::_s,ii,0],marker='o',s=20,
                      alpha=norm_weights[::_s,ii,0],c='r',lw=0)
        ax.scatter(kpts[::_s],evals[::_s,ii,1],marker='o',s=20,
                      alpha=norm_weights[::_s,ii,1],c='b',lw=0)
    
    for ii in range(num_bands):
        ax.plot(kpts[:],evals[:,ii,0],marker='o',ms=0,c='r',lw=1,ls=(0,(4,2,2,2)))
        ax.plot(kpts[:],evals[:,ii,1],marker='o',ms=0,c='b',lw=1,ls=(0,(4,2,2,2)))

    for d in dist:
        ax.axvline(d,lw=0.5,ls=':',c=(0.25,0.25,0.25))

# --------------------------------------------------------------------------------------------------

def get_weights(eigs,ef,fwhm=0.01):

    sigma = fwhm / 2.35482

    fs_weights = np.exp(-0.5 * (eigs-ef)**2/sigma**2 ) 
    fs_weights = fs_weights.sum(axis=1)  / eigs.shape[1]

    inds = np.flatnonzero( np.greater(fs_weights,1e-6) )

    return inds, fs_weights

# --------------------------------------------------------------------------------------------------

def get_points(fs,kpts):
    inds = np.flatnonzero(fs > 0.3)
    x = kpts[inds,0]
    y = kpts[inds,1]
    return x, y

# --------------------------------------------------------------------------------------------------

def get_specfun(energy,freqs,real,imag,adiabatic,eta,weights=None):

    shape = real.shape
    num_qpts = shape[1]
    num_modes = shape[2]

    if weights is None:
        weights = np.ones((num_qpts,num_modes))

    b = np.zeros(shape,dtype=float)

    for ii in range(num_qpts):
        for jj in range(num_modes):

            wq = freqs[ii,jj]
            g = imag[:,ii,jj]

            d = real[:,ii,jj]
            d0 = adiabatic[ii,jj]

            b[:,ii,jj] = weights[ii,jj] * -2*wq * (2*wq*g - 2*energy*eta) / \
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

        if '_unfolding_weights' in db.keys():
            weights = db['_unfolding_weights'][...]
        else:
            weights = None

    qpts_verts /= qpts_verts.max()
    qpts = qpts_dist / qpts_dist.max()

    spec_func = get_specfun(energy,freqs,real,imag,adiabatic,1e-5,weights)
    spec_func = spec_func.sum(axis=-1) # sum over spins ?
    spec_func /= spec_func.max()

    energy *= conv
    freqs *= conv
    new_freqs *= conv
    fwhm *= conv

    qpts = np.linspace(0,1,qpts.size)

    return spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts

# --------------------------------------------------------------------------------------------------

fig = plt.figure(figsize=(9,4))
gs = plt.GridSpec(2, 3, hspace = 0.25, wspace = 0.25, width_ratios=[1,0.5,0.5])

afm_sf = fig.add_subplot(gs[0,0])
afm_b = fig.add_subplot(gs[0,1])
afm_fs = fig.add_subplot(gs[1,1])

fim_sf = fig.add_subplot(gs[1,0])
fim_b = fig.add_subplot(gs[0,2])
fim_fs = fig.add_subplot(gs[1,2])

# fim2_sf = fig.add_subplot(gs[2,0])
# fim2_b = fig.add_subplot(gs[2,1])
# fim2_fs = fig.add_subplot(gs[2,2])

vmin = 1e-5
vmax = 0.01
c = (1.0,0.0,0.0)

# -------------------

f = '../prim/specfun/specfun/pm_U_0.00_N_1.00.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

num_bands = freqs.shape[1]
for ii in range(num_bands):
    afm_sf.plot(qpts,freqs[:,ii],marker='o',ms=0,c=c,lw=0.75,ls=(0,(2,1)),zorder=100)
    fim_sf.plot(qpts,freqs[:,ii],marker='o',ms=0,c=c,lw=0.75,ls=(0,(2,1)),zorder=100)
    # fim2_sf.plot(qpts,freqs[:,ii],marker='o',ms=0,c=c,lw=0.75,ls=(0,(2,1)),zorder=100)

# -------------------

f = 'specfun/specfun/afm_U_4.00_N_1.60.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
afm_sf.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

# # -------------------

# f = 'specfun/specfun/fim_U_4.00_N_1.80.hdf5'
# spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

# norm = LogNorm(vmin=vmin,vmax=vmax)
# extent = [0,1,energy.min(),energy.max()]
# fim_sf.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
#             interpolation='none',extent=extent)    

# -------------------

f = 'specfun/specfun/fim_U_15.00_N_1.90.hdf5'
spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(f)

norm = LogNorm(vmin=vmin,vmax=vmax)
extent = [0,1,energy.min(),energy.max()]
fim_sf.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
            interpolation='none',extent=extent)    

# -------------------

f = 'electrons/bands/afm_U_4.00_N_1.60.hdf5'
plot_electron_bands(f,afm_b)

f = 'electrons/nscf/afm_U_4.00_N_1.60.hdf5'
p = 'electrons/unfold/nscf/pm_U_0.00_N_1.00.hdf5'
plot_fs(f,p,afm_fs)

# -------------------

f = 'electrons/bands/fim_U_15.00_N_1.90.hdf5'
plot_electron_bands(f,fim_b)

f = 'electrons/nscf/fim_U_15.00_N_1.90.hdf5'
p = 'electrons/unfold/nscf/pm_U_0.00_N_1.00.hdf5'
plot_fs(f,p,fim_fs)

# # cbar = fig.colorbar(im,ax=[pm0,pm1],location='top',extend='both',aspect=40,pad=0.01)

# for v in qpts_verts:
#     pm0.axvline(v,lw=0.5,ls=':',c='w')
#     pm1.axvline(v,lw=0.5,ls=':',c='w')
#     fm0.axvline(v,lw=0.5,ls=':',c='w')
#     fm1.axvline(v,lw=0.5,ls=':',c='w')

# # -------------------

# f = f'../electrons/bands/fm_U_15.00_N_0.50.hdf5'
# with h5py.File(f,'r') as db:
#     evals = db['eigenvalues'][...].squeeze() * el_conv
#     kpts = db['kpts_vert_distances'][...]
#     kpts_verts = db['kpts_vert_distances'][...]
#     ef = db['fermi_energy'][...] * el_conv
#     # print(db.keys())
#     # kpts = db['kpts_rlu'][...]

# num_kpts, num_spin = evals.shape

# kpts /= kpts.max()
# kpts_verts /= kpts_verts.max()

# kpts = np.linspace(0,1,num_kpts)

# el0.plot(kpts,evals[...,0],c='r',lw=2)
# el0.plot(kpts,evals[...,1],c='b',lw=2)
# el0.axhline(ef,lw=0.75,ls='--',c='m')
# for v in kpts_verts:
#     el0.axvline(v,lw=0.5,ls=':',c=(0.25,0.25,0.25))

# # -----------------------------------------

# f = f'../electrons/nscf/fm_U_15.00_N_0.50.hdf5'
# with h5py.File(f,'r') as db:
#     fermi_surface = db['fermi_surface'][...]
#     if not 'kpts_mesh' in db.keys():                
#         exit('do calculation on mesh instead')
#     kpts_mesh = db['kpts_mesh'][...]
#     kpts = db['kpts_rlu'][...]

#     ef = db['fermi_energy'][...] * el_conv

# shape = fermi_surface.shape
# num_kpts = shape[0]
# num_bands = shape[1]
# num_spin = shape[2]

# fermi_surface = fermi_surface.squeeze()
# fermi_surface /= fermi_surface.max()

# print(np.nanmax(fermi_surface))

# x, y = get_points(fermi_surface[...,0],kpts) # spin up
# el1.scatter(x,y,s=0.5,c='r',alpha=0.75)

# x, y = get_points(fermi_surface[...,1],kpts) # spin down
# el1.scatter(x,y,s=0.5,c='b',alpha=0.75)

# # ---------------------------

# # ax[1].annotate('n=0.1',xycoords='data',textcoords='data',xy=(-0.45,0.45),xytext=(-0.075,0.0),
# #             arrowprops=dict(arrowstyle='-|>',lw=1,color='k'),fontsize=10)
# # ax[1].annotate('',xycoords='data',textcoords='data',xy=(-0.41,0.41),xytext=(-0.09,0.09),
# #             arrowprops=dict(arrowstyle='->',lw=1,color='k'),fontsize=10)
# # ax[1].annotate('n=0.05',xycoords='data',xy=(-0.1,0.025),fontsize=10,fontweight='bold')
# # ax[1].annotate('n=0.50',xycoords='data',xy=(-0.2,0.25),fontsize=10,fontweight='bold')
# # ax[1].annotate('n=0.95',xycoords='data',xy=(-0.475,0.425),fontsize=10,fontweight='bold')

# # ax[1].plot(-0.09,0.09,marker='o',ms=4,mec='k',mfc='k')
# # ax[1].plot(-0.41,0.41,marker='o',ms=4,mec='k',mfc='k')
# # ax[1].plot(-0.25,0.25,marker='o',ms=4,mec='k',mfc='k')

for _ax in [afm_sf,afm_b,afm_fs, fim_sf,fim_b,fim_fs]:
    for axis in ['top','bottom','left','right']:
        _ax.spines[axis].set_linewidth(1.5)
    # _ax.minorticks_on()
    _ax.tick_params(which='both',width=1,labelsize=10) #,direction='in')
    _ax.tick_params(which='major',length=5)
    _ax.tick_params(which='minor',length=2)
    _ax.set_rasterization_zorder = 1000000000

afm_b.yaxis.tick_right()
afm_fs.yaxis.tick_right()

fim_b.yaxis.tick_right()
fim_fs.yaxis.tick_right()
fim_b.yaxis.label_position = 'right'
fim_fs.yaxis.label_position = 'right'

# el0.yaxis.tick_right()
# el1.yaxis.tick_right()
# el0.yaxis.label_position = 'right'
# el1.yaxis.label_position = 'right'

afm_sf.axis([0,1,62,80])
afm_b.axis([0,1,-3.5,6.5])
afm_fs.axis([-0.5,0.5,-0.5,0.5])

fim_sf.axis([0,1,62,80])
fim_b.axis([0,1,-4.5,5.5])
fim_fs.axis([-0.5,0.5,-0.5,0.5])

afm_fs.set_yticklabels([])
# fm1.set_yticklabels([])

afm_sf.set_xticks(qpts_verts)
afm_sf.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
fim_sf.set_xticks(qpts_verts)
fim_sf.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])

afm_b.set_xticks(qpts_verts)
afm_b.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
fim_b.set_xticks(qpts_verts)
fim_b.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])

afm_fs.set_yticks([-0.5,0,0.5])
fim_fs.set_yticks([-0.5,0,0.5])

# pm0.set_xticks(qpts_verts)
# pm0.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
# pm1.set_xticks(qpts_verts)
# pm1.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])

afm_sf.set_ylabel('Energy [meV]',fontsize=10,labelpad=5)
fim_sf.set_ylabel('Energy [meV]',fontsize=10,labelpad=5)

# afm_b.set_ylabel('Energy [eV]',fontsize=10,labelpad=20)
# afm_fs.set_ylabel('k [rlu]',fontsize=10,labelpad=10)
afm_fs.set_xlabel('h [rlu]',fontsize=10,labelpad=5)

fim_b.set_ylabel('Energy [eV]',fontsize=10,labelpad=15)
fim_fs.set_ylabel('k [rlu]',fontsize=10,labelpad=10)
fim_fs.set_xlabel('h [rlu]',fontsize=10,labelpad=5)

# el0.set_xticks(qpts_verts)
# el0.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
# el1.set_xticks([-0.5,0,0.5])
# el1.set_yticks([-0.5,0,0.5])

afm_sf.annotate(f'(a)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
fim_sf.annotate(f'(b)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')

afm_b.annotate(f'(c)',xy=(0.015,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='k')
afm_fs.annotate(f'(d)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='k')

fim_b.annotate(f'(e)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='k')
fim_fs.annotate(f'(f)',xy=(0.01,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='k')

afm_sf.annotate(f'AFM, U=4, n=0.40',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
fim_sf.annotate(f'FiM, U=15, n=0.475',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')

# pm0.annotate(f'PM, U=0, n=0.40',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')
# pm1.annotate(f'PM, U=0, n=0.50',xy=(0.4,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c='w')

afm_b.set_title(f'AFM, U=4, n=0.40',fontsize=10)
fim_b.set_title(f'FiM, U=15, n=0.475',fontsize=10)


plt.savefig(f'two_atom_specfuns.png',dpi=300,bbox_inches='tight')
plt.show()
plt.close()

