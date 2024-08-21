
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
num_electrons = 1

do_electron_scf = True
max_electron_scf_steps = 400
electron_scf_density_tol = 1e-5
electron_scf_energy_tol = 1e-6
electron_mix_method = 'pulay'
electron_mix_alpha = 0.4
electron_mix_beta = 0.4
electron_mix_history = 4
electron_mix_delay = 10

spin_up_site_density = [ 1, 1, 0,0,0,0]
spin_down_site_density = [ 1, 1, 0,0,0,0]

electron_output_file = 'scf.hdf5'
