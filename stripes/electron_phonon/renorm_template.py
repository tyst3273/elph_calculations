
debug = False

task = 'phonon_self_energy' #'phonon_line_widths'
temperature = 0.01

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [10,10,1] 
num_kpts_procs = 2

use_spin = True
use_hubbard_U = True

hopping_file = 'hopping.py'
electron_fixed_fermi_energy = True

num_qpts_procs = 6
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2, 1/2,   0]]
qpts_steps = 26

spring_constants_file = 'spring_constants.py'

phonon_self_energy_step = 0.0005
phonon_self_energy_eps = 0.05



