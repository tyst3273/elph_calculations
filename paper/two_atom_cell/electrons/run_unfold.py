

from m_unfold_electrons import unfold_bands

from calcs import calcs

# --------------------------------------------------------------------------------------------------

num_calcs = len(calcs)

for ii in range(num_calcs):
    
    n, U, order = calcs[ii]

    n *= 4.0

    print(f'\nnow on num {ii}/{num_calcs}')
    print('n:',n)
    print('U:',U)
    print('order:',order)

    bands_file = f'bands/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'
    nscf_file = f'nscf/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5'

    prim_n = n / 2.0
    prim_bands_file = f'unfold/bands/pm_U_{U:3.2f}_N_{prim_n:3.2f}.hdf5'
    prim_nscf_file = f'unfold/nscf/pm_U_{U:3.2f}_N_{prim_n:3.2f}.hdf5'

    unfold_bands(bands_file,nscf_file,prim_bands_file,prim_nscf_file)

# --------------------------------------------------------------------------------------------------



