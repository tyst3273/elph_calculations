
import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize
import sys

import colormaps
cmap = colormaps.amethyst
# cmap = plt.get_cmap('magma')
cmap.set_bad('k')
# cmap = 'jet'

# --------------------------------------------------------------------------------------------------

def get_nest(filename):
     
    with h5py.File(filename,'r') as db:
        band_resolved_nesting = db['nesting_function'][...]
        qpts_mesh = db['qpts_mesh'][...]

    shape = band_resolved_nesting.shape
    num_qpts = shape[0]
    num_bands = shape[1]

    qpts = np.arange(num_qpts)

    nesting = np.zeros(num_qpts)
    for ii in range(num_bands):
        for jj in range(num_bands):
            nesting[:] += band_resolved_nesting[:,ii,jj]

    nesting.shape = qpts_mesh

    return nesting

# --------------------------------------------------------------------------------------------------

fig = plt.figure(figsize=(4.5,7))
gs = plt.GridSpec(3, 2, hspace=0.1, wspace=0.2)

ax0 = fig.add_subplot(gs[0,0])
ax1 = fig.add_subplot(gs[0,1])

ax2 = fig.add_subplot(gs[1,0])
ax3 = fig.add_subplot(gs[1,1])

ax4 = fig.add_subplot(gs[2,0])
ax5 = fig.add_subplot(gs[2,1])

extent = [-0.5,0.5,-0.5,0.5]
norm = LogNorm(vmin=2e-2,vmax=1)


nesting = get_nest('N_0.05.hdf5')
ax0.imshow(nesting,cmap=cmap,norm=norm,aspect='auto',origin='lower',
        interpolation='nearest',extent=extent)

nesting = get_nest('N_0.50.hdf5')
ax1.imshow(nesting,cmap=cmap,norm=norm,aspect='auto',origin='lower',
        interpolation='nearest',extent=extent)

nesting = get_nest('N_0.70.hdf5')
ax2.imshow(nesting,cmap=cmap,norm=norm,aspect='auto',origin='lower',
        interpolation='nearest',extent=extent)

nesting = get_nest('N_0.80.hdf5')
ax3.imshow(nesting,cmap=cmap,norm=norm,aspect='auto',origin='lower',
        interpolation='nearest',extent=extent)

nesting = get_nest('N_0.90.hdf5')
ax4.imshow(nesting,cmap=cmap,norm=norm,aspect='auto',origin='lower',
        interpolation='nearest',extent=extent)

nesting = get_nest('N_1.00.hdf5')
im = ax5.imshow(nesting,cmap=cmap,norm=norm,aspect='auto',origin='lower',
        interpolation='nearest',extent=extent)

cbar = fig.colorbar(im,ax=[ax0,ax1,ax2,ax3,ax4,ax5],location='top',aspect=40,pad=0.025,extend='both')

# --------------------------------------------------------------------------------------------------

# ax[1].annotate('n=0.1',xycoords='data',textcoords='data',xy=(-0.45,0.45),xytext=(-0.075,0.0),
#             arrowprops=dict(arrowstyle='-|>',lw=1,color='k'),fontsize=10)
# ax[1].annotate('',xycoords='data',textcoords='data',xy=(0.41,0.41),xytext=(0.09,0.09),
#             arrowprops=dict(arrowstyle='->',lw=1,color='k'),fontsize=10)
# ax[1].annotate('n=0.05',xycoords='data',xy=(-0.05,0.025),fontsize=10,fontweight='bold')
# ax[1].annotate('n=0.50',xycoords='data',xy=(0.05,0.225),fontsize=10,fontweight='bold')
# ax[1].annotate('n=0.95',xycoords='data',xy=(0.325,0.435),fontsize=10,fontweight='bold')

# ax[1].plot(0.09,0.09,marker='o',ms=4,mec='k',mfc='k')
# ax[1].plot(0.41,0.41,marker='o',ms=4,mec='k',mfc='k')
# ax[1].plot(0.25,0.25,marker='o',ms=4,mec='k',mfc='k')

ticks = [-0.5,0.0,0.5]
for _ax in [ax0,ax1,ax2,ax3,ax4,ax5]:
    for axis in ['top','bottom','left','right']:
        _ax.spines[axis].set_linewidth(1.5)
    # _ax.minorticks_on()
    _ax.tick_params(which='both',width=1,labelsize=10)
    _ax.tick_params(which='major',length=5)
    _ax.tick_params(which='minor',length=2)
    _ax.set_rasterization_zorder = 1000000000
    _ax.set_xticks(ticks)
    _ax.set_yticks(ticks)

ax0.set_xticklabels([])
ax1.set_xticklabels([])
ax3.set_xticklabels([])
ax2.set_xticklabels([])
ax1.set_yticklabels([])
ax3.set_yticklabels([])
ax5.set_yticklabels([])

# ax.set_xticks(dist)
# ax[0].set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
# ax[0].axis([0,1,-1.5,1.5])

ax4.set_xlabel('h [rlu]',fontsize=12,labelpad=5)
ax5.set_xlabel('h [rlu]',fontsize=12,labelpad=5)

ax0.set_ylabel('k [rlu]',fontsize=12,labelpad=0)
ax2.set_ylabel('k [rlu]',fontsize=12,labelpad=0)
ax4.set_ylabel('k [rlu]',fontsize=12,labelpad=0)

# ax[1].axis([-0.5,0.5,-0.5,0.5])
# ax[1].set_xticks([-0.5,-0.25,0,0.25,0.5])
# ax[1].set_yticks([-0.5,-0.25,0,0.25,0.5])
# ax[1].set_ylabel('k [rlu]',fontsize=12,labelpad=5)
# ax[1].set_xlabel('h [rlu]',fontsize=12,labelpad=5)

c =(0.2,1.0,0.2)
ax0.annotate(f'(a)   n=0.025',xy=(0.15,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c=c)
ax1.annotate(f'(b)   n=0.25',xy=(0.15,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c=c)
ax2.annotate(f'(c)   n=0.35',xy=(0.15,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c=c)
ax3.annotate(f'(d)   n=0.40',xy=(0.15,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c=c)
ax4.annotate(f'(e)   n=0.45',xy=(0.15,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c=c)
ax5.annotate(f'(f)   n=0.50',xy=(0.15,0.9),xycoords='axes fraction',fontsize=10,annotation_clip=False,c=c)

plt.savefig('prim_nesting.png',dpi=300,bbox_inches='tight')
plt.show()