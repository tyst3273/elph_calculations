
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np

# --------------------------------------------------------------------------------------------------

def run_calc(U,n,order,input_file='scf_template.py'):

    
    if order == 'pm':
        spin_up_site_density =   [ 1, 0,0]
        spin_down_site_density = [ 1, 0,0]
    elif order == 'fm':
        spin_up_site_density =   [ 1, 0,0]
        spin_down_site_density = [ 0, 0,0]

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
calcs = [[0.01,   0, 'pm'],
            [ 0.10,   0, 'pm'],
            [ 0.20,   0, 'pm'],
            [ 0.25,   0, 'pm'],
            [ 0.30,   0, 'pm'],
            [ 0.40,   0, 'pm'],
            [ 0.50,   0, 'pm'],
            [ 0.01,  15, 'fm'],
            [ 0.10,  15, 'fm'],
            [ 0.20,  15, 'fm'],
            [ 0.25,  15, 'fm'],
            [ 0.30,  15, 'fm'],
            [ 0.40,  15, 'fm'],
            [ 0.45,  15, 'fm']]
num_calcs = len(calcs)

with open('Cu_template.py','r') as f:
    template = f.read()

for ii in range(num_calcs):
    
    n, U, order = calcs[ii]

    n *= 2.0

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



