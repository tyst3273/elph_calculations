task = 'electrons'
debug = False
atom_positions_file = None
lattice_vectors = [[ 21.0, 0.0, 0.0],
    [ 0.0, 10.0, 0.0],
    [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu']
atom_files = [ 'Cu.py']
atom_files_dir = './'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.047619047619047616, 0.0, 0.0],
    [ 0.09523809523809523, 0.0, 0.0],
    [ 0.14285714285714285, 0.0, 0.0],
    [ 0.19047619047619047, 0.0, 0.0],
    [ 0.23809523809523808, 0.0, 0.0],
    [ 0.2857142857142857, 0.0, 0.0],
    [ 0.3333333333333333, 0.0, 0.0],
    [ 0.38095238095238093, 0.0, 0.0],
    [ 0.42857142857142855, 0.0, 0.0],
    [ 0.47619047619047616, 0.0, 0.0],
    [ 0.5238095238095238, 0.0, 0.0],
    [ 0.5714285714285714, 0.0, 0.0],
    [ 0.6190476190476191, 0.0, 0.0],
    [ 0.6666666666666666, 0.0, 0.0],
    [ 0.7142857142857143, 0.0, 0.0],
    [ 0.7619047619047619, 0.0, 0.0],
    [ 0.8095238095238095, 0.0, 0.0],
    [ 0.8571428571428571, 0.0, 0.0],
    [ 0.9047619047619048, 0.0, 0.0],
    [ 0.9523809523809523, 0.0, 0.0]]
temperature = 0.001
num_electrons = 18.2
num_bands = None
use_spin = True
orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 218, 1, 1]
use_kpts_symmetry = False
num_kpts_procs = 6
use_hubbard_U = True
spin_up_site_density = [ 0.8666666666666666, 0.0, 0.8666666666666666, 0.0,
     0.8666666666666666, 0.0, 0.8666666666666666, 0.0, 0.8666666666666666, 0.0,
     0.8666666666666666, 0.0, 0.8666666666666666, 0.0, 0.8666666666666666, 0.0,
     0.8666666666666666, 0.0, 0.8666666666666666, 0.0, 0.8666666666666666]
spin_down_site_density = [ 0.0, 0.8666666666666666, 0.0, 0.8666666666666666,
     0.0, 0.8666666666666666, 0.0, 0.8666666666666666, 0.0, 0.8666666666666666,
     0.0, 0.8666666666666666, 0.0, 0.8666666666666666, 0.0, 0.8666666666666666,
     0.0, 0.8666666666666666, 0.0, 0.8666666666666666, 0.0]
do_electron_scf = False
electron_fixed_fermi_energy = False
calc_electron_fermi_surface = True
electron_delta_width = 0.025
electron_dos_step = 0.01
electron_output_file = 'nscf_n_21_h_0.1333.hdf5'
write_electron_eigenvectors = False
write_site_density = True
electron_eigenvectors_input_file = None
site_density_input_file = 'restart_n_21_h_0.1333.hdf5'
job_description = None
write_kpts_hdf5_file = False
_plot_electron_bands = False
_write_kpts = False