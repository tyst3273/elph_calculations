task = 'electrons'
debug = False
atom_positions_file = None
lattice_vectors = [[ 12.0, 0.0, 0.0],
    [ 0.0, 10.0, 0.0],
    [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu']
atom_files = [ 'Cu.py']
atom_files_dir = './'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.08333333333333333, 0.0, 0.0],
    [ 0.16666666666666666, 0.0, 0.0],
    [ 0.25, 0.0, 0.0],
    [ 0.3333333333333333, 0.0, 0.0],
    [ 0.4166666666666667, 0.0, 0.0],
    [ 0.5, 0.0, 0.0],
    [ 0.5833333333333334, 0.0, 0.0],
    [ 0.6666666666666666, 0.0, 0.0],
    [ 0.75, 0.0, 0.0],
    [ 0.8333333333333334, 0.0, 0.0],
    [ 0.9166666666666666, 0.0, 0.0]]
temperature = 0.001
num_electrons = 6.0
num_bands = None
use_spin = True
orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 288, 1, 1]
use_kpts_symmetry = False
num_kpts_procs = 6
use_hubbard_U = True
spin_up_site_density = [ 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0,
     0.5, 0.0]
spin_down_site_density = [ 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5,
     0.0, 0.5]
do_electron_scf = False
electron_fixed_fermi_energy = False
calc_electron_fermi_surface = True
electron_delta_width = 0.025
electron_dos_step = 0.01
electron_output_file = 'nscf_n_12_h_0.5000.hdf5'
write_electron_eigenvectors = False
write_site_density = True
electron_eigenvectors_input_file = None
site_density_input_file = 'restart_n_12_h_0.5000.hdf5'
job_description = None
write_kpts_hdf5_file = False
_plot_electron_bands = False
_write_kpts = False
