
debug = True #False

task = 'electrons'
temperature = 0.01

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [4,4,1]
num_kpts_procs = 4

use_hubbard_U = True
use_spin = True

do_electron_scf = True
max_electron_scf_steps = 400
electron_scf_density_tol = 1e-1
electron_scf_energy_tol = 1e-1

electron_mix_method = 'simple'
electron_mix_alpha = 0.6
electron_mix_beta = 0.2
electron_mix_delay = 10
electron_mix_history = 4

electron_output_file = 'density.hdf5'
write_electron_eigenvectors = False
write_site_density = True

do_simulated_annealing = True
num_anneal_steps = 50
max_anneal_steps = 100
anneal_start_temperature = 10
anneal_final_temperature = 1
anneal_step_size = 0.25

atom_files = ['Cu.py']