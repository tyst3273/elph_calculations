
import numpy as np
import matplotlib.pyplot as plt

metallic = np.loadtxt('metallic')

afm_up = np.loadtxt('afm_up')
fm_up = np.loadtxt('fm_up')
pm_up = np.loadtxt('pm_up')
up = [afm_up,fm_up,pm_up]

afm_down = np.loadtxt('afm_down')
fm_down = np.loadtxt('fm_down')
pm_down = np.loadtxt('pm_down')
down = [afm_down,fm_down,pm_down]

def get_mag_config(step,index):
    u = up[index][step]
    d = down[index][step]

    m = np.sum(u-d)
    if np.abs(m) > 0.1: # FM
        return 1
    _ = (np.abs(u[0]-u[1])+np.abs(d[0]-d[1]))/2 # AFM
    if _ > 0.1:
        return 0
    else:   # PM
        return 2

def get_metallic(step,index):
    return metallic[step,index]

gs_energy = np.loadtxt('gs_energy')
tU = gs_energy[:,0]
ne = gs_energy[:,1]/4 # go from num E to filling fraction

gs_min = np.argmin(gs_energy[:,2:],axis=1).astype(object)

num = gs_min.size
gs_config = np.zeros(num,dtype=object)

gap_config = np.zeros(num,dtype=object)
for ii in range(num):
    gs_config[ii] = get_mag_config(ii,gs_min[ii])
    gap_config[ii] = get_metallic(ii,gs_min[ii])

inds = np.flatnonzero(gs_config == 0) # AFM
gs_config[inds] = 'r'
inds = np.flatnonzero(gs_config == 1) # FM
gs_config[inds] = 'g'
inds = np.flatnonzero(gs_config == 2) # PM
gs_config[inds] = 'b'

inds = np.flatnonzero(gap_config == 0)
mfc = np.copy(gs_config)
mfc[inds] = 'none'

ref1 = np.loadtxt('ref_1.csv',delimiter=',')
ref1[:,0] /= 2
ref2 = np.loadtxt('ref_2.csv',delimiter=',')
ref2[:,0] /= 2


fig, ax = plt.subplots(figsize=(6,5))
ax.scatter(ne,tU,edgecolors=gs_config,marker='o',s=50,c=mfc,linewidths=1)

ax.plot(ref1[:,0],ref1[:,1],ms=0,ls=(0,(3,1)),lw=2,c='k')
ax.plot(1-ref1[:,0],ref1[:,1],ms=0,ls=(0,(3,1)),lw=2,c='k')
ax.plot(ref2[:,0],ref2[:,1],ms=0,ls=(0,(3,1)),lw=2,c='k')
ax.plot(1-ref2[:,0],ref2[:,1],ms=0,ls=(0,(3,1)),lw=2,c='k')

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.1)
ax.minorticks_on()
ax.tick_params(which='both',width=1,labelsize='large')
ax.tick_params(which='major',length=5)
ax.tick_params(which='minor',length=2)
ax.set_rasterized = True

ax.axis([0.05,0.95,0.05,0.65])
ax.set_xlabel('filling fraction',fontsize='large')
ax.set_ylabel('t/U',fontsize='larger',rotation='horizontal',labelpad=15)

ax.annotate('paramagnetic',xycoords='data',xy=(0.1,0.465),fontsize='large')
ax.annotate('paramagnetic',xycoords='data',xy=(0.65,0.465),fontsize='large')

ax.annotate('antiferromagnetic',xycoords='data',xy=(0.355,0.165),fontsize='large')

ax.annotate('ferromagnetic',xycoords='data',xy=(0.1,0.065),fontsize='large')
ax.annotate('ferromagnetic',xycoords='data',xy=(0.65,0.065),fontsize='large')


plt.savefig('hubbard_mft_phase_diagram.pdf',bbox_inches='tight')
plt.show()






