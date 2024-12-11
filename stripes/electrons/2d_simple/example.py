import numpy as np


class c_simple:

    # ----------------------------------------------------------------------------------------------

    def __init__(self):

        """
        solve simple model to calculate some curves
        """

        pass

    # ----------------------------------------------------------------------------------------------

    def _solve_k(self,kx,ky):

        """
        solve hamiltonian for given kx and ky (in units 2pi/a, a=1)
        """

        return -2*(np.cos(2*np.pi*kx)+np.cos(2*np.pi*ky))

    # ----------------------------------------------------------------------------------------------
        
    def _get_kpts_mesh(self,nx,ny):

        """
        get mesh of kpts given nx and ny
        """
             
        _nx = nx // 2
        if nx % 2 == 0:
            _kx = np.arange(-_nx+1,_nx+1).astype(float)
        else:
            _kx = np.arange(-_nx,_nx+1,1).astype(float)

        _ny = ny // 2
        if ny % 2 == 0:
            _ky = np.arange(-_ny+1,_ny+1).astype(float)
        else:
            _ky = np.arange(-_ny,_ny+1,1).astype(float)

        _kx /= nx; _ky /= ny
        _kx, _ky = np.meshgrid(_kx,_ky,indexing='ij')

        _kx = _kx.flatten(); _ky = _ky.flatten()
        num_kpts = _kx.size

        return np.c_[_kx,_ky], num_kpts
        
    # ----------------------------------------------------------------------------------------------

    def solve_on_kpts(self,kpts,num_kpts):

        """
        loop over kpts and solve 
        """

        evals = np.zeros(num_kpts,dtype=float)

        for ii in range(num_kpts):
            evals[ii] = self._solve_k(*kpts[ii,:])

        return evals

    # ----------------------------------------------------------------------------------------------

    def calculate_fermi_energy(self,num_elec=0.5,nx=100,ny=100,T=0.01):

        """
        use bisection algorithm to calculate fermi level for given num_elec fraction
        """

        kpts, num_kpts = self._get_kpts_mesh(nx,ny)

        evals = self.solve_on_kpts(kpts,num_kpts)

        _bracket = np.array([evals.min(),evals.max()])
        fermi_energy = _bracket.mean()

        _tol = 1e-4
        _max_iter = 1000
        for ii in range(_max_iter):
        
            #_occupations = 2*(evals < fermi_energy).astype(float) # spin degenerate
            _occupations = 2/(np.exp(evals-fermi_energy/T)+1)
            _num_elec = _occupations.sum()/num_kpts

            print(_num_elec)

            _err = _num_elec-num_elec
            _residual = np.abs(_err)

            if _residual < _tol:
                break

            if _err > 0:
                _bracket[1] = np.copy(fermi_energy)
            else:
                _bracket[0] = np.copy(fermi_energy)

            fermi_energy = _bracket.mean() 

        if ii+1 == _max_iter:
            print('didnt coverge!')

        print('fermi_energy:',fermi_energy)

    # ----------------------------------------------------------------------------------------------


    # ----------------------------------------------------------------------------------------------

if __name__ == '__main__':

    model = c_simple()
    model.calculate_fermi_energy(1,100,100)



