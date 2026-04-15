
debug = False


_s_ = 1/2**(1/2)
atom_files = ['Cu.py','O.py']
lattice_vectors = [[   _s_,  _s_,  0],
                   [  -_s_,  _s_,  0],
                   [    0,   0, 10]]
atom_types = ['Cu','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.00,0.00],
                  [0.00,0.50,0.00]]
                
spin_up_site_density = [1, 0, 0]
spin_down_site_density = [1, 0, 0]

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [100,100,1]

num_kpts_procs = 8

use_hubbard_U = True
use_spin = True

do_electron_scf = False
max_electron_scf_steps = 400

temperature = 0.001

write_electron_eigenvectors = True

electron_output_file = 'scf.hdf5'

num_electrons = 0.95


