task = 'electrons'
debug = False
atom_positions_file = None
atom_files = [ 'Cu.py','O.py']
temperature = 0.001
num_electrons = 48
use_spin = True
orbital_type = 'tight_binding'
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 100, 100, 1]
use_kpts_symmetry = False
num_kpts_procs = 6
use_hubbard_U = True
site_density_input_file = 'scf_n_8_h_0.2500.hdf5'
do_electron_scf = False
electron_output_file = 'nscf_n_8_h_0.2500.hdf5'
write_electron_eigenvectors = False
write_site_density = True
_plot_electron_bands = False
electron_dos_step = 0.01
electron_delta_width = 0.025
calc_electron_fermi_surface = True
