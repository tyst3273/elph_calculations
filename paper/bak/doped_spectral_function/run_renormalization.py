
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.plot_fs import plot_fs
from plot_renormalized_neutrons import plot_renormalized_neutrons

# --------------------------------------------------------------------------------------------------

def run_g2x_calc(U,n,order,input_file='renorm_g2x_template.py'):

    output_file = f'renorm_g2x/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'

    kwargs = {'num_electrons':n,
              'site_density_input_file':f'scf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5',
              'electron_output_file':'tmp.hdf5',
              'elph_output_file':output_file,
              'kpts_mesh':[100,100,1]}

    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # plot_renormalized_neutrons(output_file,mode='fb',show=False)
    # plot_renormalized_neutrons(output_file,mode='qp',show=False)

# --------------------------------------------------------------------------------------------------

def run_g2m_calc(U,n,order,input_file='renorm_g2m_template.py'):

    output_file = f'renorm_g2m/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'

    kwargs = {'num_electrons':n,
              'site_density_input_file':f'scf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5',
              'electron_output_file':'tmp.hdf5',
              'elph_output_file':output_file,
              'kpts_mesh':[100,100,1]}

    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # plot_renormalized_neutrons(output_file,mode='hb',show=False)

# --------------------------------------------------------------------------------------------------

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

    run_g2x_calc(U,n,order)
    run_g2m_calc(U,n,order)
    
# --------------------------------------------------------------------------------------------------



