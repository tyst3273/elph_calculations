import numpy as np
import matplotlib.pyplot as plt
import h5py
import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'matelem.hdf5'

with h5py.File(input_file,'r') as db:
    matrix_elements = db['elph_matrix_elements'][...].squeeze()
    freqs = db['frequencies'][...]
    xi = db['coupled_orbital_area_modulation'][...].squeeze()
    qpts_rlu = db['qpts_rlu'][...]

num_kpts = matrix_elements.shape[0]
matrix_elements = matrix_elements.sum(axis=(0,2,3,5))/num_kpts
xi = xi.sum(axis=2)

num_qpts = freqs.shape[0]
num_modes = freqs.shape[1]
qpts = np.linspace(0,1,qpts_rlu.shape[0])

fig, ax = plt.subplots(1,3,figsize=(16,4))


for ii in range(num_modes-4,num_modes): 

    ax[0].plot(qpts,freqs[:,ii],lw=1,ls='-',c='k')
    ax[1].plot(qpts,freqs[:,ii],lw=1,ls='-',c='k')
    ax[2].plot(qpts,freqs[:,ii],lw=1,ls='-',c='k')  

    # ----------------------------------------------

    x = xi[:,ii].real * 0.001
    hi = freqs[:,ii]+np.abs(x)
    lo = freqs[:,ii]-np.abs(x)
    ax[0].fill_between(qpts,lo,hi,color='k',alpha=0.25)
    inds = np.flatnonzero( x <= 0 )
    ax[0].errorbar(qpts[inds],freqs[inds,ii],np.abs(x[inds]),
                   marker='o',ms=0,c='r',elinewidth=2,lw=0)
    inds = np.flatnonzero( x > 0 )
    ax[0].errorbar(qpts[inds],freqs[inds,ii],np.abs(x[inds]),
                   marker='o',ms=0,c='b',elinewidth=2,lw=0)

    x = xi[:,ii].imag * 0.001
    hi = freqs[:,ii]+np.abs(x)
    lo = freqs[:,ii]-np.abs(x)
    ax[1].fill_between(qpts,lo,hi,color='k',alpha=0.25)
    inds = np.flatnonzero( x <= 0 )
    ax[1].errorbar(qpts[inds],freqs[inds,ii],np.abs(x[inds]),
                   marker='o',ms=0,c='r',elinewidth=2,lw=0)
    inds = np.flatnonzero( x > 0 )
    ax[1].errorbar(qpts[inds],freqs[inds,ii],np.abs(x[inds]),
                   marker='o',ms=0,c='b',elinewidth=2,lw=0)
    
    x = np.abs(xi[:,ii]) * 0.001
    hi = freqs[:,ii]+x
    lo = freqs[:,ii]-x
    ax[2].fill_between(qpts,lo,hi,color='k',alpha=0.25)
    ax[2].errorbar(qpts,freqs[:,ii],x,marker='o',ms=0,c='k',elinewidth=1)

    # ----------------------------------------------

    # g = matrix_elements[:,ii].real * 0.025
    # hi = freqs[:,ii]+np.abs(g)
    # lo = freqs[:,ii]-np.abs(g)
    # ax[0].fill_between(qpts,lo,hi,color='k',alpha=0.25)
    # inds = np.flatnonzero( g <= 0 )
    # ax[0].errorbar(qpts[inds],freqs[inds,ii],np.abs(g[inds]),
    #                marker='o',ms=0,c='r',elinewidth=2,lw=0)
    # inds = np.flatnonzero( g > 0 )
    # ax[0].errorbar(qpts[inds],freqs[inds,ii],np.abs(g[inds]),
    #                marker='o',ms=0,c='b',elinewidth=2,lw=0)

    # g = matrix_elements[:,ii].imag * 0.025
    # hi = freqs[:,ii]+np.abs(g)
    # lo = freqs[:,ii]-np.abs(g)
    # ax[1].fill_between(qpts,lo,hi,color='k',alpha=0.25)
    # inds = np.flatnonzero( g <= 0 )
    # ax[1].errorbar(qpts[inds],freqs[inds,ii],np.abs(g[inds]),
    #                marker='o',ms=0,c='r',elinewidth=2,lw=0)
    # inds = np.flatnonzero( g > 0 )
    # ax[1].errorbar(qpts[inds],freqs[inds,ii],np.abs(g[inds]),
    #                marker='o',ms=0,c='b',elinewidth=2,lw=0)
    

    # g = np.abs(matrix_elements[:,ii]) * 0.025
    # hi = freqs[:,ii]+g
    # lo = freqs[:,ii]-g
    # ax[2].fill_between(qpts,lo,hi,color='k',alpha=0.25)
    # ax[2].errorbar(qpts,freqs[:,ii],g,marker='o',ms=0,c='k',elinewidth=2,lw=0)

plt.show()


