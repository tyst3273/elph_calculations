
import numpy as np
import sys
import matplotlib.pyplot as plt
import h5py 

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'electrons_out.hdf5'

with h5py.File(input_file,'r') as db:

    dos = db['dos'][...]
    energy = db['dos_energy'][...]
    ef = db['fermi_energy'][...]

fig, ax = plt.subplots(figsize=(8,6))

ax.plot(energy,dos[:,0],lw=1,ls='-',c='r',ms=0)
ax.plot(energy,-dos[:,1],lw=1,ls='-',c='b',ms=0)
ax.plot([ef,ef],[-1.1*dos.max(),1.1*dos.max()],lw=1,ls=(0,(4,2,2,1)),c=(0.5,0.5,0.5))
ax.plot([1.1*energy.min(),1.1*energy.max()],[0,0],lw=1,ls=(0,(4,2,2,1)),c=(0.5,0.5,0.5))

#plt.savefig('dos.pdf',dpi=300,bbox_inches='tight')
plt.show()

