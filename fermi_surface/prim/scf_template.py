
debug = False

task = 'electrons'
temperature = 0.01

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [100,100,1]
num_kpts_procs = 4

do_electron_scf = True

max_electron_scf_steps = 400
electron_scf_density_tol = 1e-6
electron_scf_energy_tol = 1e-6

electron_mix_method = 'pulay'
electron_mix_alpha = 0.6
electron_mix_beta = 0.2
electron_mix_delay = 10
electron_mix_history = 4

write_electron_eigenvectors = False
write_site_density = True

spin_up_site_density = [1,0,0]
spin_down_site_density = [1,0,0]

use_spin = True
atom_files = ['Cu.py', 'O.py']
lattice_vectors = [[  1.00,  0.00,  0.00],
                   [  0.00,  1.00,  0.00],
                   [  0.00,  0.00, 10.00]]
atom_types = ['Cu', 'O', 'O']
atom_positions = [[ 0.00, 0.00, 0.00],
                  [ 0.50, 0.00, 0.00],
                  [ 0.00, 0.50, 0.00]]


