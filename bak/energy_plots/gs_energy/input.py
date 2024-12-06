
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
kpts_mesh = [50,50,1]
#use_kpts_symmetry = True
num_kpts_procs = 4

use_hubbard_U = True
use_spin = True

do_electron_scf = True
max_electron_scf_steps = 200

#electron_scf_density_tol = 1e-5
#electron_scf_energy_tol = 1e-6
electron_scf_density_tol = 1e-6
electron_scf_energy_tol = 1e-6

temperature = 0.003
num_electrons = 1.6

electron_mix_method = 'pulay'
electron_mix_alpha = 0.8
electron_mix_beta = 0.6
electron_mix_history = 4
electron_mix_delay = 10

write_electron_eigenvectors = False



