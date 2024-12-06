import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

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
 
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'renormalization.hdf5'

with h5py.File(input_file,'r') as db:
        real = db['phonon_self_energy_real'][...].squeeze()
        imag = db['phonon_self_energy_imag'][...].squeeze()
        adiabatic = db['phonon_self_energy_adiabatic'][...].squeeze()
        energy = db['phonon_self_energy_energy'][...]
        freqs = db['frequencies'][...]
        new_freqs = db['renormalized_phonon_frequencies'][...]
        fwhm = db['phonon_fwhm'][...]
        qpts = db['qpts_rlu'][...]
        if 'qpts_distances' in db.keys():
            qpts_dist = db['qpts_distances'][...]
            qpts_verts = db['qpts_vert_distances'][...]

num_bands = freqs.shape[1]
num_qpts = freqs.shape[0]
qpts = np.arange(num_qpts)

fig, ax = plt.subplots(figsize=(6,8))

spec_func = get_specfun(energy,freqs,real,imag,adiabatic,1e-4)
spec_func = spec_func.sum(axis=-1)

if spec_func.ndim == 1:

    ax.plot(energy,spec_func,marker='o',ms=0,c='k',lw=1,mfc='none')
    ax.set_xlabel('Energy [t]')
    ax.set_ylabel('spectral function ?')

    _max = spec_func.max()
    freqs = freqs.squeeze()
    for ii in range(num_bands):
        ax.plot([freqs[ii],freqs[ii]],[0,_max],c='m',lw=1,ls='--')
        #ax.plot(qpts,-freqs[:,ii],marker='o',ms=2,c='k',lw=1,ls='-')

else:

    qpts_verts /= qpts_dist.max()
    qpts_dist /= qpts_dist.max()

    vmax = spec_func.max()*0.05 #0.025 #1.0
    extent = [0,1,energy.min(),energy.max()]
    ax.imshow(spec_func,cmap='magma',vmin=0,vmax=vmax,aspect='auto',origin='lower',
              interpolation='none',extent=extent)
    #ax.imshow(spec_func,cmap='bwr',vmin=-vmax,vmax=vmax,aspect='auto',origin='lower',
    #          interpolation='none',extent=extent)

    for ii in range(num_bands):

        ax.plot(qpts_dist,freqs[:,ii],marker='o',ms=0,c='g',lw=1,ls=(0,(2,1)))

        hi = new_freqs[:,ii]+fwhm[:,ii]/2
        lo = new_freqs[:,ii]-fwhm[:,ii]/2
        ax.plot(qpts_dist,new_freqs[:,ii],marker='o',ms=0,c='g',lw=1,ls='-')
        ax.plot(qpts_dist,hi,marker='o',ms=0,c='g',lw=1,ls='-')
        ax.plot(qpts_dist,lo,marker='o',ms=0,c='g',lw=1,ls='-')
        ax.fill_between(qpts_dist,lo,hi,color='g',alpha=0.5,linewidth=0)

    for v in qpts_verts:
        ax.plot([v,v],[0,energy.max()],ms=0,c=(0.5,0.5,0.5),lw=0.5,ls='--')

    ax.set_xlabel('qpts...')
    ax.set_ylabel('Energy [t]')
    ax.axis([0,1,0,energy.max()])
    #ax.axis([0,1,0.16,0.22])

ax.set_title(input_file)
plt.show()
