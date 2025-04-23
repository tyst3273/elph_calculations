
debug = True #False

task = 'polaron_mft'
temperature = 0.001

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [50,50,1]
num_kpts_procs = 4

use_hubbard_U = False #True
use_spin = True 

do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 1e-5
electron_scf_energy_tol = 1e-6

electron_mix_method = 'simple'
electron_mix_alpha = 0.8

electron_output_file = 'density.hdf5'
write_electron_eigenvectors = False
write_site_density = True

num_electrons = 2

lattice_vectors = [[ 2**(1/2),     0.00,     0.00],
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]

atom_files = ['Cu.py','O.py']
atom_types = ['Cu','Cu','O','O','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00],
                  [0.25,0.25,0.00],
                  [0.25,0.75,0.00],
                  [0.75,0.25,0.00],
                  [0.75,0.75,0.00]]

spin_up_site_density = [ 1, 1,  0, 0, 0, 0 ] 
spin_down_site_density = [ 1, 0,  0, 0, 0, 0 ]

do_polaron_simulated_annealing = True
num_anneal_steps = 10 #50
max_anneal_steps = 10 #100
anneal_start_temperature = 0.01
anneal_end_temperature = 0.0001
anneal_step_size = 0.1

spring_constants_file = 'spring_constants.py'
phonon_eigenvectors_input_file = 'phonons.hdf5'

do_polaron_scf = True
max_polaron_scf_steps = 100
polaron_scf_displacement_tol = 1e-4
displacement_mix_alpha = 0.8




