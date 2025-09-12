
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np

# --------------------------------------------------------------------------------------------------

def run_calc(U,n,order,input_file='scf_template.py'):

    if order == 'afm':
        spin_up_site_density =   [ 1, 0]
        spin_down_site_density = [ 0, 1]
    elif order == 'fim':
        spin_up_site_density =   [ 2, 0]
        spin_down_site_density = [ 0, 1]

    kwargs = {'num_electrons':n,
              'spin_up_site_density':spin_up_site_density,
              'spin_down_site_density':spin_down_site_density,
              'electron_output_file':f'scf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

# --------------------------------------------------------------------------------------------------

    # PM-M: x=0.25, U=4
    # AMF-M: x=0.4, U=4
    # FiM-M: x=0.45, U=6
    # AFM-I: x=0.5, U=6
    # FM-M: x=0.25, U=10

# parameters to sweep
calcs = [[ 0.5,   0.5, 'afm'],
         [ 0.5,   0.6, 'afm'],
         [ 0.5,   0.7, 'afm'],
         [ 0.5,   0.8, 'afm'],
         [ 0.5,   0.9, 'afm'],
         [ 0.5,   1.0, 'afm'],
         [ 0.5,   1.1, 'afm'],
         [ 0.5,   1.2, 'afm'],
         [ 0.5,   1.3, 'afm'],
         [ 0.5,   1.4, 'afm'],
         [ 0.5,   1.5, 'afm'],
         [ 0.5,   2.0, 'afm'],
         [0.475,    2, 'afm'],
         [0.45,     3, 'afm'],
         [ 0.4,     4, 'afm'],
         [ 0.3,     7, 'afm'],
          [0.4,     5, 'fim'],
          [0.4,     6, 'fim'],
          [0.4,     7, 'fim'],
         [0.475,    3, 'fim'],
         [0.475,    4, 'fim'],
         [0.475,    5, 'fim'],
         [0.475,   10, 'fim'],
         [0.475,   20, 'fim'],
         [0.45,     4, 'fim'],
         [0.45,     5, 'fim'],
         [0.45,     6, 'fim'],
         [0.45,    10, 'fim']]   
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

    run_calc(U,n,order)

# --------------------------------------------------------------------------------------------------



