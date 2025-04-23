
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.plot_fs import plot_fs
from plot_renormalized_neutrons import plot_renormalized_neutrons

# --------------------------------------------------------------------------------------------------

def run_g2x_calc(U,n,order,input_file='renorm_g2x_template.py'):

    output_file = f'renorm_g2x/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'

    kwargs = {'num_electrons':n,
              'site_density_input_file':f'nscf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5',
              'electron_output_file':'tmp.hdf5',
              'elph_output_file':output_file,
              'kpts_mesh':[50,50,1]}

    #ELPH = c_ELPH(input_file)
    #ELPH.set_config(**kwargs)
    #ELPH.run()

    plot_renormalized_neutrons(output_file,mode='fb',show=False)
    plot_renormalized_neutrons(output_file,mode='qp',show=False)

# --------------------------------------------------------------------------------------------------

def run_g2m_calc(U,n,order,input_file='renorm_g2m_template.py'):

    output_file = f'renorm_g2m/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'

    kwargs = {'num_electrons':n,
              'site_density_input_file':f'nscf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5',
              'electron_output_file':'tmp.hdf5',
              'elph_output_file':output_file,
              'kpts_mesh':[50,50,1]}

    #ELPH = c_ELPH(input_file)
    #ELPH.set_config(**kwargs)
    #ELPH.run()

    plot_renormalized_neutrons(output_file,mode='hb',show=False)

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

    run_g2x_calc(U,n,order)
    run_g2m_calc(U,n,order)

# --------------------------------------------------------------------------------------------------



