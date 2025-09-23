
import h5py 
import matplotlib.pyplot as plt
import numpy as np

scale = 0.005

fig, ax = plt.subplots()



f1 = 'matelem_1.hdf5'
with h5py.File(f1,'r') as db:
    w1 = db['frequencies'][...]
    x1 = db['coupled_orbital_area_modulation'][...]

nq, nb = w1.shape
no = x1.shape[-1]
q1 = np.linspace(0,1,nq)

for ii in range(nb):

    _w = w1[:,ii]
    _x = np.abs(x1[:,ii,1]) / 2 * scale

    ax.plot(q1,_w,c='g',lw=1)

    ax.fill_between(q1,_w+_x,_w-_x,color='g',alpha=0.2)



f2 = 'prim/matelem_1.hdf5'
with h5py.File(f2,'r') as db:
    w2 = db['frequencies'][...]
    x2 = db['coupled_orbital_area_modulation'][...]

nq, nb = w2.shape
no = x1.shape[-1]
q2 = np.linspace(0,1,nq)

for ii in range(nb):

    _w = w2[:,ii]
    _x = np.abs(x2[:,ii,0]) / 2 * scale

    ax.plot(q2,_w,c='m',ls=':',lw=1)

    ax.fill_between(q2,_w+_x,_w-_x,color='m',alpha=0.2)
    


plt.show()

