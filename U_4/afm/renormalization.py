
task = 'phonon_self_energy' 

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
kpts_mesh = [400,400,1]
num_kpts_procs = 2

use_hubbard_U = True
use_spin = True
temperature = 0.01
num_electrons = 1.6

do_electron_scf = False
electron_fixed_fermi_energy = True #False

site_density_input_file = 'scf.hdf5'
electron_output_file = 'nah.hdf5'

num_qpts_procs = 10
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2, 1/2,   0],
             [   1,   0,   0],
             [   0,   0,   0]]
qpts_steps = 100
#qpts_steps = 25

spring_constants_file = 'spring_constants.py'

elph_output_file = 'renormalization.hdf5' 
phonon_self_energy_step = None 
phonon_self_energy_eps = 0.1

#_write_qpts = True
