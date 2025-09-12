
debug = False

lattice_vectors = [[ 2**(1/2),     0.00,     0.00], 
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]

atom_types = ['Cu','Cu']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00]]

atom_files = ['Cu.py']

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [250,250,1]

num_kpts_procs = 10

use_hubbard_U = True
use_spin = True

do_electron_scf = True
max_electron_scf_steps = 400

electron_scf_density_tol = 1e-5
electron_scf_energy_tol = 1e-6

temperature = 0.001

electron_mix_method = 'simple'
electron_mix_alpha = 0.8

write_electron_eigenvectors = False
write_site_density = True

do_simulated_annealing = True
num_anneal_steps = 10
max_anneal_steps = 20
anneal_start_temperature = 0.01
anneal_end_temperature = 0.0001
anneal_step_size = 0.25