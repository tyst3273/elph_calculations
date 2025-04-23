
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np

# --------------------------------------------------------------------------------------------------

def run_calc(U,n,order,input_file='nscf_template.py'):


    kwargs = {'num_electrons':n,
              'site_density_input_file':f'scf_restart/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5',
              'electron_output_file':f'nscf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

# --------------------------------------------------------------------------------------------------

# parameters to sweep
calcs = [[0.25,4,'pm'],
         [0.4,4,'afm'],
         [0.45,6,'fim'],
         [0.5,6,'afm'],
         [0.25,10,'fm']]
num_calcs = len(calcs)

for ii in range(num_calcs):
    
    n, U, order = calcs[ii]

    n *= 4.0

    print(f'\nnow on num {ii}/{num_calcs}')
    print('n:',n)
    print('U:',U)
    print('order:',order)

    run_calc(U,n,order)

# --------------------------------------------------------------------------------------------------



