task = 'phonon_self_energy'
debug = False


lattice_vectors = [[ 8.0, 0.0, 0.0],
                   [ 0.0, 8.0, 0.0],
                   [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu']
atom_files = [ 'Cu.py']
atom_files_dir = '/home/ty/research/repos/elph_calculations/stripes/simulated_anneal/8x8'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.125, 0.0, 0.0],
    [ 0.25, 0.0, 0.0],
    [ 0.375, 0.0, 0.0],
    [ 0.5, 0.0, 0.0],
    [ 0.625, 0.0, 0.0],
    [ 0.75, 0.0, 0.0],
    [ 0.875, 0.0, 0.0],
    [ 0.0, 0.125, 0.0],
    [ 0.125, 0.125, 0.0],
    [ 0.25, 0.125, 0.0],
    [ 0.375, 0.125, 0.0],
    [ 0.5, 0.125, 0.0],
    [ 0.625, 0.125, 0.0],
    [ 0.75, 0.125, 0.0],
    [ 0.875, 0.125, 0.0],
    [ 0.0, 0.25, 0.0],
    [ 0.125, 0.25, 0.0],
    [ 0.25, 0.25, 0.0],
    [ 0.375, 0.25, 0.0],
    [ 0.5, 0.25, 0.0],
    [ 0.625, 0.25, 0.0],
    [ 0.75, 0.25, 0.0],
    [ 0.875, 0.25, 0.0],
    [ 0.0, 0.375, 0.0],
    [ 0.125, 0.375, 0.0],
    [ 0.25, 0.375, 0.0],
    [ 0.375, 0.375, 0.0],
    [ 0.5, 0.375, 0.0],
    [ 0.625, 0.375, 0.0],
    [ 0.75, 0.375, 0.0],
    [ 0.875, 0.375, 0.0],
    [ 0.0, 0.5, 0.0],
    [ 0.125, 0.5, 0.0],
    [ 0.25, 0.5, 0.0],
    [ 0.375, 0.5, 0.0],
    [ 0.5, 0.5, 0.0],
    [ 0.625, 0.5, 0.0],
    [ 0.75, 0.5, 0.0],
    [ 0.875, 0.5, 0.0],
    [ 0.0, 0.625, 0.0],
    [ 0.125, 0.625, 0.0],
    [ 0.25, 0.625, 0.0],
    [ 0.375, 0.625, 0.0],
    [ 0.5, 0.625, 0.0],
    [ 0.625, 0.625, 0.0],
    [ 0.75, 0.625, 0.0],
    [ 0.875, 0.625, 0.0],
    [ 0.0, 0.75, 0.0],
    [ 0.125, 0.75, 0.0],
    [ 0.25, 0.75, 0.0],
    [ 0.375, 0.75, 0.0],
    [ 0.5, 0.75, 0.0],
    [ 0.625, 0.75, 0.0],
    [ 0.75, 0.75, 0.0],
    [ 0.875, 0.75, 0.0],
    [ 0.0, 0.875, 0.0],
    [ 0.125, 0.875, 0.0],
    [ 0.25, 0.875, 0.0],
    [ 0.375, 0.875, 0.0],
    [ 0.5, 0.875, 0.0],
    [ 0.625, 0.875, 0.0],
    [ 0.75, 0.875, 0.0],
    [ 0.875, 0.875, 0.0]]

temperature = 0.001
num_electrons = 56.0

orbital_type = 'tight_binding'
hopping_file = 'hopping.py'

kpts_option = 'mesh'
kpts_mesh = [ 50, 50, 1]
use_kpts_symmetry = False

num_kpts_procs = 6

use_spin = True
use_hubbard_U = True
spin_up_site_density = [ 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0,
     0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.875, 0.0, 0.875, 0.0,
     0.875, 0.0, 0.875, 0.0, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875,
     0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.0, 0.875, 0.0, 0.875,
     0.0, 0.875, 0.0, 0.875, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0,
     0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875]
spin_down_site_density = [ 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875,
     0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.0, 0.875, 0.0, 0.875,
     0.0, 0.875, 0.0, 0.875, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0,
     0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.875, 0.0, 0.875, 0.0,
     0.875, 0.0, 0.875, 0.0, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875,
     0.875, 0.0, 0.875, 0.0, 0.875, 0.0, 0.875, 0.0]

do_electron_scf = False
electron_fixed_fermi_energy = True

calc_electron_fermi_surface = True
electron_delta_width = 0.025
electron_dos_step = 0.01
electron_output_file = 'nscf_n_8_h_0.1250.hdf5'

write_electron_eigenvectors = False
write_site_density = True
site_density_input_file = 'nscf_n_8_h_0.1250.hdf5'

num_qpts_procs = 4
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2, 1/2,   0],
             [   1,   0,   0],
             [   0,   0,   0]]
qpts_steps = 20
spring_constants_file = 'spring_constants.py'

elph_output_file = 'renormalization.hdf5' #'full.hdf5'

phonon_self_energy_step = None 
phonon_self_energy_eps = 0.1 