import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

conv = 1.0 #3/8

# --------------------------------------------------------------------------------------------------

def get_points(fs,kpts):
    inds = np.flatnonzero(fs > 0.3)
    print(inds)
    x = kpts[inds,0]
    y = kpts[inds,1]
    return x, y

# --------------------------------------------------------------------------------------------------

def plot_electrons(n,U,order):

    n *= 4.0
    fig, ax = plt.subplots(2,1,figsize=(4.5,8),height_ratios=[0.75,1],gridspec_kw={'hspace':0.1})

    f = f'bands/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'
    with h5py.File(f,'r') as db:
        evals = db['eigenvalues'][...] #* conv
        dist = db['kpts_vert_distances'][...]
        ef = db['fermi_energy'][...] #* conv

    num_kpts, num_bands, num_spin = evals.shape

    dist /= dist.max()

    kpts = np.linspace(0,1,num_kpts)
    ax[0].axhline(ef,lw=0.75,ls='--',c='k')
    ax[0].fill_between(kpts,ef+0.08,ef-0.08,color='m',alpha=0.1)

    for ii in range(num_bands):
        ax[0].plot(kpts,evals[:,ii,0],c='r',lw=2)
        ax[0].plot(kpts,evals[:,ii,1],c='b',lw=2)

    for d in dist:
        ax[0].axvline(d,lw=0.5,ls=':',c=(0.25,0.25,0.25))

    # -----------------------------------------

    f = f'nscf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'
    with h5py.File(f,'r') as db:

        fermi_surface = db['fermi_surface'][...]
        if not 'kpts_mesh' in db.keys():                
            exit('do calculation on mesh instead')
        kpts_mesh = db['kpts_mesh'][...]
        kpts = db['kpts_rlu'][...]
        metal = db['is_metal'][...]

    # ax[0].axhline(ef,lw=0.75,ls='--',c='b')
    # ax[0].axhline(ef,lw=0.75,ls='--',c='k')

    shape = fermi_surface.shape
    num_kpts = shape[0]
    num_bands = shape[1]
    num_spin = shape[2]

    fermi_surface = np.nansum(fermi_surface,axis=1)
    # fermi_surface = fermi_surface.sum(axis=1)
    # fermi_surface /= np.nanmax(fermi_surface)

    x, y = get_points(fermi_surface[...,0],kpts) # spin up
    ax[1].scatter(x,y,s=0.5,c='r',alpha=0.75)
    x, y = get_points(fermi_surface[...,1],kpts) # spin down
    ax[1].scatter(x,y,s=0.5,c='b',alpha=0.75)

    ax[0].set_title(f'metal: {metal}, {f}')

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

    ax[0].annotate(f'(a)',xy=(-0.1,1.05),xycoords='axes fraction',fontsize=10,annotation_clip=False)
    ax[1].annotate(f'(b)',xy=(-0.1,0.975),xycoords='axes fraction',fontsize=10,annotation_clip=False)

    plt.savefig(f'{order}_U_{U:3.2f}_N_{n:3.2f}.png',dpi=300,bbox_inches='tight')
    plt.show()
    plt.close()


if __name__ == '__main__':

    calcs = [[ 0.5,   0.5, 'afm'],
             [ 0.5,   0.6, 'afm'],
             [ 0.5,   0.7, 'afm'],
             [ 0.5,   0.8, 'afm'],
             [ 0.5,   0.9, 'afm'],
             [ 0.5,   1.0, 'afm'],
             [ 0.5,   1.1, 'afm'],
             [ 0.5,   1.2, 'afm'],
             [ 0.5,   1.3, 'afm'],
             [ 0.5,   1.4, 'afm'],
             [ 0.5,   1.5, 'afm'],
             [ 0.5,   2.0, 'afm'],
             [0.475,    2, 'afm'],
             [0.45,     3, 'afm'],
             [ 0.4,     4, 'afm'],
             [ 0.3,     7, 'afm'],
              [0.4,     5, 'fim'],
              [0.4,     6, 'fim'],
              [0.4,     7, 'fim'],
             [0.475,    3, 'fim'],
             [0.475,    4, 'fim'],
             [0.475,    5, 'fim'],
             [0.475,   10, 'fim'],
             [0.475,   20, 'fim'],
             [0.45,     4, 'fim'],
             [0.45,     5, 'fim'],
             [0.45,     6, 'fim'],
             [0.45,    10, 'fim'],
            [ 0.5,   2.5, 'afm'],
            [ 0.5,   3.0, 'afm'],
            [ 0.5,   3.5, 'afm'],
            [ 0.5,   4.0, 'afm'],
            [ 0.5,   4.5, 'afm'],
            [ 0.5,   5.0, 'afm']]   
    num_calcs = len(calcs)

    for calc in calcs:
        plot_electrons(*calc)