
import numpy as np
import matplotlib.pyplot as plt
import os

# custom modules
from elph.drivers.m_ELPH import c_ELPH

# --------------------------------------------------------------------------------------------------

def run_calc(n,order,input_file='electron_scf_restart.py'):

    kwargs = {'num_electrons':n,
              'site_density_input_file':f'scf/{order}_N_{n:3.2f}.hdf5',
              'electron_output_file':f'scf_restart/{order}_N_{n:3.2f}.hdf5'}

    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

# --------------------------------------------------------------------------------------------------

# parameters to sweep
n_arr = np.linspace(0,2,21)[1:]
num_calcs = n_arr.size
print('\nn_arr:\n',n_arr)

orders = ['afm','pm','fm','fim','cdw']

for ii in range(num_calcs):

    n = n_arr[ii]

    print(f'\nnow on num {ii}/{num_calcs}')
    print(f'n: {n:.3f}')

    for order in orders:
        run_calc(n,order)

# --------------------------------------------------------------------------------------------------



