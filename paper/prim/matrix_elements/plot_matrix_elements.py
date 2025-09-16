import numpy as np
import matplotlib.pyplot as plt
import h5py

e_scale = 3.0/8.0 * 1000

with h5py.File('matrix_elements.hdf5','r') as db:
    matrix_elements = db['elph_matrix_elements'][...].squeeze()
    freqs = db['frequencies'][...]* e_scale 
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

fig, ax = plt.subplots(figsize=(4.5,6))
            # gridspec_kw={'hspace':0.05,'wspace':0.1,'height_ratios':[0.75,1]})

g = -0.0025

for ii in range(num_modes):

    x = np.abs(xi[:,ii]) * e_scale * g
    hi = freqs[:,ii]+x
    lo = freqs[:,ii]-x

    ax.fill_between(qpts,lo,hi,color='m',alpha=0.5)
    # ax.errorbar(qpts,freqs[:,ii],x,marker='o',ms=0,c='m',elinewidth=1,alpha=0.25)

    ax.plot(qpts,hi,lw=1,ls='-',c='m')
    ax.plot(qpts,lo,lw=1,ls='-',c='m')
    ax.plot(qpts,freqs[:,ii],lw=1,ls='-',c='k')

    ax.fill_between(qpts,lo,hi,color='m',alpha=0.5)
    # ax.errorbar(qpts,freqs[:,ii],x,marker='o',ms=0,c='m',elinewidth=1,alpha=0.25)

    ax.plot(qpts,hi,lw=1,ls='-',c='m')
    ax.plot(qpts,lo,lw=1,ls='-',c='m')
    ax.plot(qpts,freqs[:,ii],lw=1,ls='-',c='k')

    # g = np.abs(matrix_elements[:,ii])**2*scale
    # hi = freqs[:,ii]+g
    # lo = freqs[:,ii]-g
    # ax.fill_between(qpts,lo,hi,color='b',alpha=0.5)

for v in verts:

    ax.axvline(v,lw=1,ls=(0,(2,1)),c=(0.25,0.25,0.25))
    ax.axvline(v,lw=1,ls=(0,(2,1)),c=(0.25,0.25,0.25))


for _ax in [ax]: #ax.ravel():
    for axis in ['top','bottom','left','right']:
        _ax.spines[axis].set_linewidth(1.5)
    _ax.minorticks_on()
    _ax.tick_params(which='both',width=1,labelsize=10)
    _ax.tick_params(which='major',length=5)
    _ax.tick_params(which='minor',length=2)
    _ax.set_rasterized = True

# ax.axis([0,1,0.0,80])

labels = [r'$\Gamma$','X','M',r'$\Gamma$']
ax.set_xticks(verts)
ax.set_xticklabels(labels)

ax.set_ylabel('Energy [meV]',fontsize=12,labelpad=5)

# plt.savefig(f'matrix_elements.png',dpi=300,bbox_inches='tight')
plt.show()
# plt.close()


