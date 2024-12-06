
debug = True

task = 'neutron_scattering' 
temperature = 0.01

num_qpts_procs = 8 #10
qpts_option = 'path'
qpts_path = [[   8,   8,   0],
             [  16,  16,   0]]
qpts_steps = 101 #8*2*50+1

spring_constants_file = 'spring_constants.py'

neutron_energy_step = 0.001
neutron_delta_width = 0.0025

phonon_output_file = 'neutrons.hdf5'
