
import numpy as np
import matplotlib.pyplot as plt
import os

# custom modules
from elph.drivers.m_ELPH import c_ELPH

# --------------------------------------------------------------------------------------------------

def run_calc(n,order,input_file='electron_scf.py'):

    if order == 'cdw':
        spin_up_site_density =   [ 1, 0] #, 0,0,0,0]
        spin_down_site_density = [ 1, 0] #, 0,0,0,0]
    elif order == 'pm':
        spin_up_site_density =   [ 1, 1] #, 0,0,0,0]
        spin_down_site_density = [ 1, 1] #, 0,0,0,0]
    elif order == 'afm':
        spin_up_site_density =   [ 1, 0] #, 0,0,0,0]
        spin_down_site_density = [ 0, 1] #, 0,0,0,0]
    elif order == 'fm':
        spin_up_site_density =   [ 1, 1] #, 0,0,0,0]
        spin_down_site_density = [ 0, 0] #, 0,0,0,0]
    elif order == 'fim':
        spin_up_site_density =   [ 2, 0] #, 0,0,0,0]
        spin_down_site_density = [ 0, 1] #, 0,0,0,0]

    kwargs = {'num_electrons':n,
              'spin_up_site_density':spin_up_site_density,
              'spin_down_site_density':spin_down_site_density,
              'electron_output_file':f'scf/{order}_N_{n:3.2f}.hdf5'}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

# --------------------------------------------------------------------------------------------------

# parameters to sweep
n_arr = np.linspace(0.25,0.75,41)*4
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



