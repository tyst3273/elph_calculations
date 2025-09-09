import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

conv = 3/8

# --------------------------------------------------------------------------------------------------

def get_points(fs,kpts,cut=0.95):
    inds = np.flatnonzero(fs > 0.3)
    x = kpts[inds,0]
    y = kpts[inds,1]
    return x, y

# --------------------------------------------------------------------------------------------------

def plot_electrons(n,U,order):

    n *= 2.0

    fig, ax = plt.subplots(2,1,figsize=(4.5,8),height_ratios=[0.75,1],gridspec_kw={'hspace':0.1})

    # fig = plt.figure(figsize=(4.5,6))
    # gs = plt.GridSpec(1, 2, hspace = 0.1, wspace = 0.05)
    # ax0 = fig.add_subplot(gs[0])
    # ax1 = fig.add_subplot(gs[1])

    f = f'bands/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'
    with h5py.File(f,'r') as db:
        evals = db['eigenvalues'][...].squeeze() * conv
        dist = db['kpts_vert_distances'][...]
        ef = db['fermi_energy'][...] * conv
        # print(db.keys())
        # kpts = db['kpts_rlu'][...]

    num_kpts, num_spin = evals.shape

    dist /= dist.max()

    kpts = np.linspace(0,1,num_kpts)

    ax[0].plot(kpts,evals[...,0],c='r',lw=2)
    ax[0].plot(kpts,evals[...,1],c='b',lw=2)
    ax[0].axhline(ef,lw=0.75,ls='--',c='m')
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

        ef = db['fermi_energy'][...] * conv

    shape = fermi_surface.shape
    num_kpts = shape[0]
    num_bands = shape[1]
    num_spin = shape[2]

    fermi_surface = fermi_surface.squeeze()
    fermi_surface /= fermi_surface.max()

    print(np.nanmax(fermi_surface))

    x, y = get_points(fermi_surface[...,0],kpts) # spin up
    ax[1].scatter(x,y,s=0.5,c='r',alpha=0.75)

    x, y = get_points(fermi_surface[...,1],kpts) # spin down
    ax[1].scatter(x,y,s=0.5,c='b',alpha=0.75)

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

    calcs = [[0.01,   0, 'pm'],
            [ 0.10,   0, 'pm'],
            [ 0.20,   0, 'pm'],
            [ 0.25,   0, 'pm'],
            [ 0.30,   0, 'pm'],
            [ 0.40,   0, 'pm'],
            [ 0.50,   0, 'pm'],
            [ 0.01,  15, 'fm'],
            [ 0.10,  15, 'fm'],
            [ 0.20,  15, 'fm'],
            [ 0.25,  15, 'fm'],
            [ 0.30,  15, 'fm'],
            [ 0.40,  15, 'fm'],
            [ 0.45,  15, 'fm']]
    num_calcs = len(calcs)

    for calc in calcs:
        plot_electrons(*calc)