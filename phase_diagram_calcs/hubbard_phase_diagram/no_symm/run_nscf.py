
import numpy as np
import matplotlib.pyplot as plt
import os

# custom modules
from elph.drivers.m_ELPH import c_ELPH

# --------------------------------------------------------------------------------------------------

def run_calc(U,n,order,input_file='electron_nscf.py'):

    kwargs = {'num_electrons':n,
              'site_density_input_file':f'scf_restart/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5',
              'electron_output_file':f'nscf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'}

    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

# --------------------------------------------------------------------------------------------------

# parameters to sweep
U_arr = np.linspace(0,20,41)
n_arr = np.linspace(0,2,21)[1:]

print('\nU_arr:\n',U_arr)
print('\nn_arr:\n',n_arr)

n_arr, U_arr = np.meshgrid(n_arr,U_arr,indexing='ij')
n_arr = n_arr.flatten(); U_arr = U_arr.flatten()
num_calcs = n_arr.size

orders = ['afm','pm','fm','fim']

with open('Cu_template.py','r') as f:
    template = f.read()

for ii in range(num_calcs):

    U = U_arr[ii]
    n = n_arr[ii]

    print(f'\nnow on num {ii}/{num_calcs}')
    print(f'U: {U:.3f}')
    print(f'n: {n:.3f}')

    # have to write U to the atom file ...
    with open('Cu.py','w') as f:
        f.write(template)
        f.write(f'hubbard_U = [{U:.6f}]\n')

    for order in orders:
        run_calc(U,n,order)

# --------------------------------------------------------------------------------------------------



