
task = 'phonon_self_energy' #'phonon_line_widths'
temperature = 0.001

use_spin = True
use_hubbard_U = True

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

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [100,100,1] 
num_kpts_procs = 1

hopping_file = 'hopping.py'
electron_fixed_fermi_energy = True

num_qpts_procs = 6
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0]]
qpts_steps = 101

spring_constants_file = 'spring_constants.py'

phonon_self_energy_step = 0.0005
phonon_self_energy_eps = 0.05



