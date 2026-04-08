import numpy as np
import matplotlib.pyplot as plt
import h5py
import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'matelem.hdf5'

with h5py.File(input_file,'r') as db:
    matrix_elements = db['elph_matrix_elements'][...].squeeze()
    freqs = db['frequencies'][...]
    xi = db['coupled_orbital_area_modulation'][...].squeeze()
    qpts_rlu = db['qpts_rlu'][...]

num_kpts = matrix_elements.shape[0]
matrix_elements = matrix_elements.sum(axis=(0,2,3,5))/num_kpts
xi = xi.sum(axis=2)

num_qpts = freqs.shape[0]
num_modes = freqs.shape[1]
qpts = np.linspace(0,1,qpts_rlu.shape[0])

fig, ax = plt.subplots(figsize=(8,6))

scale = 0.1

for ii in range(num_modes-4,num_modes): 

    # x = np.abs(xi[:,ii])**2*0.0001
    # hi = freqs[:,ii]+x
    # lo = freqs[:,ii]-x
    # ax.fill_between(qpts,lo,hi,color='m',alpha=0.5)
    # ax.errorbar(qpts,freqs[:,ii],x,marker='o',ms=0,c='k',elinewidth=2)

    ax.plot(qpts,freqs[:,ii],lw=1,ls='-',c='k')

    g = np.abs(matrix_elements[:,ii])**2 * 0.1
    # g = np.abs(matrix_elements[:,ii]).imag * scale ** 2
    hi = freqs[:,ii]+g
    lo = freqs[:,ii]-g
    ax.fill_between(qpts,lo,hi,color='b',alpha=0.5)
    ax.errorbar(qpts,freqs[:,ii],g,marker='o',ms=0,c='k',elinewidth=2)

plt.show()


