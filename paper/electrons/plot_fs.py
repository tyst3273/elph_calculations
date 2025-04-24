
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
        rlat_vecs = db['reciprocal_lattice_vectors'][...]   
        a = np.linalg.norm(rlat_vecs[0,:])
        b = np.linalg.norm(rlat_vecs[1,:])

    aspect = b/a
    aspect = 'auto'

    shape = fermi_surface.shape
    num_kpts = shape[0]
    num_bands = shape[1]
    num_spin = shape[2]

    # sum over bands
    fermi_surface = fermi_surface.sum(axis=(1)) 
    up = fermi_surface[:,0].reshape(kpts_mesh).squeeze()
    down = fermi_surface[:,1].reshape(kpts_mesh).squeeze()

    red = plt.cm.Reds
    red.set_under('w')
    blue = plt.cm.Blues
    blue.set_under('w')

    print(up.shape)

    fig, ax = plt.subplots(1,2,figsize=(8,3.5),clear=True,num=1)

    vmax = max(up.max(),down.max())*0.1
    vmin = 0.0
    if vmax <= vmin:
        vmin = vmax

    lw = 0.5
    ls = (0,(2,1,1,1))
    c = 'g'
    a = 0.25

    for xx in [-1,0,1]:
        for yy in [-1,0,1]:
            
            extent = [-0.5+xx,0.5+xx,-0.5+yy,0.5+yy]
            # extent = [-0.5,0.5,-0.5,0.5]

            ax[0].imshow(up.T,cmap=red,vmin=vmin,vmax=vmax,aspect=aspect,origin='lower',
                interpolation='none',extent=extent)
            ax[1].imshow(down.T,cmap=blue,vmin=vmin,vmax=vmax,aspect=aspect,origin='lower',
                interpolation='none',extent=extent)

            # ax[0].plot([xx+0.5,xx+0.5],[-1.5,1.5],lw=lw,ls=ls,c=c,ms=0,alpha=a)
            # ax[0].plot([xx-0.5,xx-0.5],[-1.5,1.5],lw=lw,ls=ls,c=c,ms=0,alpha=a)
            # ax[0].plot([-1.5,1.5],[yy+0.5,yy+0.5],lw=lw,ls=ls,c=c,ms=0,alpha=a)
            # ax[0].plot([-1.5,1.5],[yy-0.5,yy-0.5],lw=lw,ls=ls,c=c,ms=0,alpha=a)

            # ax[1].plot([xx+0.5,xx+0.5],[-1.5,1.5],lw=lw,ls=ls,c=c,ms=0,alpha=a)
            # ax[1].plot([xx-0.5,xx-0.5],[-1.5,1.5],lw=lw,ls=ls,c=c,ms=0,alpha=a)
            # ax[1].plot([-1.5,1.5],[yy+0.5,yy+0.5],lw=lw,ls=ls,c=c,ms=0,alpha=a)
            # ax[1].plot([-1.5,1.5],[yy-0.5,yy-0.5],lw=lw,ls=ls,c=c,ms=0,alpha=a)

    fig.suptitle(input_file)

    ax[0].axis([-0.75,0.75,-0.75,0.75])
    ax[1].axis([-0.75,0.75,-0.75,0.75])

    pdf = input_file.replace('hdf5','pdf')
    plt.savefig(pdf,dpi=100,bbox_inches='tight')

    plt.show()

    # plt.close()
    # plt.clf()

# --------------------------------------------------------------------------------------------------


# if len(sys.argv) > 1:
#     input_file = sys.argv[1]
# else:
#     input_file = 'electrons_out.hdf5'

input_files = os.listdir('nscf')
for input_file in input_files:
    if input_file.endswith('hdf5'):
        plot_fs(os.path.join('nscf',input_file))
