import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

from calcs import calcs


# conv = 1.0 #3/8

# --------------------------------------------------------------------------------------------------

def get_weights(eigs,ef,fwhm=0.01):

    sigma = fwhm / 2.35482

    fs_weights = np.exp(-0.5 * (eigs-ef)**2/sigma**2 ) 
    fs_weights = fs_weights.sum(axis=1)  / eigs.shape[1]

    inds = np.flatnonzero( np.greater(fs_weights,1e-6) )

    return inds, fs_weights

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

    # for ii in range(num_bands):
    #     ax[0].plot(kpts,evals[:,ii,0],c='k',lw=2)

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

    for ii in range(num_bands):
        _s = 1
        ax[0].scatter(kpts[::_s],evals[::_s,ii,0],marker='o',s=20,
                      alpha=norm_weights[::_s,ii,0],c='r',lw=0)
        ax[0].scatter(kpts[::_s],evals[::_s,ii,1],marker='o',s=20,
                      alpha=norm_weights[::_s,ii,1],c='b',lw=0)
    
    for ii in range(num_bands):
        ax[0].plot(kpts[:],evals[:,ii,0],marker='o',ms=0,c='r',lw=1,ls=(0,(4,2,2,2)))
        ax[0].plot(kpts[:],evals[:,ii,1],marker='o',ms=0,c='b',lw=1,ls=(0,(4,2,2,2)))

    for d in dist:
        ax[0].axvline(d,lw=0.5,ls=':',c=(0.25,0.25,0.25))

    # -----------------------------------------

    # power = 1.2

    with h5py.File('mapped_kpts.hdf5','r') as db:
        mapped_kpts = db['mapped_kpts'][...]

    with h5py.File(prim_fs_file,'r') as db:

        eigs = db['eigenvalues'][...]
        ef = db['fermi_energy'][...]
        kpts = db['kpts_rlu'][...]
        prl = db['reciprocal_lattice_vectors'][...]

    # inds, fs_weights = get_weights(eigs[...,0],ef) 
    # ax[1].scatter(kpts[inds,0],kpts[inds,1],s=0.5,c='k',alpha=fs_weights[inds],zorder=100)

    with h5py.File(fs_file,'r') as db:

        eigs = db['eigenvalues'][...]
        ef = db['fermi_energy'][...]
        kpts = db['kpts_rlu'][...]
        scrl = db['reciprocal_lattice_vectors'][...]
        mapped_kpts = db['_mapped_kpts'][...]

    trans = np.linalg.inv( prl.T ) @ scrl.T

    inds, fs_weights = get_weights(eigs[...,0],ef) 
    if inds.size !=0 :
        # ax[1].scatter(kpts[inds,0],kpts[inds,1],s=0.5,c='r',alpha=fs_weights[inds],zorder=100)
        ax[1].scatter(mapped_kpts[inds,0],mapped_kpts[inds,1],s=0.5,c='r',
                      alpha=fs_weights[inds],zorder=100)
    
        for xx in [-1,0,1]:
            for yy in [-1,0,1]:
                dk = np.array([xx,yy,0])
                dk = trans @ dk
                ax[1].scatter(mapped_kpts[inds,0]+dk[0],mapped_kpts[inds,1]+dk[1],s=0.5,c='r',
                      alpha=fs_weights[inds],zorder=100)
                
    inds, fs_weights = get_weights(eigs[...,1],ef) 
    if inds.size !=0 :
        # ax[1].scatter(kpts[inds,0],kpts[inds,1],s=0.5,c='b',alpha=fs_weights[inds],zorder=100)
        ax[1].scatter(mapped_kpts[inds,0],mapped_kpts[inds,1],s=0.5,c='b',
                      alpha=fs_weights[inds],zorder=100)
        
        for xx in [-1,0,1]:
            for yy in [-1,0,1]:
                dk = np.array([xx,yy,0])
                dk = trans @ dk
                ax[1].scatter(mapped_kpts[inds,0]+dk[0],mapped_kpts[inds,1]+dk[1],s=0.5,c='b',
                      alpha=fs_weights[inds],zorder=100)

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