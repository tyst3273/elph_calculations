# linewidths converged-ish for phonon_self_energy_width = 0.01, kpts_mesh = [250,250,1]
# spectral function converged-ish for phonon_self_energy_eps = 0.0075 and kpts_mesh = [400,400,1]
# but doing coarse grid now for faster calcs

#debug = True

task = 'electrons'
temperature = 0.01

use_spin = True
use_hubbard_U = True

num_electrons = 1.8

atom_files = ['Cu.py','O.py']
lattice_vectors = [[ 2**(1/2),     0.00,     0.00],
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]
atom_types = ['Cu','Cu','O','O','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00],
                  [0.25,0.25,0.00],
                  [0.75,0.25,0.00],
                  [0.25,0.75,0.00],
                  [0.75,0.75,0.00]]

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [200,200,1] 
num_kpts_procs = 4

hopping_file = 'hopping.py'

do_electron_scf = False

electron_dos_step = 0.001
electron_delta_width = 0.1
#_plot_electron_bands = True

#electron_fixed_fermi_energy = 0.0

site_density_input_file = 'scf.hdf5'
electron_output_file = 'nscf.hdf5'

electron_delta_width = 0.01
calc_electron_fermi_surface = True


