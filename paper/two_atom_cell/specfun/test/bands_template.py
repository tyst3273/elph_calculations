
debug = True

atom_files = ['Cu.py','O.py']
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

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'path'
kpts_path = [[   0,   0,   0],
             [ 1/2, 1/2,   0],
             [   1,   0,   0],
             [   0,   0,   0]]
kpts_steps = 201
num_kpts_procs = 8

use_hubbard_U = True
use_spin = True

temperature = 0.001

do_electron_scf = False
site_density_input_file = 'nscf.hdf5'
electron_output_file = 'bands.hdf5'
electron_fixed_fermi_energy = True

_plot_electron_bands = True

