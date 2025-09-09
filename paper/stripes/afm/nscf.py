task = 'electrons'
debug = False
atom_positions_file = None
lattice_vectors = [[ 2.0**(1/2), 0.0, 0.0],
    [ 0.0, 2.0**(1/2), 0.0],
    [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'Cu' ]
atom_positions = [[ 0.0, 0.0, 0.0],[0.5, 0.5, 0.0]]
atom_files = ['Cu.py']
temperature = 0.001
num_electrons = 2.0
use_spin = True
orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 400, 400, 1]
use_kpts_symmetry = False
num_kpts_procs = 4
use_hubbard_U = True
do_electron_scf = False
calc_electron_fermi_surface = True
electron_dos_step = 0.01
electron_delta_width = 0.025
electron_output_file = 'nscf_afm.hdf5'
site_density_input_file = 'scf_afm.hdf5'
write_electron_eigenvectors = False
write_site_density = True
