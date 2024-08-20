
import matplotlib.pyplot as plt
import h5py
import numpy as np
import os

precision = 6

# --------------------------------------------------------------------------------------------------

def _get_data(file_name):

    with h5py.File(file_name,'r') as db:
        free_energy = db['free_energy'][...]
        gs_energy = db['ground_state_energy'][...]
        metal = db['is_metal'][...].astype(int)
        up = db['spin_up_site_density'][...]
        down = db['spin_down_site_density'][...]
        converged = db['converged_electron_scf'][...]

    mag = up.round(3)-down.round(3)
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

def get_phase(U,dir='.'):

    energy = []
    order = []
    metal = []

    _c, _e, _o, _m = _get_data(dir+'/'+f'afm_dense_U{U:.3f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'fm_dense_U{U:.3f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'fim_dense_U{U:.3f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'pm_dense_U{U:.3f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    _c, _e, _o, _m = _get_data(dir+'/'+f'cdw_dense_U{U:.3f}.hdf5')
    energy.append(_e); order.append(_o); metal.append(_m)

    ind = np.argmin(np.array(energy))
    order = order[ind]; metal = metal[ind]

    return energy, metal

# --------------------------------------------------------------------------------------------------

def get_sweep_params(dir='.'):

    U = []

    files = os.listdir(dir)
    for f in files:
        if not f.endswith('.hdf5'):
            continue

        f = f[:-5]
        f = f.split('_')
        for _ in f:
            if _.startswith('U'):
                U.append(float(_[1:]))

    U = np.unique(np.array(U,dtype=float))

    return U

# --------------------------------------------------------------------------------------------------


U_arr = get_sweep_params('symm')
num_calcs = U_arr.size

energy = np.zeros((num_calcs,5),dtype=float)
metal = np.zeros((num_calcs,5),dtype=int)

for ii in range(num_calcs):

    U = U_arr[ii]
    _energy, _metal = get_phase(U,'symm') # afm, fm, fim, pm

    energy[ii,:] = _energy
    metal[ii,:] = _metal


fig, ax = plt.subplots(figsize=(4,3.5))

label = ['afm','fm','fim','pm','cdw']
c = ['r','b','m','g','k']
marker = ['s','o','d','^','*']

# cdw converges to PM for no electron-phonon coupling
for ii in range(4):

    ax.plot(U_arr,energy[:,ii],c=c[ii],marker=marker[ii],
            ms=2,lw=1,ls='-',label=label[ii]) #,clip_on=False)

data = np.loadtxt('ref_data/AFM_2.csv',delimiter=',')
plt.plot(1/data[:,0],data[:,1],c='r',lw=1,ls='--',marker='o',mfc='none',ms=0,label='ref-afm')
data = np.loadtxt('ref_data/FM_2.csv',delimiter=',')
plt.plot(1/data[:,0],data[:,1],c='b',lw=1,ls='--',marker='s',mfc='none',ms=0,label='ref-fim')

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.1)
ax.minorticks_on()
ax.tick_params(which='both',width=1,labelsize='medium')
ax.tick_params(which='major',length=5)
ax.tick_params(which='minor',length=2)
ax.set_rasterized = True

ax.set_xlabel('U/t',fontsize='large')
ax.set_ylabel('E/t',fontsize='large')

ax.axis([4,10,-1.9,-1])

ax.legend(frameon=False,fontsize='large')

plt.savefig('free_energies.pdf',bbox_inches='tight')
#plt.show()




















