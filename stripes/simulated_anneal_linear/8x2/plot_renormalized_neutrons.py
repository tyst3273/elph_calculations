import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

import matplotlib as mpl

mpl.rc('text', usetex=True)
mpl.rcParams['text.latex.preamble'] = r"\usepackage{bm}"

# --------------------------------------------------------------------------------------------------

def get_specfun(energy,fwhm,freq):

    fwhm += 0.001

    sigma = fwhm/(2*np.sqrt(2*np.log(2)))
    b = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((energy-freq)/sigma)**2)

    return b

# --------------------------------------------------------------------------------------------------

def get_qpt_strs(qpts):
    qpt_strs = np.zeros(qpts.shape[0],dtype=object)
    for ii in range(qpts.shape[0]):
        _q = qpts[ii,:]
        qpt_strs[ii] = f'{_q[0]: 12.6f}, {_q[1]: 12.6f}, {_q[2]: 12.6f}'
    return qpt_strs

# --------------------------------------------------------------------------------------------------

def plot_renormalized_neutrons(renorm_file,show=True):

    fig, ax = plt.subplots(figsize=(6,6),clear=True)

    neutrons_file = 'neutrons.hdf5'
    with h5py.File(neutrons_file,'r') as db:
        form_factors = db['form_factors'][...]
        structure_factors = db['structure_factors'][...]
        freqs = db['frequencies'][...]
        qpts = np.abs(db['qpts_rlu'][...]).round(6)
        num_qpts = db['num_qpts'][...]
        if 'qpts_distances' in db.keys():
            qpts_dist = db['qpts_distances'][...]
            qpts_verts = db['qpts_vert_distances'][...]
            qpts_path = db['qpts_path'][...]

    qpts_verts /= qpts_dist.max()
    qpts_dist /= qpts_dist.max()

    with h5py.File(renorm_file,'r') as db:
        _freqs = db['frequencies'][...]
        renorm_freqs = db['renormalized_phonon_frequencies'][...]
        renorm_fwhm = db['phonon_fwhm'][...]
        renorm_qpts = np.abs(db['qpts_rlu'][...]).round(6)

    # qpts[:,0] = 0

    num_bands = freqs.shape[1]
    num_qpts = freqs.shape[0]

    qpts = get_qpt_strs(qpts)
    renorm_qpts = get_qpt_strs(renorm_qpts)

    energy = np.linspace(0,0.25,1000)

    # weight specfun by form factors
    renorm_sqw = np.zeros((energy.size,num_qpts),dtype=float)

    for ii in range(num_qpts):

        _ind = np.flatnonzero(renorm_qpts == qpts[ii])
        # print(_ind)

        if _ind.size == 0:
            continue
        
        for jj in range(num_bands):
            _specfun = get_specfun(energy,renorm_fwhm[_ind,jj],renorm_freqs[_ind,jj])
            renorm_sqw[:,ii] += _specfun*form_factors[ii,jj]

    #vmax = 2.5e-4 #0.025 #1.0
    vmax = np.nanmax(renorm_sqw)*0.125
    extent = [0,1,energy.min(),energy.max()]
    ax.imshow(renorm_sqw,cmap='hot',vmin=0,vmax=vmax,aspect='auto',origin='lower',
                interpolation='none',extent=extent)

    for ii in range(num_bands):
        ax.plot(qpts_dist,freqs[:,ii],marker='o',ms=0,c='g',lw=1,ls=(0,(2,1)),alpha=0.25)

    for v in qpts_verts:
        ax.plot([v,v],[0,energy.max()],ms=0,c=(0.5,0.5,0.5),lw=1,ls='--')

    #ax[0].axis([0,1,0,2.5])
    #ax.set_ylim([0,energy.max()])
    # ax.set_ylim(0.16,0.22)
    ax.set_xticks(qpts_verts)

    ticks = []
    for ii in range(qpts_verts.size):
        vert = qpts_path[ii]
        Q = f'({vert[0]:g},{vert[1]:g})'
        ticks.append(Q)

    ax.set_xticklabels(ticks)
    ax.set_ylabel(r'$\omega_{\bm{q}\nu}$',fontsize='x-large',rotation='horizontal',labelpad=15)

    # ax.set_title(specfun_file+'; '+mode)
    
    pdf = 'renormalized_neutrons.pdf'
    plt.savefig(pdf,dpi=100,bbox_inches='tight')

    if show:
        plt.show()

    plt.close()

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    plot_renormalized_neutrons('renormalization.hdf5',show=True)








