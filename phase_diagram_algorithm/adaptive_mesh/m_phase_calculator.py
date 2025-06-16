import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------------------------------------------------------

class c_example_phase_calculator:

    # ----------------------------------------------------------------------------------------------

    def __init__(self,r0=3/4,y0=1/2,x1=9/12,y1=9/12,
                 x2=7/8,y2=7/8,x3=1/3,x4=1/3,y4=3/5,dx=1/100):

        """
        example phase checker that returns phases based on a simple condition
        """

        self.r0 = r0

        self.y0 = y0

        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2

        self.x3 = x3

        self.x4 = x4
        self.y4 = y4

        self.dx = dx

    # ----------------------------------------------------------------------------------------------

    def calculate_phase(self,x,y):

        """
        check phase based on a simple condition:

        """
        
        val = 0
        
        if y >= self.y0:
            val = 2

        if x >= self.x1 and y >= self.y1 and x <= self.x2 and y <= self.y2:
            val = 0

        if np.sqrt((x-self.x3)**2+(y-1.0)**2) <= self.x3:
            val = 3

        if np.sqrt(x**2+y**2) <= self.r0:
            val = 1
        
        if x <= self.x4+self.dx and x >= self.x4-self.dx and y <= self.y4:
            val = 4

        return val
    
    # ----------------------------------------------------------------------------------------------

    def plot_phase_diagram(self,num_x,num_y):

        """
        plot the phase diagram on a uniform grid
        """

        fig, ax = plt.subplots(figsize=(6,6))

        x = np.linspace(0,1,num_x)
        y = np.linspace(0,1,num_y)

        x_grid, y_grid = np.meshgrid(x,y,indexing='ij')
        coords = np.c_[x_grid.flatten(), y_grid.flatten()]

        phases = np.zeros((num_x,num_y),dtype=int)

        for ii in range(num_x):
            for jj in range(num_y):
                phases[ii,jj] = self.calculate_phase(x[ii],y[jj])

        unique_phases = np.unique(phases)
        num_phases = unique_phases.size

        _flat_phases = phases.flatten()
        for ii in range(num_phases):
            _inds = np.flatnonzero(_flat_phases == unique_phases[ii])
            _x = coords[_inds,0]
            _y = coords[_inds,1]
            ax.scatter(_x,_y,s=2)

        plt.show()

# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

class c_text_file_phase_calculator:
    
    # ----------------------------------------------------------------------------------------------

    def __init__(self,phase_file='coarse_phases.txt'):

        """
        load data and metadata needed to check phases
        """

        self.phase = np.loadtxt(phase_file).T

        self.num_x, self.num_y = self.phase.shape
        self.x = np.linspace(0,1,self.num_x)
        self.y = np.linspace(0,1,self.num_y)

        self.phase = self.phase.flatten()

        self.x_coords, self.y_coords = np.meshgrid(self.x,self.y,indexing='ij')
        self.x_coords = self.x_coords.flatten()
        self.y_coords = self.y_coords.flatten()

    # ----------------------------------------------------------------------------------------------

    def calculate_phase(self,x,y):

        """
        expects x and y to be between 0 and 1. normalize if u have to.
        it simply finds the nearest phase and returns that.
        """

        _distances = np.sqrt((self.x_coords-x)**2+(self.y_coords-y)**2)
        index = np.argsort(_distances)[0]

        return self.phase[index]
    
    # ----------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    num_x = 100
    num_y = 100

    example = c_example_phase_calculator()
    example.plot_phase_diagram(num_x,num_y)

    # pc = c_phase_checker()

    # num_x = 100; num_y = 100
    # x = np.linspace(0,1,num_x); y = np.linspace(0,1,num_y)

    # phases = np.zeros((num_x*num_y))
    # index = 0
    # for xx in x:
    #     for yy in y:
    #         phases[index] = pc.calculate_phase(xx,yy)
    #         index += 1

    # c = np.zeros((num_x*num_y,3),dtype=float)
    # c[np.flatnonzero(phases == 3),1] = 1.0 # pm
    # c[np.flatnonzero(phases == 1),2] = 1.0 # afm
    # c[np.flatnonzero(phases == 2),0] = 1.0 # fm
    # c[np.flatnonzero(phases == 4),0] = 1.0 # fim
    # c[np.flatnonzero(phases == 4),2] = 1.0 # fim

    # fig, ax = plt.subplots(figsize=(4,4))

    # x, y = np.meshgrid(x,y,indexing='ij')
    # x = x.flatten(); y = y.flatten()

    # for ii in range(1,5):

    #     inds = np.flatnonzero(phases == ii)
    #     _x = x[inds]; _y = y[inds]; _c = c[inds]
    #     ax.scatter(_x,_y,marker='o',s=1,c=_c,linewidths=1,clip_on=False)

    # plt.show()

# --------------------------------------------------------------------------------------------------
