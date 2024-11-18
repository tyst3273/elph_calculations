
debug = False

task = 'electrons'
temperature = 0.001

atom_files = ['Cu.py','O.py']

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [40,80,1]
num_kpts_procs = 16

use_hubbard_U = True
use_spin = True

do_electron_scf = True

max_electron_scf_steps = 400
electron_scf_density_tol = 1e-6
electron_scf_energy_tol = 1e-6

electron_mix_method = 'pulay'
electron_mix_alpha = 0.6
electron_mix_beta = 0.2
electron_mix_delay = 10
electron_mix_history = 4

electron_output_file = 'density.hdf5'
write_electron_eigenvectors = False
write_site_density = True


