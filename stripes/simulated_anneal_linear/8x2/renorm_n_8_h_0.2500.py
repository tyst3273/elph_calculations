task = 'phonon_self_energy'
# debug = True

atom_positions_file = None
lattice_vectors = [[ 8.0, 0.0, 0.0],
                   [ 0.0, 2.0, 0.0],
                   [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O',
     'O', 'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu',
     'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O', 'O',
     'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O', 'O']
atom_files = [ 'Cu.py', 'O.py']
atom_files_dir = '/home/ty/research/repos/elph_calculations/stripes/simulated_anneal_linear/8x2'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.0625, 0.0, 0.0],
    [ 0.0, 0.25, 0.0],
    [ 0.125, 0.0, 0.0],
    [ 0.1875, 0.0, 0.0],
    [ 0.125, 0.25, 0.0],
    [ 0.25, 0.0, 0.0],
    [ 0.3125, 0.0, 0.0],
    [ 0.25, 0.25, 0.0],
    [ 0.375, 0.0, 0.0],
    [ 0.4375, 0.0, 0.0],
    [ 0.375, 0.25, 0.0],
    [ 0.5, 0.0, 0.0],
    [ 0.5625, 0.0, 0.0],
    [ 0.5, 0.25, 0.0],
    [ 0.625, 0.0, 0.0],
    [ 0.6875, 0.0, 0.0],
    [ 0.625, 0.25, 0.0],
    [ 0.75, 0.0, 0.0],
    [ 0.8125, 0.0, 0.0],
    [ 0.75, 0.25, 0.0],
    [ 0.875, 0.0, 0.0],
    [ 0.9375, 0.0, 0.0],
    [ 0.875, 0.25, 0.0],
    [ 0.0, 0.5, 0.0],
    [ 0.0625, 0.5, 0.0],
    [ 0.0, 0.75, 0.0],
    [ 0.125, 0.5, 0.0],
    [ 0.1875, 0.5, 0.0],
    [ 0.125, 0.75, 0.0],
    [ 0.25, 0.5, 0.0],
    [ 0.3125, 0.5, 0.0],
    [ 0.25, 0.75, 0.0],
    [ 0.375, 0.5, 0.0],
    [ 0.4375, 0.5, 0.0],
    [ 0.375, 0.75, 0.0],
    [ 0.5, 0.5, 0.0],
    [ 0.5625, 0.5, 0.0],
    [ 0.5, 0.75, 0.0],
    [ 0.625, 0.5, 0.0],
    [ 0.6875, 0.5, 0.0],
    [ 0.625, 0.75, 0.0],
    [ 0.75, 0.5, 0.0],
    [ 0.8125, 0.5, 0.0],
    [ 0.75, 0.75, 0.0],
    [ 0.875, 0.5, 0.0],
    [ 0.9375, 0.5, 0.0],
    [ 0.875, 0.75, 0.0]]

temperature = 0.001
num_electrons = 12.0
use_spin = True

orbital_type = 'tight_binding'
hopping_file = 'hopping.py'

use_hubbard_U = True

do_electron_scf = False
electron_fixed_fermi_energy = True

write_electron_eigenvectors = False
site_density_input_file = 'restart_n_8_h_0.2500.hdf5'

elph_output_file = 'renormalization.hdf5' #'full.hdf5'
phonon_self_energy_step = None 
phonon_self_energy_eps = 0.1 

kpts_option = 'mesh'
kpts_mesh = [ 10, 40, 1]
use_kpts_symmetry = False
num_kpts_procs = 4

num_qpts_procs = 4
qpts_option = 'path'
qpts_path = [[   0,    0,   0],
             [   0,  1/2,   0]]
qpts_steps = 21
spring_constants_file = 'spring_constants.py'

