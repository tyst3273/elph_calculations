
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



