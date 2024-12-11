
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
import h5py

# --------------------------------------------------------------------------------------------------

def make_colormap(color):

    colors = [[*color,0],[*color,0.1],[*color,1]]
    positions = [0,0.5,1]
    positions = np.arange(len(colors))

    nc = 256
    arr = np.ones((nc,4),dtype=float)
    positions = np.array(positions,dtype=float)
    positions *= nc/positions.max()
    positions = positions.astype(int)

    for ii in range(len(colors)-1):

        c0 = colors[ii]
        if len(c0) == 3:
            c0.append(1.0)

        c1 = colors[ii+1]
        if len(c1) == 3:
            c1.append(1.0)

        for jj in range(4):
            arr[positions[ii]:positions[ii+1],jj] = \
                np.linspace(c0[jj],c1[jj],positions[ii+1]-positions[ii])

    arr[:,:3] = arr[:,:3]/255
    cmap = ListedColormap(arr)

    return cmap

# --------------------------------------------------------------------------------------------------

def get_fs(input_file):

    with h5py.File(input_file,'r') as db:
        fermi_surface = db['fermi_surface'][...]
        if not 'kpts_mesh' in db.keys():
            exit('do calculation on mesh instead')
        kpts_mesh = db['kpts_mesh'][...]

    shape = fermi_surface.shape
    num_kpts = shape[0]
    num_bands = shape[1]
    num_spin = shape[2]

    # sum over bands
    fermi_surface = fermi_surface.sum(axis=(1)).squeeze().reshape(kpts_mesh[:2])

    return fermi_surface

# --------------------------------------------------------------------------------------------------

def plot_fs(fermi_surface,ax,cmap):
    
    vmax = fermi_surface.max()*0.1
    for xx in [-1,0,1]:
        for yy in [-1,0,1]:

            extent = [-0.5+xx,0.5+xx,-0.5+yy,0.5+yy]

            ax.imshow(fermi_surface.T,cmap=cmap,vmin=0,vmax=vmax,aspect='auto',origin='lower',
                interpolation='gaussian',extent=extent)

# --------------------------------------------------------------------------------------------------

def plot_arrow(color,n):

    color = [c/255.0 for c in color]

    kf = 1/4.0*(1-n/2.0)
    #ax.quiver(-kf,-kf,2*kf,2*kf,angles='xy',scale_units='xy',scale=1,color=color)
    ax.quiver(0,0,kf,kf,angles='xy',scale_units='xy',scale=1,color=color)

# --------------------------------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(4,4))

cycle = [[55,  126, 184],[255, 127, 0],[77,  175, 74],[247, 129, 191],[166, 86,  40],
         [152, 78,  163],[153, 153, 153],[228, 26,  28],[222, 222, 0]]

color = [0,0,0]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.00.hdf5')
plot_fs(fermi_surface,ax,cmap)
plot_arrow(color,0.0)

color = cycle[0]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_0.90.hdf5')
plot_fs(fermi_surface,ax,cmap)
plot_arrow(color,0.1)

color = cycle[1]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_0.80.hdf5')
plot_fs(fermi_surface,ax,cmap)
plot_arrow(color,0.2)

color = cycle[2]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_0.70.hdf5')
plot_fs(fermi_surface,ax,cmap)
plot_arrow(color,0.3)

color = cycle[3]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_0.60.hdf5')
plot_fs(fermi_surface,ax,cmap)
plot_arrow(color,0.4)

color = cycle[4]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_0.50.hdf5')
plot_fs(fermi_surface,ax,cmap)
plot_arrow(color,0.5)

color = cycle[5]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_0.40.hdf5')
plot_fs(fermi_surface,ax,cmap)
plot_arrow(color,0.6)

color = cycle[6]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_0.30.hdf5')
plot_fs(fermi_surface,ax,cmap)
plot_arrow(color,0.7)

color = cycle[7]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_0.20.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = cycle[8]
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_0.10.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = 255-np.array(cycle[0])
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.10.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = 255-np.array(cycle[1])
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.20.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = 255-np.array(cycle[2])
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.30.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = 255-np.array(cycle[3])
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.40.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = 255-np.array(cycle[4])
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.50.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = 255-np.array(cycle[5])
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.60.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = 255-np.array(cycle[6])
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.70.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = 255-np.array(cycle[7])
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.80.hdf5')
plot_fs(fermi_surface,ax,cmap)

color = 255-np.array(cycle[8])
cmap = make_colormap(color)
fermi_surface = get_fs('nscf_n_1.90.hdf5')
plot_fs(fermi_surface,ax,cmap)

#for xx in [-1,0,1]:
#    for yy in [-1,0,1]:
#        ax.plot([xx+0.5,xx+0.5],[-1.5,1.5],lw=1,ls=(0,(2,2)),c=(0,0,0),ms=0,alpha=0.5)
#        ax.plot([xx-0.5,xx-0.5],[-1.5,1.5],lw=1,ls=(0,(2,2)),c=(0,0,0),ms=0,alpha=0.5)
#        ax.plot([-1.5,1.5],[yy+0.5,yy+0.5],lw=1,ls=(0,(2,2)),c=(0,0,0),ms=0,alpha=0.5)
#        ax.plot([-1.5,1.5],[yy-0.5,yy-0.5],lw=1,ls=(0,(2,2)),c=(0,0,0),ms=0,alpha=0.5)

ax.axis([-0.5,0.5,-0.5,0.5])
#ax.axis([-1,1,-1,1])

plt.show()


