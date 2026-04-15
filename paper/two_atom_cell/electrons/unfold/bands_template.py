
debug = True

_s_ = 1/2**(1/2)
atom_files = ['Cu.py','O.py']
lattice_vectors = [[   _s_,  _s_,  0],
                   [  -_s_,  _s_,  0],
                   [    0,   0, 10]]
atom_types = ['Cu','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.00,0.00],
                  [0.00,0.50,0.00]]

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'path'
kpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0],
             [ 1/2, 1/2,   0],
             [   0,   0,   0]]
kpts_steps = 201
num_kpts_procs = 8

use_hubbard_U = True
use_spin = True

temperature = 0.001

site_density_input_file = 'nscf.hdf5'
electron_output_file = 'bands.hdf5'

do_electron_scf = False
electron_fixed_fermi_energy = True

# _plot_electron_bands = True

# num_electrons = 0.95

