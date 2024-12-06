# linewidths converged-ish for phonon_self_energy_width = 0.01, kpts_mesh = [250,250,1]
# spectral function converged-ish for phonon_self_energy_eps = 0.0075 and kpts_mesh = [400,400,1]
# but doing coarse grid now for faster calcs

debug = True

task = 'neutron_scattering' 
temperature = 0.01

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

num_qpts_procs = 4 #10
qpts_option = 'path'
qpts_path = [[   4,   0,   0],
             [   8,   0,   0]]
qpts_steps = 201

spring_constants_file = 'spring_constants.py'

#_plot_phonon_bands = True

neutron_energy_step = 0.001
neutron_delta_width = 0.0025

phonon_output_file = 'neutrons.hdf5'
