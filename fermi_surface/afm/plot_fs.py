import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

# --------------------------------------------------------------------------------------------------

def plot_fs(input_file):

    with h5py.File(input_file,'r') as db:
            fermi_surface = db['fermi_surface'][...]
            if not 'kpts_mesh' in db.keys():
                exit('do calculation on mesh instead')
            kpts_mesh = db['kpts_mesh'][...]

    shape = fermi_surface.shape
    num_kpts = shape[0]
    num_bands = shape[1]
    num_spin = shape[2]

    # sum over bands
    fermi_surface = fermi_surface.sum(axis=(1,2)) 
    fermi_surface.shape = kpts_mesh

    fig, ax = plt.subplots(figsize=(4,4))

    extent = [0,1,0,1]
    vmax = fermi_surface.max()*0.1

    for xx in [-1,0,1]:
        for yy in [-1,0,1]:
            
            extent = [-0.5+xx,0.5+xx,-0.5+yy,0.5+yy]
            ax.imshow(fermi_surface,cmap='Greys',vmin=0,vmax=vmax,aspect='auto',origin='lower',
                interpolation='none',extent=extent)

            ax.plot([xx+0.5,xx+0.5],[-1.5,1.5],lw=1,ls='--',c='g',ms=0)
            ax.plot([xx-0.5,xx-0.5],[-1.5,1.5],lw=1,ls='--',c='g',ms=0)
            ax.plot([-1.5,1.5],[yy+0.5,yy+0.5],lw=1,ls='--',c='g',ms=0)
            ax.plot([-1.5,1.5],[yy-0.5,yy-0.5],lw=1,ls='--',c='g',ms=0)

    fig.suptitle(input_file)

    pdf = input_file.replace('hdf5','pdf')
    plt.savefig(pdf,dpi=100,bbox_inches='tight')

#    plt.show()

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'electrons_out.hdf5'

    plot_fs(input_file)


