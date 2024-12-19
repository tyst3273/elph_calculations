
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

def plot_stripe(path,doping,n,fig,ax):
    
    nums, pos, density, down, up, energy, mag, num_electrons, gap, magnetization = \
        read_file(path)

    xmax = pos[:,0].max(); xmin = pos[:,0].min()
    ymax = pos[:,1].max(); ymin = pos[:,1].min()

    # magnetisation density
    scale = 500
    size = (density-density.min())*scale+50

    im = ax.scatter(pos[:,0],pos[:,1],s=size,cmap='bwr',vmin=-1,vmax=1,
        c=mag,alpha=1,edgecolors='k',linewidths=1.5)
    fig.colorbar(im,extend='both',aspect=30,pad=0.025)

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

if len(sys.argv) > 1:
    doping = float(sys.argv[1])
else:
    doping = 0.0625

doping_dir = f'{doping:.4f}'

# get all unitcell sizes for this doping
_sc_dirs = ['4x4','6x6','8x8','16x16']
sc_dirs = []
for _sc_dir in _sc_dirs:
    n = _sc_dir.split('x')[0]
    _path = os.path.join(_sc_dir,doping_dir,f'restart_n_{n}_h_{doping_dir}.hdf5')
    if not os.path.exists(_path):
        continue
    sc_dirs.append(_sc_dir)

print(sc_dirs)

num_dirs = len(sc_dirs)

with PdfPages(f'h_{doping_dir}_results.pdf') as pdf:
    
    for _sc_dir in sc_dirs:
        
        n = int(_sc_dir.split('x')[0])

        fig, ax = plt.subplots(1,2,figsize=(8,4.25),clear=True,
                            gridspec_kw={'wspace':0.2,'width_ratios':[1,0.5]})

        # plot stripe order, ground state energy, magnetization, and gap
        _path = os.path.join(_sc_dir,doping_dir,f'restart_n_{n}_h_{doping_dir}.hdf5')
        plot_stripe(_path,doping_dir,n,fig,ax[0])

        # plot density of states, magnetization, and gap
#        plt.show()

        pdf.savefig(fig,bbox_inches='tight',dpi=200)

        plt.close()
        plt.clf()




# ------------------------------------------------------------------------------

