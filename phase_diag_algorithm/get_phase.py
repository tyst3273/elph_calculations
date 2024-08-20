import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------------------------------------------------------

class phase_checker:
    
    # ----------------------------------------------------------------------------------------------

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

    # ----------------------------------------------------------------------------------------------

    def check_phase(self,x,y):

        """
        expects x and y to be between 0 and 1. normalize if u have to.
        it simply finds the nearest phase and returns that.
        """

        _distances = np.sqrt((self.x_coords-x)**2+(self.y_coords-y)**2)
        index = np.argsort(_distances)[0]

        return self.phase[index]

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # instantiate this class to check phase (it loads phases from a file)
    pc = phase_checker()

    # create x, y coords to loop over
    num_x = 100; num_y = 100
    x = np.linspace(0,1,num_x); y = np.linspace(0,1,num_y)

    # the phases. used for plotting below
    phases = np.zeros((num_x*num_y))

    # loop over the coords and get phases
    index = 0
    for xx in x:
        for yy in y:
            phases[index] = pc.check_phase(xx,yy)
            index += 1

    # colors of points to plot
    c = np.zeros((num_x*num_y,3),dtype=float)
    c[np.flatnonzero(phases == 3),1] = 1.0 # pm
    c[np.flatnonzero(phases == 1),2] = 1.0 # afm
    c[np.flatnonzero(phases == 2),0] = 1.0 # fm
    c[np.flatnonzero(phases == 4),0] = 1.0 # fim
    c[np.flatnonzero(phases == 4),2] = 1.0 # fim

    # create plot
    fig, ax = plt.subplots(figsize=(4,4))

    # these are coords on 'meshgrid'
    x, y = np.meshgrid(x,y,indexing='ij')
    x = x.flatten(); y = y.flatten()

    # loop over the phases
    for ii in range(1,5):

        # plot them
        inds = np.flatnonzero(phases == ii)
        _x = x[inds]; _y = y[inds]; _c = c[inds]
        ax.scatter(_x,_y,marker='o',s=1,c=_c,linewidths=1,clip_on=False)

    # show plot
    plt.show()

    # fuck bitches

    # get money

# --------------------------------------------------------------------------------------------------

