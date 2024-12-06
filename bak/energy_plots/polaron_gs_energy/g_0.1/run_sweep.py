
import numpy as np
import matplotlib.pyplot as plt

# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph.io.m_command_line import get_input_files

# --------------------------------------------------------------------------------------------------

input_file = 'input.py'

#U_arr = np.linspace(4,10,61)
U_arr = np.linspace(0,4,41)
num_calcs = U_arr.size

# initial guesses for density
fm_up = [0.8, 0.8, 0.0,0.0,0.0,0.0]
fm_down = [0.2, 0.2, 0.0,0.0,0.0,0.0]

afm_up = [0.8, 0.2, 0.0,0.0,0.0,0.0]
afm_down = [0.2, 0.8, 0.0,0.0,0.0,0.0]

pm_up = [0.5, 0.5, 0.0,0.0,0.0,0.0]
pm_down = [0.5, 0.5, 0.0,0.0,0.0,0.0]

fim_up = [0.8, 0.2, 0.0,0.0,0.0,0.0]
fim_down = [0.2, 0.2, 0.0,0.0,0.0,0.0]

cdw_up = [0.8, 0.2, 0.0,0.0,0.0,0.0]
cdw_down = [0.8, 0.2, 0.0,0.0,0.0,0.0]

# calc options
dense_mesh = [100,100,1]
use_kpts_symmetry = True

# --------------------------------------------------------------------------------------------------

with open('Cu_template.py','r') as f:
    template = f.read()

for ii in range(num_calcs):

    U = U_arr[ii]

    print(f'\nnow on num {ii}/{num_calcs}')
    print(f'U: {U:.3f}')

    # have to write U to the atom file ...
    with open('Cu.py','w') as f:
        f.write(template)
        f.write(f'hubbard_U = [{U:.6f}]\n')

    # ----------------------------------------------------------------------------------------------

    coarse_file = f'afm_coarse_U{U:.3f}.hdf5'
    dense_file = f'afm_dense_U{U:.3f}.hdf5'

    # afm -- scf
    kwargs = {'electron_output_file':coarse_file,
              'spin_up_site_density':afm_up,
              'spin_down_site_density':afm_down,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # afm -- scf
    kwargs = {'electron_output_file':dense_file,
              'site_density_input_file':coarse_file,
              'kpts_mesh':dense_mesh,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # ----------------------------------------------------------------------------------------------

    coarse_file = f'fm_coarse_U{U:.3f}.hdf5'
    dense_file = f'fm_dense_U{U:.3f}.hdf5'

    # fm -- scf
    kwargs = {'electron_output_file':coarse_file,
              'spin_up_site_density':fm_up,
              'spin_down_site_density':fm_down,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # fm -- scf
    kwargs = {'electron_output_file':dense_file,
              'site_density_input_file':coarse_file,
              'kpts_mesh':dense_mesh,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # ----------------------------------------------------------------------------------------------

    coarse_file = f'pm_coarse_U{U:.3f}.hdf5'
    dense_file = f'pm_dense_U{U:.3f}.hdf5'

    # pm -- scf
    kwargs = {'electron_output_file':coarse_file,
              'spin_up_site_density':pm_up,
              'spin_down_site_density':pm_down,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # pm -- scf
    kwargs = {'electron_output_file':dense_file,
              'site_density_input_file':coarse_file,
              'kpts_mesh':dense_mesh,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # ----------------------------------------------------------------------------------------------

    coarse_file = f'fim_coarse_U{U:.3f}.hdf5'
    dense_file = f'fim_dense_U{U:.3f}.hdf5'

    # fim -- scf
    kwargs = {'electron_output_file':coarse_file,
              'spin_up_site_density':fim_up,
              'spin_down_site_density':fim_down,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # fim -- scf
    kwargs = {'electron_output_file':dense_file,
              'site_density_input_file':coarse_file,
              'kpts_mesh':dense_mesh,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # ----------------------------------------------------------------------------------------------

    coarse_file = f'cdw_coarse_U{U:.3f}.hdf5'
    dense_file = f'cdw_dense_U{U:.3f}.hdf5'

    # fim -- scf
    kwargs = {'electron_output_file':coarse_file,
              'spin_up_site_density':cdw_up,
              'spin_down_site_density':cdw_down,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # fim -- scf
    kwargs = {'electron_output_file':dense_file,
              'site_density_input_file':coarse_file,
              'kpts_mesh':dense_mesh,
              'use_kpts_symmetry':use_kpts_symmetry}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # ----------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------





