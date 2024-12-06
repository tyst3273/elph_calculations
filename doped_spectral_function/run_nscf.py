
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.plot_fs import plot_fs

# --------------------------------------------------------------------------------------------------

def run_calc(U,n,order,input_file='nscf_template.py'):

    output_file = f'nscf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'
    kwargs = {'num_electrons':n,
              'site_density_input_file':f'scf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5',
              'electron_output_file':output_file}

    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    plot_fs(output_file,show=False)

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



