
import numpy as np
import matplotlib.pyplot as plt
import h5py 


density_file = 'scf_density.hdf5'

with h5py.File(density_file,'r') as db:

    nums = db['atom_type_nums'][...]

    cu_inds = np.flatnonzero(nums == 0)
    o_inds = np.flatnonzero(nums == 1)

    pos = db['atom_positions_cartesian'][...]

    density = db['site_density'][cu_inds]
    down = db['spin_down_site_density'][cu_inds]
    up = db['spin_up_site_density'][cu_inds]

fig, ax = plt.subplots(figsize=(6.5,6),gridspec_kw={'wspace':0.1})

# ------------------------------------------------------------------------------

xmax = pos[:,0].max(); xmin = pos[:,0].min()
ymax = pos[:,1].max(); ymin = pos[:,1].min()

# Cu atoms
cu_inds = np.flatnonzero(nums == 0)

# magnetisation density
mag = up-down
scale = 1000
im = ax.scatter(pos[cu_inds,0],pos[cu_inds,1],s=(density-density.min())*scale+50,cmap='bwr',
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

plt.show()

