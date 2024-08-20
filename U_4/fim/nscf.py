
task = 'electrons' 

lattice_vectors = [[ 2**(1/2),     0.00,     0.00],
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]

atom_types = ['Cu','Cu','O','O','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00],
                  [0.25,0.25,0.00],
                  [0.75,0.25,0.00],
                  [0.25,0.75,0.00],
                  [0.75,0.75,0.00]]
atom_files = ['Cu.py','O.py']

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [100,100,1]
num_kpts_procs = 8

use_hubbard_U = True
use_spin = True
temperature = 0.01
num_electrons = 1.9

do_electron_scf = False
electron_fixed_fermi_energy = True

site_density_input_file = 'scf.hdf5'
electron_output_file = 'nscf.hdf5'

_plot_electron_bands = True

calc_electron_fermi_surface = True
electron_dos_step = 0.001
electron_delta_width = 0.005



