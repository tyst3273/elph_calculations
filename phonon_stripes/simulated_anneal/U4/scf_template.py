
debug = True
task = 'electrons'
atom_files = [ 'Cu.py','O.py']
temperature = 0.001
use_spin = True
use_hubbard_U = True

orbital_type = 'tight_binding'
hopping_file = 'hopping.py'
kpts_option = 'mesh'
use_kpts_symmetry = False
num_kpts_procs = 8
do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 1e-5
electron_scf_energy_tol = 1e-6
electron_mix_method = 'simple'
electron_mix_alpha = 0.8
write_electron_eigenvectors = False
write_site_density = True

do_simulated_annealing = True
num_anneal_steps = 20
max_anneal_steps = 30
anneal_start_temperature = 1.0
anneal_end_temperature = 0.001
anneal_step_size = 0.1

spring_constants_file = 'spring_constants.py'

