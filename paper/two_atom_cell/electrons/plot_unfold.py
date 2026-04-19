import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

from calcs import calcs


# conv = 1.0 #3/8

# --------------------------------------------------------------------------------------------------

def get_points(eigs,ef,kpts,fwhm=0.01):

    sigma = fwhm / 2.35482

    # fs_weights = np.exp(-0.5 * (eigs-ef)**2/sigma**2 ) 
    # fs_weights = fs_weights.sum(axis=1)  / eigs.shape[1]

    fs_weights = ( np.abs(eigs-ef) < fwhm ).astype(int)
    fs_weights = fs_weights.sum(axis=1)  / eigs.shape[1]

    # inds = np.flatnonzero( np.greater(fs_weights,0.000001) )
    inds = np.flatnonzero( fs_weights > 1 )

    x = kpts[inds,0]
    y = kpts[inds,1]
    return x, y, fs_weights[inds]

# --------------------------------------------------------------------------------------------------

def plot_electrons(bands_file,fs_file,prim_bands_file,prim_fs_file):

    fig, ax = plt.subplots(2,1,figsize=(4.5,8),height_ratios=[0.75,1],gridspec_kw={'hspace':0.1})

    # ----------------------------

    with h5py.File(prim_bands_file,'r') as db:
        evals = db['eigenvalues'][...] #* conv
        dist = db['kpts_vert_distances'][...]
        # ef = db['fermi_energy'][...] #* conv

    with h5py.File(prim_fs_file,'r') as db:
        ef = db['fermi_energy'][...]

    num_kpts, num_bands, num_spin = evals.shape

    dist /= dist.max()
    kpts = np.linspace(0,1,num_kpts)

    # ax[0].axhline(ef,lw=0.75,ls=(0,(4,1,2,1)),c='k')

    for ii in range(num_bands):
        ax[0].plot(kpts,evals[:,ii,0],c='k',lw=2)

    with h5py.File(bands_file,'r') as db:
        evals = db['eigenvalues'][...] #* conv
        dist = db['kpts_vert_distances'][...]
        ef = db['fermi_energy'][...] #* conv
        weights = db['_unfolding_weights'][...]

    norm_weights = ( weights / weights.max() ) ** 1.2

    num_kpts, num_bands, num_spin = evals.shape

    dist /= dist.max()
    kpts = np.linspace(0,1,num_kpts)

    ax[0].axhline(ef,lw=0.75,ls=(0,(4,2)),c='k')

    # for ii in range(num_bands):
    #     _s = 1
    #     ax[0].scatter(kpts[::_s],evals[::_s,ii,0],marker='o',s=10,
    #                   alpha=norm_weights[::_s,ii,0],c='r',lw=0)
    #     ax[0].scatter(kpts[::_s],evals[::_s,ii,1],marker='o',s=10,
    #                   alpha=norm_weights[::_s,ii,1],c='b',lw=0)
    
    for ii in range(num_bands):
        _s = 1
        ax[0].plot(kpts[::_s],evals[::_s,ii,0],marker='o',ms=1,c='r',lw=0)
        ax[0].plot(kpts[::_s],evals[::_s,ii,1],marker='o',ms=1,c='b',lw=0)

    for d in dist:
        ax[0].axvline(d,lw=0.5,ls=':',c=(0.25,0.25,0.25))

    # -----------------------------------------

    # power = 1.2

    with h5py.File(prim_fs_file,'r') as db:

        fermi_surface = db['fermi_surface'][...]
        eigs = db['eigenvalues'][...]
        ef = db['fermi_energy'][...]
        if not 'kpts_mesh' in db.keys():                
            exit('do calculation on mesh instead')
        kpts_mesh = db['kpts_mesh'][...]
        kpts = db['kpts_rlu'][...]
        metal = db['is_metal'][...]

    # x, y, fs_weights = get_points(eigs[...,0],ef,kpts) 
    # ax[1].scatter(x,y,s=0.5,c='k',alpha=fs_weights,zorder=100)

    with h5py.File(fs_file,'r') as db:

        fermi_surface = db['fermi_surface'][...]
        eigs = db['eigenvalues'][...]
        ef = db['fermi_energy'][...]
        if not 'kpts_mesh' in db.keys():                
            exit('do calculation on mesh instead')
        kpts_mesh = db['kpts_mesh'][...]
        kpts = db['kpts_rlu'][...]
        metal = db['is_metal'][...]
        mapped_kpts = db['_mapped_kpts'][...]
        weights = db['_unfolding_weights'][...]
        fs_weights = db['_fs_weights'][...]

    # x, y, fs_weights = get_points(eigs[...,0],ef,kpts) 
    # if fs_weights.size != 0:
    #     ax[1].scatter(x,y,s=0.5,c='r',alpha=fs_weights,zorder=100)
    # x, y, fs_weights = get_points(eigs[...,1],ef,kpts) 
    # if fs_weights.size != 0:
    #     ax[1].scatter(x,y,s=0.5,c='b',alpha=fs_weights,zorder=100)

    x, y, fs_weights = get_points(eigs[...,0],ef,kpts) 
    if fs_weights.size != 0:
        ax[1].scatter(x,y,s=0.5,c='r',alpha=1.0,zorder=100)
    x, y, fs_weights = get_points(eigs[...,1],ef,kpts) 
    if fs_weights.size != 0:
        ax[1].scatter(x,y,s=0.5,c='b',alpha=1.0,zorder=100)

    # if weights.size != 0:

    #     norm_weights = weights / weights.max() 

    #     shape = fermi_surface.shape
    #     num_kpts = shape[0]
    #     num_bands = shape[1]
    #     num_spin = shape[2]

    #     x, y = mapped_kpts[:,0], mapped_kpts[:,1]
    #     # ax[1].scatter(x,y,s=0.5,c='r',alpha=(fs_weights[:,:,0]*norm_weights[:,:,0]).sum(axis=1))
    #     # ax[1].scatter(x,y,s=0.5,c='b',alpha=(fs_weights[:,:,1]*norm_weights[:,:,1]).sum(axis=1))
    #     ax[1].scatter(x,y,s=0.5,c='r',alpha=(fs_weights[:,:,0]).sum(axis=1)/2.0)
    #     ax[1].scatter(x,y,s=0.5,c='b',alpha=(fs_weights[:,:,1]).sum(axis=1)/2.0)

    ax[0].set_title(f'metal: {metal}')

    # -----------------------------------------

    for _ax in ax:
        for axis in ['top','bottom','left','right']:
            _ax.spines[axis].set_linewidth(1.5)
        # _ax.minorticks_on()
        _ax.tick_params(which='both',width=1,labelsize=10,direction='in')
        _ax.tick_params(which='major',length=5)
        _ax.tick_params(which='minor',length=2)
        _ax.set_rasterization_zorder = 1000000000

    ax[0].set_xticks(dist)
    ax[0].set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
    ax[0].set_xlim([0,1])
    ax[0].set_ylabel('E [eV]',fontsize=12,labelpad=5)

    ax[1].axis([-0.5,0.5,-0.5,0.5])
    ax[1].set_ylabel('k [rlu]',fontsize=12,labelpad=5)
    ax[1].set_xlabel('h [rlu]',fontsize=12,labelpad=5)

    ax[0].annotate(f'(a)',xy=(-0.1,1.05),xycoords='axes fraction',
                   fontsize=10,annotation_clip=False)
    ax[1].annotate(f'(b)',xy=(-0.1,0.975),xycoords='axes fraction',
                   fontsize=10,annotation_clip=False)

    plt.savefig(f'electrons.png',dpi=300,bbox_inches='tight')
    plt.show()
    plt.close()


if __name__ == '__main__':

    num_calcs = len(calcs)

    for ii in range(num_calcs):
        
        n, U, order = calcs[ii]

        n *= 4.0

        print(f'\nnow on num {ii}/{num_calcs}')
        print('n:',n)
        print('U:',U)
        print('order:',order)

        bands_file = f'bands/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'
        nscf_file = f'nscf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'

        prim_n = n / 2.0
        prim_bands_file = f'unfold/bands/pm_U_{U:3.2f}_N_{prim_n:3.2f}.hdf5'
        prim_nscf_file = f'unfold/nscf/pm_U_{U:3.2f}_N_{prim_n:3.2f}.hdf5'
        
        plot_electrons(bands_file,nscf_file,prim_bands_file,prim_nscf_file)