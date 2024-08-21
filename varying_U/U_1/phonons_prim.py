
task = 'phonons' 

lattice_vectors = [[     1.00,     0.00,     0.00],
                   [     0.00,     1.00,     0.00],
                   [     0.00,     0.00,    10.00]]

atom_types = ['Cu','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.00,0.00],
                  [0.00,0.50,0.00]]
atom_files = ['Cu.py','O.py']

temperature = 0.01

num_qpts_procs = 10
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0],
             [ 1/2, 1/2,   0],
             [   0,   0,   0]]
qpts_steps = 100

spring_constants_file = 'spring_constants.py'


#phonon_delta_width = 0.001
#phonon_dos_step = 0.0001

_plot_phonon_bands = True

