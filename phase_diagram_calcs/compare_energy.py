
import matplotlib.pyplot as plt
import h5py
import numpy as np
import os

from ref_data.hirsh import *
from ref_data.fleck import *


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

def _get_polaron_data(file_name):

    with h5py.File(file_name,'r') as db:
        polaron_0 = db['polaron_mft_energy_0'][...]
        polaron = db['polaron_mft_energy'][...]
        strain = db['distorted_crystal_energy'][...]

    return polaron #+polaron_0+strain

# --------------------------------------------------------------------------------------------------

def get_order(U,n,dir='scf_restart'):

    #print(U.round(3),n.round(3))

    energy = []
    order = []
    metal = []

    # get free calcs
    _free_dir = 'hubbard_phase_diagram/symm/scf_restart/'

    _c, _e, _o, _m = _get_data(_free_dir+f'afm_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(_free_dir+f'fm_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(_free_dir+f'fim_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    _fim = np.copy(_e) # DEV
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(_free_dir+f'pm_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(_free_dir+f'cdw_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _c:
        energy.append(_e); order.append(_o); metal.append(_m)

    # get polaron calcs
    _polaron_dir = 'hubbard_polaron_phase_diagram/no_symm/restart/'

    _c, _e, _o, _m = _get_data(_polaron_dir+f'electron_cdw_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _o == 'fim' or _o == 'cdw':
       _o += '_eph'
    if _c:
        _e += _get_polaron_data(_polaron_dir+f'polaron_cdw_U_{U:3.2f}_N_{n:3.2f}.hdf5')
        energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(_polaron_dir+f'electron_fim_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    if _o == 'fim' or _o == 'cdw':
       _o += '_eph'
    if _c:
        #print((_e-_fim).round(6))
        _e += _get_polaron_data(_polaron_dir+f'polaron_fim_U_{U:3.2f}_N_{n:3.2f}.hdf5')
        #print((_e-_fim).round(6),'\n')
        energy.append(_e); order.append(_o); metal.append(_m)

    # find the mininum
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


order = np.zeros(num_calcs,dtype=object) 
metal = np.zeros(num_calcs,dtype=int) # 0=insulator, 1=metal

for ii in range(num_calcs):

    U = U_arr[ii]; n = n_arr[ii]
    _o, _m = get_order(U,n)
    order[ii] = _o
    metal[ii] = _m

n_arr = n_arr/4

for _o in np.unique(order):

    marker = 'o'
    if _o == 'pm':
        c = (0,1,0)
    elif _o == 'afm':
        c = 'r'
    elif _o == 'fm':
        c = 'b'
    elif _o == 'fim':
        c = (1,0,1)
    elif _o == 'cdw':
        c = 'k'
    elif _o == 'fim_eph':
        c = (1,0,1)
        marker = '+'
    elif _o == 'cdw_eph':
        c = 'm'
        marker = '+'

    inds = np.flatnonzero(order == _o)
    _n = n_arr[inds]; _U = U_arr[inds]; _m = metal[inds]

    inds = np.flatnonzero(_m == 1) # metal
    ax.scatter(_n[inds],_U[inds],marker=marker,s=20,c=c,linewidths=1,
        clip_on=False)
    ax.scatter(1-_n[inds],_U[inds],marker=marker,s=20,c=c,linewidths=1,
        clip_on=False)

    inds = np.flatnonzero(_m == 0) # insulator
    ax.scatter(_n[inds],_U[inds],marker=marker,s=10,c='none',edgecolors=c,
        linewidths=1,clip_on=False)
    ax.scatter(1-_n[inds],_U[inds],marker=marker,s=10,c='none',edgecolors=c,
        linewidths=1,clip_on=False)

#ax.scatter(-1,-1,marker='o',s=25,c='r',linewidths=1,label='metal')
#ax.scatter(-1,-1,marker='o',s=10,c='none',edgecolors='r',linewidths=1,label='insulator')
#fig.legend(frameon=False,loc=1,bbox_to_anchor=(0.95,1.01))

# hirsh
x = np.array(para_to_mag['x'])/2
y = np.array(para_to_mag['y'])
ax.plot(1-x,y,lw=2,ls=(0,(4,1,2,1)),c='k')

x = np.array(ferro_to_afm['x'])/2
y = np.array(ferro_to_afm['y'])
ax.plot(1-x,y,lw=2,ls=(0,(4,1,2,1)),c='k')

# fleck
x = np.array(ferri['x'])
y = np.array(ferri['y'])
ax.plot(x,y,lw=2,ls=(0,(2,1)),c='k')
x = np.array(para['x'])
y = np.array(para['y'])
ax.plot(x,y,lw=2,ls=(0,(2,1)),c='k')




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

plt.savefig('hubbard_mft_phase_diagram_vs_polaron.pdf',bbox_inches='tight',dpi=300)
#plt.show()

