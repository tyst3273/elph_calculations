
import h5py 
import matplotlib.pyplot as plt
import numpy as np

# scale = 0.0025
scale = 0.00005

fig, ax = plt.subplots()

# --------

f1 = 'matelem.hdf5'
# f1 = 'prim/matelem_2.hdf5'
with h5py.File(f1,'r') as db:
    w1 = db['frequencies'][...]
    x1 = db['coupled_orbital_area_modulation'][...]
    g1 = db['elph_matrix_elements'][...].sum(axis=(0,2,3,5))

nq, nb = w1.shape
no = x1.shape[-1]
q1 = np.linspace(0,1,nq)

for ii in range(nb):

    _w = w1[:,ii]
    # _x = np.abs(x1[:,ii,0]) / 2 * scale * np.sqrt(2)
    _x = np.abs(g1[:,ii]) / 2 * scale 

    ax.plot(q1,_w,c='g',lw=0.5)

    # ax.fill_between(q1,_w+_x,_w-_x,color='g',alpha=0.2)
    ax.errorbar(q1,_w,_x,elinewidth=2,c='g',barsabove=True,alpha=0.25)

# --------

f2 = 'prim/matelem.hdf5'
with h5py.File(f2,'r') as db:
    w2 = db['frequencies'][...]
    x2 = db['coupled_orbital_area_modulation'][...]

nq, nb = w2.shape
no = x1.shape[-1]
q2 = np.linspace(0,1,nq)

for ii in range(nb):

    _w = w2[:,ii]
    _x = np.abs(x2[:,ii,0]) / 2 * scale

    ax.plot(q2,_w,c='m',ls='-',lw=0.5)

    ax.fill_between(q2,_w+_x,_w-_x,color='m',alpha=0.2)
    # ax.errorbar(q2,_w,_x,elinewidth=2,c='m',barsabove=True,alpha=0.25)
    
# --------

plt.show()

