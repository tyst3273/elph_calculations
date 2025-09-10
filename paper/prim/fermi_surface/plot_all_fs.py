import numpy as np
import os
import h5py
import matplotlib.pyplot as plt
import sys

# --------------------------------------------------------------------------------------------------

def get_points(fs,kpts,cut=0.95):
    inds = np.flatnonzero(fs > 0.3)
    x = kpts[inds,0]
    y = kpts[inds,1]
    return x, y

# --------------------------------------------------------------------------------------------------


fig, ax = plt.subplots(2,1,figsize=(4.5,8),height_ratios=[0.75,1],gridspec_kw={'hspace':0.1})

f = 'bands.hdf5'
with h5py.File(f,'r') as db:
    evals = db['eigenvalues'][...].squeeze() * (3/8)
    dist = db['kpts_vert_distances'][...]
    # print(db.keys())
    # kpts = db['kpts_rlu'][...]

dist /= dist.max()

kpts = np.linspace(0,1,evals.size)
ax[0].plot(kpts,evals,c='k',lw=2)
for d in dist:
    ax[0].axvline(d,lw=0.5,ls=':',c=(0.25,0.25,0.25))


calcs = np.arange(0.1,2.0,0.1)
print(calcs)
colors = plt.get_cmap('managua')(np.linspace(0,1,len(calcs)))


for ii, n in enumerate(calcs):

    f = f'N_{n:3.2f}.hdf5'

    with h5py.File(f,'r') as db:
        fermi_surface = db['fermi_surface'][...]
        if not 'kpts_mesh' in db.keys():                
            exit('do calculation on mesh instead')
        kpts_mesh = db['kpts_mesh'][...]
        kpts = db['kpts_rlu'][...]

        ef = db['fermi_energy'][...]
    
    if n.round(3) in [0.1,1.9,1.0]:

        ax[0].axhline(ef*(3/8),ls='--',c='m',lw=0.75)
        ax[0].annotate(f'n={n/2:.2f}',xy=(0.125,ef*(3/8)+0.025),xycoords='data',fontsize=10,fontweight='bold')

    shape = fermi_surface.shape
    num_kpts = shape[0]
    num_bands = shape[1]
    num_spin = shape[2]


    fermi_surface = fermi_surface.squeeze()
    fermi_surface /= fermi_surface.max()
    x, y = get_points(fermi_surface,kpts)

    ax[1].scatter(x,y,s=0.5,c=colors[ii],alpha=0.75)
    # ax[1].scatter(x,y,s=0.5,c='k',alpha=0.72)


# ax[1].annotate('n=0.1',xycoords='data',textcoords='data',xy=(-0.45,0.45),xytext=(-0.075,0.0),
#             arrowprops=dict(arrowstyle='-|>',lw=1,color='k'),fontsize=10)
ax[1].annotate('',xycoords='data',textcoords='data',xy=(0.41,0.41),xytext=(0.09,0.09),
            arrowprops=dict(arrowstyle='->',lw=1,color='k'),fontsize=10)
ax[1].annotate('n=0.05',xycoords='data',xy=(-0.05,0.025),fontsize=10,fontweight='bold')
ax[1].annotate('n=0.50',xycoords='data',xy=(0.05,0.225),fontsize=10,fontweight='bold')
ax[1].annotate('n=0.95',xycoords='data',xy=(0.325,0.435),fontsize=10,fontweight='bold')

ax[1].plot(0.09,0.09,marker='o',ms=4,mec='k',mfc='k')
ax[1].plot(0.41,0.41,marker='o',ms=4,mec='k',mfc='k')
ax[1].plot(0.25,0.25,marker='o',ms=4,mec='k',mfc='k')

for _ax in ax:
    for axis in ['top','bottom','left','right']:
        _ax.spines[axis].set_linewidth(1.5)
    # _ax.minorticks_on()
    _ax.tick_params(which='both',width=1,labelsize=10,direction='in')
    _ax.tick_params(which='major',length=5)
    _ax.tick_params(which='minor',length=2)
    _ax.set_rasterization_zorder = 1000000000

ax[0].set_xticks(dist)
ax[0].set_xticklabels([r'$\Gamma$','X','M',r'$\Gamma$'])
ax[0].axis([0,1,-1.5,1.5])
# ax[0].set_xlabel('k [rlu]',fontsize=12,labelpad=5)
ax[0].set_ylabel('E [eV]',fontsize=12,labelpad=5)

ax[1].axis([-0.5,0.5,-0.5,0.5])
ax[1].set_xticks([-0.5,-0.25,0,0.25,0.5])
ax[1].set_yticks([-0.5,-0.25,0,0.25,0.5])
ax[1].set_ylabel('k [rlu]',fontsize=12,labelpad=5)
ax[1].set_xlabel('h [rlu]',fontsize=12,labelpad=5)

ax[0].annotate(f'(a)',xy=(-0.1,1.05),xycoords='axes fraction',fontsize=10,annotation_clip=False)
ax[1].annotate(f'(b)',xy=(-0.1,0.975),xycoords='axes fraction',fontsize=10,annotation_clip=False)

plt.savefig(f'prim_bands.png',dpi=300,bbox_inches='tight')
plt.show()
plt.close()



