
debug = False

task = 'phonons' 
temperature = 0.001

_s_ = 1/2**(1/2)
atom_files = ['Cu.py','O.py']
lattice_vectors = [[   _s_,  _s_,  0],
                   [  -_s_,  _s_,  0],
                   [    0,   0, 10]]
atom_types = ['Cu','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.00,0.00],
                  [0.00,0.50,0.00]]

spring_constants_file = 'spring_constants.py'

num_qpts_procs = 10
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0],
             [ 1/2, 1/2,   0],
             [   0,   0,   0]]
qpts_steps = 100

use_qpts_symmetry = False

phonon_output_file = 'phonons.hdf5'

_plot_phonon_bands = True







