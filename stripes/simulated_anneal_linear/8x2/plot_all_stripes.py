
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import h5py 
import sys

# --------------------------------------------------------------------------------------------------

def read_file(density_file):

    with h5py.File(density_file,'r') as db:

        nums = db['atom_type_nums'][...]

        pos = db['atom_positions_cartesian'][...]

        density = db['site_density'][...]
        num_electrons = density.sum()

        down = db['spin_down_site_density'][...]
        up = db['spin_up_site_density'][...]

        mag = up-down
        magnetization = mag.sum()

        energy = db['ground_state_energy'][...]
        energy /= up.size

        gap = db['gap'][...]
        
        return nums, pos, density, down, up, energy, mag, num_electrons, gap, magnetization

# --------------------------------------------------------------------------------------------------

def read_dos(density_file):

    with h5py.File(density_file,'r') as db:

        density = db['site_density'][...]
        num_electrons = density.sum()
        num_atoms = density.size

        down = db['spin_down_site_density'][...]
        up = db['spin_up_site_density'][...]

        mag = up-down
        magnetization = mag.sum()

        energy = db['ground_state_energy'][...]
        energy /= up.size

        gap = db['gap'][...]

        fermi_energy = db['fermi_energy'][...]
        
        dos = db['dos'][...]
        dos_energy = db['dos_energy'][...]

        dos /= num_atoms

        return energy, num_electrons, gap, magnetization, fermi_energy, dos, dos_energy

# --------------------------------------------------------------------------------------------------

def plot_stripe(hdf5_file,fig,ax):
    
    nums, pos, density, down, up, energy, mag, num_electrons, gap, magnetization = \
        read_file(hdf5_file)

    xmax = pos[:,0].max(); xmin = pos[:,0].min()
    ymax = pos[:,1].max(); ymin = pos[:,1].min()

    # Cu atoms
    cu_inds = np.flatnonzero(nums == 0)

    density = density[cu_inds]
    up = up[cu_inds]
    down = down[cu_inds]

    # magnetisation density
    mag = up-down
    scale = 1000
    im = ax.scatter(pos[cu_inds,0],pos[cu_inds,1],s=(density-density.min())*scale+50,cmap='bwr',
        c=mag,alpha=1,edgecolors='k',linewidths=1.5,vmin=-1,vmax=1)
    fig.colorbar(im,extend='both',aspect=30,pad=0.025)

    # scale = 500
    # size = (density-density.min())*scale+50
    # im = ax.scatter(pos[:,0],pos[:,1],s=size,cmap='bwr',vmin=-1,vmax=1,
    #     c=mag,alpha=1,edgecolors='k',linewidths=1.5)
    # cbar = fig.colorbar(im,extend='both',aspect=30,pad=0.025)
    # cbar.ax.set_yticks([-1,0,1])

    # configure plots
    lims = [xmin-0.5,xmax+0.5,ymin-0.5,ymax+0.5]
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(1.5)
    ax.minorticks_on()
    ax.tick_params(which='both',width=1,labelsize='x-large')
    ax.tick_params(which='major',length=3)
    ax.tick_params(which='minor',length=1)
    ax.axis(lims)
    #ax.set_xticks(np.arange(0,n+1))
    #ax.set_yticks(np.arange(0,n+1))

    ax.set_xlabel('X [a]',labelpad=8,fontsize='x-large')
    ax.set_ylabel('Y [a]',labelpad=2,fontsize='x-large')

    ax.annotate(r'$E_{gs}$='+f'{energy:.6f}',xy=(0.1,1.05),xycoords='axes fraction',
                annotation_clip=False,fontsize='x-large')
    ax.annotate(r'$\Delta$='+f'{gap:.3f}',xy=(0.1,1.125),xycoords='axes fraction',
                annotation_clip=False,fontsize='x-large')
    ax.annotate(r'mag.='+f'{magnetization:.3f}',xy=(0.1,1.2),xycoords='axes fraction',
                annotation_clip=False,fontsize='x-large')

# --------------------------------------------------------------------------------------------------

def plot_dos(hdf5_file,fig,ax):
    
    # energy, num_electrons, gap, magnetization, fermi_energy, dos, dos_energy = \
    #     read_dos('prim/nscf_prim.hdf5')
    # ax.plot(dos[:,0],dos_energy,c='k',lw=1,ls=(0,(4,2,2,2)),ms=0)
    # ax.plot(-dos[:,1],dos_energy,c='k',lw=1,ls=(0,(4,2,2,2)),ms=0)

    # energy, num_electrons, gap, magnetization, fermi_energy, dos, dos_energy = \
    #     read_dos('afm/nscf_afm.hdf5')
    # ax.plot(dos[:,0],dos_energy,c='r',lw=1,ls=(0,(2,2)),ms=0)
    # ax.plot(-dos[:,1],dos_energy,c='b',lw=1,ls=(0,(2,2)),ms=0)

    energy, num_electrons, gap, magnetization, fermi_energy, dos, dos_energy = \
        read_dos(hdf5_file)
    ax.plot(dos[:,0],dos_energy,c='r',lw=1.5,ls='-',ms=0)
    ax.plot(-dos[:,1],dos_energy,c='b',lw=1.5,ls='-',ms=0)

    ax.plot([-0.5,0.5],[fermi_energy,fermi_energy],lw=1,ls='--',c='k')
    ax.plot([0],[fermi_energy],ms=4,marker='o',mew=1,c='k')

    ax.fill_betweenx(dos_energy,dos[:,0],x2=-dos[:,1],color='m',alpha=0.25)

    xlim = dos.max()
    ymin = dos_energy.min()
    ymax = dos_energy.max()

    # configure plots
    lims = [-0.5,0.5,ymin-0.1,ymax+0.1]
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(1.5)
    ax.minorticks_on()
    ax.tick_params(which='both',width=1,labelsize='x-large')
    ax.tick_params(which='major',length=3)
    ax.tick_params(which='minor',length=1)
    ax.axis(lims)
    #ax.set_xticks(np.arange(0,n+1))
    #ax.set_yticks(np.arange(0,n+1))

    ax.set_xlabel('DoS [arb. units]',labelpad=8,fontsize='x-large')
    ax.set_ylabel('Energy [t]',labelpad=-5,fontsize='x-large')

    ax.annotate(r'$E_{gs}$='+f'{energy:.6f}',xy=(0.1,1.05),xycoords='axes fraction',
                annotation_clip=False,fontsize='x-large')
    ax.annotate(r'$\Delta$='+f'{gap:.3f}',xy=(0.1,1.125),xycoords='axes fraction',
                annotation_clip=False,fontsize='x-large')
    ax.annotate(r'mag.='+f'{magnetization:.3f}',xy=(0.1,1.2),xycoords='axes fraction',
                annotation_clip=False,fontsize='x-large')

# --------------------------------------------------------------------------------------------------

if len(sys.argv) > 1:
    hdf5_file = sys.argv[1]
else:
    hdf5_file = 'restart_n_8_h_0.2500.hdf5' 

fig, ax = plt.subplots(1,2,figsize=(8,4.25),clear=True,
                    gridspec_kw={'wspace':0.2,'width_ratios':[1,0.5]})

# plot stripe order, ground state energy, magnetization, and gap

plot_stripe(hdf5_file,fig,ax[0])
plot_dos(hdf5_file,fig,ax[1])

plt.savefig(hdf5_file.replace('.hdf5','.pdf'),bbox_inches='tight',dpi=200)
plt.show()
plt.close()
plt.clf()




# ------------------------------------------------------------------------------

