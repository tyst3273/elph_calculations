
debug = False

task = 'electrons'
temperature = 0.001

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [100,100,1]
num_kpts_procs = 8

use_hubbard_U = True
use_spin = True

do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 1e-4
electron_scf_energy_tol = 1e-5

electron_mix_method = 'simple'
electron_mix_alpha = 0.8

write_electron_eigenvectors = False
write_site_density = True

lattice_vectors = [[ 2**(1/2),     0.00,     0.00],
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]

atom_files = ['Cu.py']
atom_types = ['Cu','Cu']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00]]

spin_up_site_density = [1, 0] 
spin_down_site_density = [0, 1]

do_simulated_annealing = True
num_anneal_steps = 30
max_anneal_steps = 50
anneal_start_temperature = 0.001
anneal_end_temperature = 0.0001
anneal_step_size = 0.25


num_electrons = 0.35*4



