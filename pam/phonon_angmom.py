
import matplotlib.pyplot as plt
import numpy as np
import h5py 


# --------------------------------------------------------------------------------------------------

class c_connectivity:

    # ----------------------------------------------------------------------------------------------

    def __init__(self,filename='phonons.hdf5'):

        """
        """

        with h5py.File(filename,'r') as db:

            # [qpts, bands, basis] : note that bands/basis order backwards from common definition
            self.evecs = db['eigenvectors'][...] 

            # [qpts, bands] 
            self.freqs = db['frequencies'][...]

            self.masses = db['atom_masses'][...]

            self.qpts = db['qpts_rlu'][...]
            self.qpts_dists = db['qpts_distances'][...]
            self.qpts_verts = db['qpts_vert_distances'][...]

        self.num_qpts, self.num_bands, self.num_basis = self.evecs.shape
        self.num_atoms = self.num_basis // 3

        self.effective_charges = np.array([-2, -2, 1, 1, 1, 1],dtype=float)

        # self._calc_pam()

        # find all the degeneracies
        self._find_all_degeneracies()

    # ----------------------------------------------------------------------------------------------

    def _calc_pam(self):

        self.pam = np.zeros(self.freqs.shape)

        for qq in range(self.num_qpts):
            for vv in range(self.num_bands):

                _eqv = self.evecs[qq,vv,...].reshape(self.num_atoms,3)

                for aa in range(self.num_atoms):
                    _eqva = _eqv[aa,:]
                    self.pam[qq,vv] += np.imag( np.cross(_eqva.conj().T,_eqva) )[2]

        ### DEV ###
        fig, ax = plt.subplots(figsize=(4.5,4.5))
        for vv in range(self.num_bands):
            ax.plot(self.qpts_dists,self.freqs[:,vv],c='k',lw=0,ms=1)
            _hi = self.freqs[:,vv] + self.pam[:,vv]
            _lo = self.freqs[:,vv] - self.pam[:,vv]
            ax.fill_between(self.qpts_dists,_hi,_lo)
        plt.show()
        ### DEV ###

    # ----------------------------------------------------------------------------------------------

    def _find_all_degeneracies(self):

        """
        loop over all q-points and find any degeneracies -- only works for unconnected bands since
        this algo assumes that the bands are sorted in ascending order of frequency
        """

        self.num_degen_manifolds = []
        self.manifold_sizes = []
        self.manifold_freqs = []
        self.manifolds = []

        self.has_degeneracies = np.zeros(self.num_qpts,dtype=bool) * False

        for ii in range(self.num_qpts):

            _freqs = self.freqs[ii,:]
            _num_degen, _sizes, _freqs, _manifolds = \
                self._find_degenerate_manifolds(_freqs)
            
            if _num_degen != 0:
                self.has_degeneracies[ii] = True

            self.num_degen_manifolds.append(_num_degen)
            self.manifold_sizes.append(_sizes)
            self.manifold_freqs.append(_freqs)
            self.manifolds.append(_manifolds)

    # ----------------------------------------------------------------------------------------------

    def _find_degenerate_manifolds(self,freqs,cutoff=1e-6):

        """
        find degenerate modes at the given kpoint
        """

        _diff = freqs[1:]-freqs[:-1] 

        manifolds = []
        _manifold = [0]
        for ii in range(self.num_bands-1):

            if _diff[ii] < cutoff:
                _manifold.append(ii+1)
                if ii == self.num_bands-2:
                    manifolds.append(_manifold)

            else:
                manifolds.append(_manifold)
                _manifold = [ii+1]

        num_manifolds = len(manifolds)
        manifold_sizes = np.zeros(num_manifolds,dtype=int)
        manifold_freqs = np.zeros(num_manifolds,dtype=float)
        for ii in range(num_manifolds):

            manifold_freqs[ii] = freqs[manifolds[ii][0]]

            _n = len(manifolds[ii])
            manifold_sizes[ii] = _n

        num_degen_manifolds = np.count_nonzero(manifold_sizes-1)
        
        # number of denerate manifold, the number of states in each manifold, the frequency of
        # each manifold, and the manifolds
        return num_degen_manifolds, manifold_sizes, manifold_freqs, manifolds
    
    # ----------------------------------------------------------------------------------------------

    def apply_field_pert(self,B=[0,0,1]):

        """
        apply magnetic field as a perturbation and lift the degeneracy of chiral modes
        """

        B = np.array(B)

        _gamma = self._fill_gamma_matrix(B)

        self.new_freqs = np.zeros(self.freqs.shape,dtype=float) 
        self.new_evecs = np.zeros(self.evecs.shape,dtype=complex)
        for qq in range(self.num_qpts):
            
            _num_degen = self.num_degen_manifolds[qq]
            _degen_sizes = self.manifold_sizes[qq]
            _degen_freqs = self.manifold_freqs[qq]
            _degen_manifolds = self.manifolds[qq]

            _eq = self.evecs[qq,...]

            for bb, _manifold in enumerate(_degen_manifolds):
                
                _w = _degen_freqs[bb]
                _s = _degen_sizes[bb]
                if _s == 1 or _w < 1e-3:
                    self.new_evecs[qq,_manifold] = self.evecs[qq,_manifold,:]
                    self.new_freqs[qq,_manifold] = self.freqs[qq,_manifold]
                    continue
                    
                _D = np.eye(_s) * _w**2
                
                _pert = np.zeros(_D.shape,dtype=complex)
                for ii in range(2):
                    for jj in range(2):
                        _ei = _eq[ii,:].conj().T
                        _ej = _eq[jj,:]
                        _pert[ii,jj] = 1j * _w * (_ei @ _gamma @ _ej)

                _evals, _evecs = np.linalg.eigh(_pert)
                self.new_freqs[qq,_manifold] = np.sqrt(_w**2+_evals)

                # self.new_evecs[qq,_manifold,...] = 
        
        ### DEV ###
        fig, ax = plt.subplots(figsize=(4.5,4.5))
        for ii in range(self.num_bands):
            ax.plot(self.qpts_dists,self.new_freqs[:,ii],lw=0,ms=1,marker='o')
        plt.show()
        ### DEV ###

    # ----------------------------------------------------------------------------------------------

    def _fill_gamma_matrix(self,B):

        """
        apply magnetic field as a perturbation and lift the degeneracy of chiral modes
        """

        gamma = np.zeros((self.num_basis,self.num_basis),dtype=float)
        for ii in range(self.num_atoms):
            _q = self.effective_charges[ii]
            _m = self.masses[ii]
            for jj in range(3):
                _gx = -_q / _m * B[0]
                _gy = -_q / _m * B[1]
                _gz = -_q / _m * B[2]
                gamma[3*ii:3*ii+3,3*ii:3*ii+3] = [ [    0, -_gz,  _gy],
                                                   [  _gz,    0, -_gx],
                                                   [ -_gy,  _gx,    0] ]
        return gamma
        
    # ----------------------------------------------------------------------------------------------

if __name__ == '__main__':

    connectivity = c_connectivity()
    connectivity.apply_field_pert(B=[0,0,1000])