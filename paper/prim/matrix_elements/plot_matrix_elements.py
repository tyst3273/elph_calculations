import numpy as np
import matplotlib.pyplot as plt
import h5py

e_scale = 3.0/8.0

with h5py.File('matrix_elements.hdf5','r') as db:
    matrix_elements = db['elph_matrix_elements'][...].squeeze()
    freqs = db['frequencies'][...]*e_scale*1000
    xi = db['coupled_orbital_area_modulation'][...].squeeze()
    qpts_rlu = db['qpts_rlu'][...]
    if 'qpts_distances' in db.keys():
        verts = db['qpts_vert_distances'][...]
        dists = db['qpts_distances'][...]

num_kpts = matrix_elements.shape[0]
matrix_elements = matrix_elements.sum(axis=(0,-1))/num_kpts

num_qpts = freqs.shape[0]
num_modes = freqs.shape[1]
# qpts = np.linspace(0,1,qpts_rlu.shape[0])
qpts = dists/dists.max()
verts = verts/dists.max()

fig, ax = plt.subplots(2,1,figsize=(4.5,6),
            gridspec_kw={'hspace':0.05,'wspace':0.1,'height_ratios':[0.75,1]})

scale = 0.25

for ii in range(num_modes):

    x = np.abs(xi[:,ii])*scale
    hi = freqs[:,ii]+x
    lo = freqs[:,ii]-x

    ax[0].fill_between(qpts,lo,hi,color='m',alpha=0.5)
    # ax.errorbar(qpts,freqs[:,ii],x,marker='o',ms=0,c='m',elinewidth=1,alpha=0.25)

    ax[0].plot(qpts,hi,lw=1,ls='-',c='m')
    ax[0].plot(qpts,lo,lw=1,ls='-',c='m')
    ax[0].plot(qpts,freqs[:,ii],lw=1,ls='-',c='k')

    ax[1].fill_between(qpts,lo,hi,color='m',alpha=0.5)
    # ax.errorbar(qpts,freqs[:,ii],x,marker='o',ms=0,c='m',elinewidth=1,alpha=0.25)

    ax[1].plot(qpts,hi,lw=1,ls='-',c='m')
    ax[1].plot(qpts,lo,lw=1,ls='-',c='m')
    ax[1].plot(qpts,freqs[:,ii],lw=1,ls='-',c='k')

    # g = np.abs(matrix_elements[:,ii])**2*scale
    # hi = freqs[:,ii]+g
    # lo = freqs[:,ii]-g
    # ax.fill_between(qpts,lo,hi,color='b',alpha=0.5)

for v in verts:

    ax[0].axvline(v,lw=1,ls=(0,(2,1)),c=(0.25,0.25,0.25))
    ax[1].axvline(v,lw=1,ls=(0,(2,1)),c=(0.25,0.25,0.25))


for _ax in ax.ravel():
    for axis in ['top','bottom','left','right']:
        _ax.spines[axis].set_linewidth(1.5)
    _ax.minorticks_on()
    _ax.tick_params(which='both',width=1,labelsize=10)
    _ax.tick_params(which='major',length=5)
    _ax.tick_params(which='minor',length=2)
    _ax.set_rasterized = True



ax[0].axis([0,1,64,77])
ax[1].axis([0,1,0.0,35])

labels = [r'$\Gamma$','X','M',r'$\Gamma$']
ax[0].set_xticks(verts)
ax[0].set_xticklabels([])
ax[1].set_xticks(verts)
ax[1].set_xticklabels(labels)

ax[1].set_ylabel('Energy [meV]',fontsize=12,labelpad=5)
ax[0].set_ylabel('Energy [meV]',fontsize=12,labelpad=5)

# ax.set_title(r'(0,1+$\xi$,0)',fontsize=12)
# ax.set_title(r'(H+$\xi$,0,0)',fontsize=12)

# ax[1].set_xlabel('Energy [meV]',fontsize=12)

plt.savefig(f'matrix_elements.png',dpi=300,bbox_inches='tight')
plt.show()
# plt.close()


