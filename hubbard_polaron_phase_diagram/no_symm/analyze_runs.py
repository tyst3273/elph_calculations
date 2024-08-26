
import matplotlib.pyplot as plt
import h5py
import numpy as np
import os


# --------------------------------------------------------------------------------------------------

def _get_data(file_name):

    with h5py.File(file_name,'r') as db:
        free_energy = db['free_energy'][...]
        gs_energy = db['ground_state_energy'][...]
        metal = db['is_metal'][...].astype(int)
        up = db['spin_up_site_density'][...]
        down = db['spin_down_site_density'][...]
        converged = db['converged_electron_scf'][...]

    mag = (up-down).round(4)
    if np.all(mag == 0.0):
        order = 'pm'
    elif mag[0] == -mag[1]:
        order = 'afm'
    elif mag[0] == mag[1]:
        order = 'fm'
    else:
        order = 'fim'

    return converged, free_energy, order, metal

# --------------------------------------------------------------------------------------------------

def get_order(U,n,dir='scf_restart'):

    energy = []
    order = []
    metal = []

    _c, _e, _o, _m = _get_data(dir+'/'+f'afm_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'fm_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'fim_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'pm_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'cdw_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    ind = np.argmin(np.array(energy))
    order = order[ind]; metal = metal[ind]

    return order, metal

# --------------------------------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(4,4))


# parameters to sweep
U_arr = np.linspace(0,20,41)
n_arr = np.linspace(0,2,21)[1:]

print('\nU_arr:\n',U_arr)
print('\nn_arr:\n',n_arr)

n_arr, U_arr = np.meshgrid(n_arr,U_arr,indexing='ij')
n_arr = n_arr.flatten(); U_arr = U_arr.flatten()
num_calcs = n_arr.size


order = np.zeros(num_calcs,dtype=int) # 0=afm, 1=fm, 2=pm, 3=fim, 4=cdw
metal = np.zeros(num_calcs,dtype=int) # 0=insulator, 1=metal

for ii in range(num_calcs):

    U = U_arr[ii]; n = n_arr[ii]
    _o, _m = get_order(U,n)

    if _o == 'afm':
        _o = 0
    elif _o == 'fm':
        _o = 1
    elif _o == 'pm':
        _o = 2
    elif _o == 'fim':
        _o = 3
    else: 
        _o == 4

    metal[ii] = _m
    order[ii] = _o

n_arr = n_arr/4
c = np.zeros((num_calcs,3),dtype=float)
c[np.flatnonzero(order == 2),1] = 1.0 # pm
c[np.flatnonzero(order == 0),0] = 1.0 # afm
c[np.flatnonzero(order == 1),2] = 1.0 # fm
c[np.flatnonzero(order == 3),0] = 1.0 # fim 
c[np.flatnonzero(order == 3),2] = 1.0 # fim

markers = np.ones(num_calcs,dtype='str')
markers[np.flatnonzero(order == 0)] = 'o'
markers[np.flatnonzero(order == 1)] = '^'
markers[np.flatnonzero(order == 2)] = 's'
markers[np.flatnonzero(order == 3)] = 'd'

markers = ['o','^','*','d']
markers = ['o','o','o','o']

for ii in range(4):
    inds = np.flatnonzero(order == ii)
    _n = n_arr[inds]; _U = U_arr[inds]; _c = c[inds]; _m = metal[inds]

    inds = np.flatnonzero(_m == 1)
    ax.scatter(_n[inds],_U[inds],marker=markers[ii],s=20,c=_c[inds],linewidths=1,
        clip_on=False)
    ax.scatter(1-_n[inds],_U[inds],marker=markers[ii],s=20,c=_c[inds],linewidths=1,
        clip_on=False)

    inds = np.flatnonzero(_m == 0)
    ax.scatter(_n[inds],_U[inds],marker=markers[ii],s=10,c='none',edgecolors=_c[inds],
        linewidths=1,clip_on=False)
    ax.scatter(1-_n[inds],_U[inds],marker=markers[ii],s=10,c='none',edgecolors=_c[inds],
        linewidths=1,clip_on=False)

#ax.scatter(-1,-1,marker='o',s=25,c='r',linewidths=1,label='metal')
#ax.scatter(-1,-1,marker='o',s=10,c='none',edgecolors='r',linewidths=1,label='insulator')
#fig.legend(frameon=False,loc=1,bbox_to_anchor=(0.95,1.01))

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.1)
ax.minorticks_on()
ax.tick_params(which='both',width=1,labelsize='medium')
ax.tick_params(which='major',length=5)
ax.tick_params(which='minor',length=2)
ax.set_rasterized = True

ax.axis([0.0,1.0,0.0,20])
ax.set_xlabel('filling fraction',fontsize='large',labelpad=8)
ax.set_ylabel('U/t',fontsize='large',rotation='horizontal',labelpad=15)

ax.set_xticks(np.linspace(0,1,11))
ax.set_yticks(np.linspace(0,20,11))

"""
ax.annotate('PM',xycoords='data',xy=(0.175,3.5),fontsize='xx-large',fontweight='bold')
ax.annotate('PM',xycoords='data',xy=(0.8,3.5),fontsize='xx-large',fontweight='bold')
ax.annotate('AFM',xycoords='data',xy=(0.44,3.5),fontsize='xx-large',fontweight='bold')
ax.annotate('FM',xycoords='data',xy=(0.15,16),fontsize='xx-large',fontweight='bold')
ax.annotate('FM',xycoords='data',xy=(0.8,16),fontsize='xx-large',fontweight='bold')
ax.annotate('FiM',xycoords='data',xy=(0.32,12),fontsize='xx-large',fontweight='bold')
ax.annotate('FiM',xycoords='data',xy=(0.58,12),fontsize='xx-large',fontweight='bold')
"""

plt.savefig('hubbard_mft_phase_diagram.pdf',bbox_inches='tight',dpi=300)
#plt.show()

