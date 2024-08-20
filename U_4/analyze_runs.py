
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

def get_data(n,dir='scf'):

    energy = []
    order = []
    metal = []

    _c, _e, _o, _m = _get_data(dir+'/'+f'afm_N_{n:3.2f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'fm_N_{n:3.2f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'fim_N_{n:3.2f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'pm_N_{n:3.2f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'cdw_N_{n:3.2f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    #ind = np.argmin(np.array(energy))
    #order = order[ind]; metal = metal[ind]
    
    return energy

# --------------------------------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(4,4))

# parameters to sweep
n_arr = np.linspace(0.25,0.75,41)*4
num_calcs = n_arr.size
print('\nn_arr:\n',n_arr)

order = np.zeros(num_calcs,dtype=int) # 0=afm, 1=fm, 2=pm, 3=fim, 4=cdw
metal = np.zeros(num_calcs,dtype=int) # 0=insulator, 1=metal
energy = np.zeros((num_calcs,5),dtype=float)

for ii in range(num_calcs):

    n = n_arr[ii]

    try:
        energy[ii,:] = get_data(n)
    except:
        continue

n_arr = n_arr/4

# afm, fm, fim, pm, cdw
c = ['r','b','m','g','k']
m = ['o','^','*','d','+']

for ii in range(5):
    ax.plot(n_arr,energy[:,ii],marker=m[ii],ms=4,c=c[ii],lw=1,clip_on=False)

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

#ax.axis([0.0,1.0,0.0,20])
ax.set_xlabel('filling fraction',fontsize='large',labelpad=8)
ax.set_ylabel('Free energy [t]',fontsize='large',labelpad=8)

#ax.set_xticks(np.linspace(0,1,11))
#ax.set_yticks(np.linspace(0,20,11))

"""
ax.annotate('PM',xycoords='data',xy=(0.175,3.5),fontsize='xx-large',fontweight='bold')
ax.annotate('PM',xycoords='data',xy=(0.8,3.5),fontsize='xx-large',fontweight='bold')
ax.annotate('AFM',xycoords='data',xy=(0.44,3.5),fontsize='xx-large',fontweight='bold')
ax.annotate('FM',xycoords='data',xy=(0.15,16),fontsize='xx-large',fontweight='bold')
ax.annotate('FM',xycoords='data',xy=(0.8,16),fontsize='xx-large',fontweight='bold')
ax.annotate('FiM',xycoords='data',xy=(0.32,12),fontsize='xx-large',fontweight='bold')
ax.annotate('FiM',xycoords='data',xy=(0.58,12),fontsize='xx-large',fontweight='bold')
"""

plt.savefig('etc.pdf',bbox_inches='tight',dpi=300)
#plt.show()

