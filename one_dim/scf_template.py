task = 'electrons'
atom_files = ['Cu.py']
debug = True
atom_files_dir = './'
temperature = 0.001
use_spin = True
orbital_type = 'tight_binding'
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 24, 24, 1]
use_kpts_symmetry = False
num_kpts_procs = 4
use_hubbard_U = True
do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 1e-2
electron_scf_energy_tol = 1e-4
electron_mix_method = 'simple'
electron_mix_alpha = 0.6
electron_output_file = 'scf_n_8_h_0.5000.hdf5'
write_electron_eigenvectors = False
write_site_density = True
do_simulated_annealing = True
num_anneal_steps = 50
max_anneal_steps = 75
anneal_start_temperature = 0.1
anneal_end_temperature = 0.0001
anneal_step_size = 0.5
