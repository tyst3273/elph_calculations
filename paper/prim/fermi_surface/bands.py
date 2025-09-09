
debug = False

lattice_vectors = [[     1.00,     0.00,     0.00], 
                   [     0.00,     1.00,     0.00],
                   [     0.00,     0.00,    10.00]]

atom_types = ['Cu']
atom_positions = [0.00,0.00,0.00]
atom_files = ['Cu.py']

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'path'
kpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0],
             [ 1/2, 1/2,   0],
             [   0,   0,   0]]
kpts_steps = 51
num_kpts_procs = 4

_plot_electron_bands = True

electron_fixed_fermi_energy = 0.0

do_electron_scf = False #True
temperature = 0.001
num_electrons = 1

#write_site_density = True
electron_output_file = 'bands.hdf5'
#site_density_input_file =  '_den'

