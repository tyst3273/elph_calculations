
import numpy as np
import matplotlib.pyplot as plt
import h5py 


polaron_file = 'polaron.hdf5'

with h5py.File(polaron_file,'r') as db:

    disp = db['mft_polaron_displacements'][...]
    pos = db['atom_positions_cartesian'][...]
    nums = db['atom_type_nums'][...]

    density = db['site_density'][...]
    down = db['spin_down_site_density'][...]
    up = db['spin_up_site_density'][...]

fig, ax = plt.subplots(figsize=(10,10))

# plot the spin density
#scale = 800
#ax.scatter(pos[:,0]+disp[:,0],pos[:,1]+disp[:,1],s=up*scale,c='r',edgecolors='none',alpha=0.5)
#ax.scatter(pos[:,0]+disp[:,0],pos[:,1]+disp[:,1],s=down*scale,c='b',edgecolors='none',alpha=0.5)

scale = 2500
inds = np.flatnonzero(nums == 0)
delta = np.abs(density[inds]-density[inds].max())
spins = up[inds]-down[inds]

# plot the undisplaced sites
inds = np.flatnonzero(nums == 0)
ax.scatter(pos[inds,0],pos[inds,1],s=60,c='none',edgecolors='k')
ax.scatter(pos[inds,0]+disp[inds,0],pos[inds,1]+disp[inds,1],
            s=40+(delta*scale),c=spins,cmap='bwr',edgecolors='k')

inds = np.flatnonzero(nums == 1)
ax.scatter(pos[inds,0],pos[inds,1],s=20,c='none',edgecolors='k')
ax.scatter(pos[inds,0]+disp[inds,0],pos[inds,1]+disp[inds,1],
            s=20,c='b',edgecolors='k')

ax.quiver(pos[:,0],pos[:,1],disp[:,0],disp[:,1],angles='xy',scale_units='xy',scale=1)

plt.savefig('polaron.pdf',dpi=300,bbox_inches='tight')
#plt.show()

