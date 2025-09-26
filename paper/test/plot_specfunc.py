
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

import sys

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

    qpts_verts /= qpts_verts.max()
    qpts = qpts_dist / qpts_dist.max()

    spec_func = get_specfun(energy,freqs,real,imag,adiabatic,1e-5)
    spec_func = spec_func.sum(axis=-1) # sum over spins ?
    spec_func /= spec_func.max()

    energy *= conv
    freqs *= conv
    new_freqs *= conv
    fwhm *= conv

    return spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts

# --------------------------------------------------------------------------------------------------

def plot_specfunc(filename):

    fig, ax = plt.subplots(figsize=(4.5,3))

    vmin = 1e-5
    vmax = 0.01
    c = (1.0,0.0,0.0)

    # -------------------

    spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data(filename)

    norm = LogNorm(vmin=vmin,vmax=vmax)
    extent = [0,1,energy.min(),energy.max()]
    ax.imshow(spec_func,cmap=cmap,norm=norm,aspect='auto',origin='lower',
                interpolation='none',extent=extent)    

    for v in qpts_verts:
        ax.axvline(v,lw=0.5,ls=':',c='w')

    num_bands = freqs.shape[1]
    for ii in range(num_bands):

        # hi = new_freqs+fwhm/2
        # lo = new_freqs-fwhm/2
        # ax.fill_between(qpts,hi[:,ii],lo[:,ii],color='g',alpha=0.25)
        # ax.plot(qpts,new_freqs[:,ii],marker='o',ms=0,c='g',lw=0.75,ls='-')

        ax.plot(qpts,freqs[:,ii],marker='o',ms=0,c='m',lw=0.5,ls='-')

    # -------------------
    # plot primitve cell results

    # spec_func, energy, freqs, new_freqs, fwhm, qpts, qpts_verts = get_data('prim/elph_out.hdf5')

    # for v in qpts_verts:
    #     ax.axvline(v,lw=0.5,ls=':',c='w')

    # num_bands = freqs.shape[1]
    # for ii in range(num_bands):

    #     hi = new_freqs+fwhm/2
    #     lo = new_freqs-fwhm/2
    #     ax.fill_between(qpts,hi[:,ii],lo[:,ii],color='g',alpha=0.25)
    #     ax.plot(qpts,new_freqs[:,ii],marker='o',ms=0,c='g',lw=0.75,ls='-')

    #     ax.plot(qpts,freqs[:,ii],marker='o',ms=0,c='m',lw=0.5,ls='-')

    # ---------------------------

    for _ax in [ax]:
        for axis in ['top','bottom','left','right']:
            _ax.spines[axis].set_linewidth(1.5)
        # _ax.minorticks_on()
        _ax.tick_params(which='both',width=1,labelsize=10) #,direction='in')
        _ax.tick_params(which='major',length=5)
        _ax.tick_params(which='minor',length=2)
        _ax.set_rasterization_zorder = 1000000000

    ax.axis([0,1,62,80])
    # ax.set_xticks(qpts_verts)
    # ax.set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
    ax.set_ylabel('Energy [meV]',fontsize=10,labelpad=5)

    ax.set_title(filename)

    pdf = filename.replace('.hdf5','.pdf')
    plt.savefig(pdf,dpi=300,bbox_inches='tight')
    plt.show()
    plt.close()

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    if len(sys.argv) != 1:
        filename = sys.argv[1]
    else:
        filename = 'nk_50.hdf5'

    plot_specfunc(filename)
    

