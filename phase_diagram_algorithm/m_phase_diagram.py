
import numpy as np
import matplotlib.pyplot as plt

from m_phase_calculator import c_example_phase_calculator


# --------------------------------------------------------------------------------------------------

class c_local_adaptive_mesh:

    # ----------------------------------------------------------------------------------------------

    def __init__(self,mesh_size,calculate_phase):

        """
        """

        self.mesh_size = np.array(mesh_size,dtype=int)
        self.num_dimensions = self.mesh_size.size

        # callback function to calculate the phase
        self.calculate_phase = calculate_phase

    # ----------------------------------------------------------------------------------------------
    
    def _init_coarse_mesh(self):

        """
        initialize the coarse mesh coordinates
        """

        _edges = []
        for ii in range(self.num_dimensions):
            _edges.append(np.arange(self.mesh_size[ii]))
        _grid = np.meshgrid(*_edges,indexing='ij')

        self.coordinates = np.array([_g.flatten() for _g in _grid]).T
        self.num_coordinates = self.coordinates.shape[0]

        self.phases = np.zeros(self.num_coordinates, dtype=int)

    # ----------------------------------------------------------------------------------------------

    def coarse_calculation(self):

        """
        do a calculation on the coarse mesh
        """

        self._init_coarse_mesh()
        
        for ii in range(self.num_coordinates):
            _coords = self.coordinates[ii,:] / self.mesh_size
            self.phases[ii] = self.calculate_phase(*_coords)

    # ----------------------------------------------------------------------------------------------

    def plot_phase_diagram(self):

        """
        plot the phase diagram on a uniform grid
        """

        fig, ax = plt.subplots(figsize=(6,6))

        unique_phases = np.unique(self.phases)
        num_phases = unique_phases.size

        _flat_phases = self.phases.flatten()
        for ii in range(num_phases):
            _inds = np.flatnonzero(_flat_phases == unique_phases[ii])
            _x = self.coordinates[_inds,0]
            _y = self.coordinates[_inds,1]
            ax.scatter(_x,_y,s=2)

        plt.show()

    # ----------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    example = c_example_phase_calculator()

    calculator = c_local_adaptive_mesh([20,20],example.calculate_phase)
    calculator.coarse_calculation()
    calculator.plot_phase_diagram()

    # print(calculator.flat_coordinates)
