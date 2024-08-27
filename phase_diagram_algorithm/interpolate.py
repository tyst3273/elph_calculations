import numpy as np
import matplotlib.pyplot as plt

# dont use this
"""
def regenerate_interpolated_data(num_x=500,num_y=500,plot=True):

    num_n_interp = num_x
    num_U_interp = num_y

    # load the raw data
    data = np.loadtxt('raw_phases.txt')
    U = np.unique(data[:,0])
    num_U = U.size
    n = np.unique(data[:,1])
    num_n = n.size

    # reshape raw data (+1 is to be consistent w/ Beaus code)
    phase = data[:,2].astype(int)+1
    phase.shape = [num_n,num_U]
    phase = np.r_[phase[:-1,:],np.flipud(phase)]
    num_n = 2*num_n-1
    n = np.r_[n,2+n[:-1]]
    n /= 4.0

    # create interpolation grid
    interp_U = np.linspace(U.min(),U.max(),num_U_interp)
    interp_n = np.linspace(0,1,num_n_interp)
    interp_n, interp_U = np.meshgrid(interp_n,interp_U,indexing='ij')
    interp_n = interp_n.flatten(); interp_U = interp_U.flatten()
    points = np.c_[interp_n,interp_U]

    # interpolate
    interp_phase = interpn((n,U),phase,points,bounds_error=False,fill_value=None,method='nearest')
    interp_phase = interp_phase.round(1).astype(int)
    num_points = interp_phase.size

    # write coarse and interpolated data to file
    interp_phase.shape = [num_n_interp,num_U_interp]
    np.savetxt('interpolated_phases.txt',interp_phase.T,fmt='%d')
    np.savetxt('coarse_phases.txt',phase.T,fmt='%d')

    # toggle this on/off to toggle plotting
    if plot:

        interp_phase = interp_phase.flatten()
        
        c = np.zeros((num_points,3),dtype=float)
        c[np.flatnonzero(interp_phase == 3),1] = 1.0 # pm
        c[np.flatnonzero(interp_phase == 1),2] = 1.0 # afm
        c[np.flatnonzero(interp_phase == 2),0] = 1.0 # fm
        c[np.flatnonzero(interp_phase == 4),0] = 1.0 # fim
        c[np.flatnonzero(interp_phase == 4),2] = 1.0 # fim

        fig, ax = plt.subplots(figsize=(4,4))

        for ii in range(1,5):

            inds = np.flatnonzero(interp_phase == ii)
            _n = interp_n[inds]; _U = interp_U[inds]; _c = c[inds]
            ax.scatter(_n,_U,marker='o',s=1,c=_c,linewidths=1,clip_on=False)

        plt.show()
"""

class phase_checker:

    def __init__(self,phase_file='coarse_phases.txt'):

        """
        load data and metadata needed to check phases
        """

        self.phase = np.loadtxt(phase_file)

        self.num_x, self.num_y = self.phase.shape
        self.x = np.linspace(0,1,self.num_x)
        self.y = np.linspace(0,1,self.num_y)

        self.phase = self.phase.flatten()

        self.x_coords, self.y_coords = np.meshgrid(self.x,self.y,indexing='ij')
        self.x_coords = self.x_coords.flatten()
        self.y_coords = self.y_coords.flatten()


    def check_phase(self,x,y):

        """
        expects x and y to be between 0 and 1. normalize if u have to.
        it simply finds the nearest phase and returns that.
        """

        _distances = np.sqrt((self.x_coords-x)**2+(self.y_coords-y)**2)
        index = np.argsort(_distances)[0]

        return self.phase[index]


if __name__ == '__main__':

    pc = phase_checker()

    num_x = 100; num_y = 100
    x = np.linspace(0,1,num_x); y = np.linspace(0,1,num_y)

    phases = np.zeros((num_x*num_y))
    index = 0
    for xx in x:
        for yy in y:
            phases[index] = pc.check_phase(xx,yy)
            index += 1

    c = np.zeros((num_x*num_y,3),dtype=float)
    c[np.flatnonzero(phases == 3),1] = 1.0 # pm
    c[np.flatnonzero(phases == 1),2] = 1.0 # afm
    c[np.flatnonzero(phases == 2),0] = 1.0 # fm
    c[np.flatnonzero(phases == 4),0] = 1.0 # fim
    c[np.flatnonzero(phases == 4),2] = 1.0 # fim

    fig, ax = plt.subplots(figsize=(4,4))

    x, y = np.meshgrid(x,y,indexing='ij')
    x = x.flatten(); y = y.flatten()

    for ii in range(1,5):

        inds = np.flatnonzero(phases == ii)
        _x = x[inds]; _y = y[inds]; _c = c[inds]
        ax.scatter(_x,_y,marker='o',s=1,c=_c,linewidths=1,clip_on=False)

    plt.show()


