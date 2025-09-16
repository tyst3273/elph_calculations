
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np
import time
import os 

# --------------------------------------------------------------------------------------------------

def run_calc(U,n,order,input_file='bands_template.py'):

    kwargs = {'num_electrons':n,
              'site_density_input_file':f'nscf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5',
              'electron_output_file':f'bands/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    del ELPH

# --------------------------------------------------------------------------------------------------

# parameters to sweep
# calcs = [[ 0.5,   0.5, 'afm'],
#          [ 0.5,   0.6, 'afm'],
#          [ 0.5,   0.7, 'afm'],
#          [ 0.5,   0.8, 'afm'],
#          [ 0.5,   0.9, 'afm'],
#          [ 0.5,   1.0, 'afm'],
#          [ 0.5,   1.1, 'afm'],
#          [ 0.5,   1.2, 'afm'],
#          [ 0.5,   1.3, 'afm'],
#          [ 0.5,   1.4, 'afm'],
#          [ 0.5,   1.5, 'afm'],
#          [ 0.5,   2.0, 'afm'],
#          [0.475,    2, 'afm'],
#          [0.45,     3, 'afm'],
#          [ 0.4,     4, 'afm'],
#          [ 0.3,     7, 'afm'],
#           [0.4,     5, 'fim'],
#           [0.4,     6, 'fim'],
#           [0.4,     7, 'fim'],
#          [0.475,    3, 'fim'],
#          [0.475,    4, 'fim'],
#          [0.475,    5, 'fim'],
#          [0.475,   10, 'fim'],
#          [0.475,   20, 'fim'],
#          [0.45,     4, 'fim'],
#          [0.45,     5, 'fim'],
#          [0.45,     6, 'fim'],
#          [0.45,    10, 'fim']]   
calcs = [[ 0.5,   2.5, 'afm'],
         [ 0.5,   3.0, 'afm'],
         [ 0.5,   3.5, 'afm'],
         [ 0.5,   4.0, 'afm'],
         [ 0.5,   4.5, 'afm'],
         [ 0.5,   5.0, 'afm']]
num_calcs = len(calcs)

with open('Cu_template.py','r') as f:
    template = f.read()

for ii in range(num_calcs):
    
    n, U, order = calcs[ii]

    n *= 4.0

    print(f'\nnow on num {ii}/{num_calcs}')
    print('n:',n)
    print('U:',U)
    print('order:',order)

    # have to write U to the atom file ...
    with open('Cu.py','w') as f:
        f.write(template)
        f.write(f'hubbard_U = [{U:.6f}]\n')
        os.fsync(f.fileno())

    # have to sleep or the wrong U is read for some reason ...
    time.sleep(1.0)

    run_calc(U,n,order)

# --------------------------------------------------------------------------------------------------



