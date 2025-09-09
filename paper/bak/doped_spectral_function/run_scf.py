
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np

# --------------------------------------------------------------------------------------------------

def run_calc(U,n,order,input_file='scf_template.py'):

    if order == 'cdw':
        spin_up_site_density =   [ 1, 0, 0,0,0,0]
        spin_down_site_density = [ 1, 0, 0,0,0,0]
    elif order == 'pm':
        spin_up_site_density =   [ 1, 1, 0,0,0,0]
        spin_down_site_density = [ 1, 1, 0,0,0,0]
    elif order == 'afm':
        spin_up_site_density =   [ 1, 0, 0,0,0,0]
        spin_down_site_density = [ 0, 1, 0,0,0,0]
    elif order == 'fm':
        spin_up_site_density =   [ 1, 1, 0,0,0,0]
        spin_down_site_density = [ 0, 0, 0,0,0,0]
    elif order == 'fim':
        spin_up_site_density =   [ 2, 0, 0,0,0,0]
        spin_down_site_density = [ 0, 1, 0,0,0,0]

    kwargs = {'num_electrons':n,
              'spin_up_site_density':spin_up_site_density,
              'spin_down_site_density':spin_down_site_density,
              'electron_output_file':f'scf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

# --------------------------------------------------------------------------------------------------

# parameters to sweep
calcs = [[0.2,  4, 'pm'],
         [0.3,  4, 'pm'],
         [0.4,  4, 'afm'],
         [0.45, 4, 'fim'],
         [0.5,  4, 'afm'],
         [0.2,  8, 'pm'],
         [0.3,  8, 'fm'],
         [0.4,  8, 'fim'],
         [0.45, 8, 'fim'],
         [0.5,  8, 'afm']]
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



