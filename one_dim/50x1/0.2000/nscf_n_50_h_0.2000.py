task = 'electrons'
debug = False
atom_positions_file = None
lattice_vectors = [[ 50.0, 0.0, 0.0],
    [ 0.0, 10.0, 0.0],
    [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu']
atom_files = [ 'Cu.py']
atom_files_dir = './'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.02, 0.0, 0.0],
    [ 0.04, 0.0, 0.0],
    [ 0.06, 0.0, 0.0],
    [ 0.08, 0.0, 0.0],
    [ 0.1, 0.0, 0.0],
    [ 0.12, 0.0, 0.0],
    [ 0.14, 0.0, 0.0],
    [ 0.16, 0.0, 0.0],
    [ 0.18, 0.0, 0.0],
    [ 0.2, 0.0, 0.0],
    [ 0.22, 0.0, 0.0],
    [ 0.24, 0.0, 0.0],
    [ 0.26, 0.0, 0.0],
    [ 0.28, 0.0, 0.0],
    [ 0.3, 0.0, 0.0],
    [ 0.32, 0.0, 0.0],
    [ 0.34, 0.0, 0.0],
    [ 0.36, 0.0, 0.0],
    [ 0.38, 0.0, 0.0],
    [ 0.4, 0.0, 0.0],
    [ 0.42, 0.0, 0.0],
    [ 0.44, 0.0, 0.0],
    [ 0.46, 0.0, 0.0],
    [ 0.48, 0.0, 0.0],
    [ 0.5, 0.0, 0.0],
    [ 0.52, 0.0, 0.0],
    [ 0.54, 0.0, 0.0],
    [ 0.56, 0.0, 0.0],
    [ 0.58, 0.0, 0.0],
    [ 0.6, 0.0, 0.0],
    [ 0.62, 0.0, 0.0],
    [ 0.64, 0.0, 0.0],
    [ 0.66, 0.0, 0.0],
    [ 0.68, 0.0, 0.0],
    [ 0.7, 0.0, 0.0],
    [ 0.72, 0.0, 0.0],
    [ 0.74, 0.0, 0.0],
    [ 0.76, 0.0, 0.0],
    [ 0.78, 0.0, 0.0],
    [ 0.8, 0.0, 0.0],
    [ 0.82, 0.0, 0.0],
    [ 0.84, 0.0, 0.0],
    [ 0.86, 0.0, 0.0],
    [ 0.88, 0.0, 0.0],
    [ 0.9, 0.0, 0.0],
    [ 0.92, 0.0, 0.0],
    [ 0.94, 0.0, 0.0],
    [ 0.96, 0.0, 0.0],
    [ 0.98, 0.0, 0.0]]
temperature = 0.001
num_electrons = 40.0
num_bands = None
use_spin = True
orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 142, 1, 1]
use_kpts_symmetry = False
num_kpts_procs = 6
use_hubbard_U = True
spin_up_site_density = [ 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0,
     0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8,
     0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0,
     0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0]
spin_down_site_density = [ 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8,
     0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0,
     0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8,
     0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8, 0.0, 0.8]
do_electron_scf = False
electron_fixed_fermi_energy = False
calc_electron_fermi_surface = True
electron_delta_width = 0.025
electron_dos_step = 0.01
electron_output_file = 'nscf_n_50_h_0.2000.hdf5'
write_electron_eigenvectors = False
write_site_density = True
electron_eigenvectors_input_file = None
site_density_input_file = 'restart_n_50_h_0.2000.hdf5'
job_description = None
write_kpts_hdf5_file = False
_plot_electron_bands = False
_write_kpts = False
