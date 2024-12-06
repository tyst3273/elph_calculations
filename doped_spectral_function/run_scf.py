
# custom modules
from elph.drivers.m_ELPH import c_ELPH

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
calcs = [[0.10,'pm'], [0.30,'pm'], [0.50,'pm'],  [0.70,'pm'],  [0.90,'pm'],
         [1.10,'pm'], [1.30,'pm'], [1.50,'afm'], [1.70,'fim'], [1.90,'fim']]
num_calcs = len(calcs)

U = 5.0

for ii in range(num_calcs):

    n = calcs[ii][0] 
    order = calcs[ii][1]

    print(f'\nnow on num {ii}/{num_calcs}')
    print('n:',n)
    print('order:',order)

    run_calc(U,n,order)

# --------------------------------------------------------------------------------------------------



