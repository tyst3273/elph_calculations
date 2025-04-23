
debug = False

task = 'phonons' 
temperature = 0.001

atom_files = ['Cu.py','O.py']
lattice_vectors = [[     1.00,     0.00,     0.00],
                   [     0.00,     1.00,     0.00],
                   [     0.00,     0.00,    10.00]]
atom_types = ['Cu','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.00,0.00],
                  [0.00,0.50,0.00]]

num_qpts_procs = 8 #10
qpts_option = 'path'
qpts_path = [[   0,   0,  0],
             [   0, 1/2,  0],
             [ 1/2, 1/2,  0],
             [   0,   0,  0]]
qpts_steps = 401

spring_constants_file = 'spring_constants.py'

# neutron_energy_step = 0.001
# neutron_delta_width = 0.0025

# phonon_output_file = 'neutrons_hb.hdf5'

_plot_phonon_bands = True