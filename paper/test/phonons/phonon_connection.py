
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

            # [qpts, bands, basis] : note that bands/basis order is backwards from 
            # common definition
            self.evecs = db['eigenvectors'][...] 

            # [qpts, bands] 
            self.freqs = db['frequencies'][...]

            self.qpts = db['qpts_rlu'][...]
            self.qpts_dists = db['qpts_distances'][...]
            self.qpts_verts = db['qpts_vert_distances'][...]

        self.num_qpts, self.num_bands, self.num_basis = self.evecs.shape

        # sort modes are neighboring qpts according to size of projection
        self._connect_bands()

        for ii in range(self.num_bands):
            plt.plot(self.qpts_dists,self.freqs[:,ii])
        plt.show()
        exit()

        # find all the degeneracies
        self._find_all_degeneracies()

    # ----------------------------------------------------------------------------------------------

    def _connect_bands(self):

        """
        sort modes are neighboring qpts according to size of projection 
            P_nm = | < q, n| q + dq, m >|**2

        NOTE: below, k = q+dq
        """

        self.band_order = np.zeros(self.freqs.shape,dtype=int)
        self.band_order[0,:] = np.arange(self.num_bands)

        for ii in range(1,self.num_qpts):

            _eq = self.evecs[ii-1,...]
            _ek = self.evecs[ii,...]

            _Pqk = np.abs( _eq.conj() @ _ek.T )**2

            _order = []
            for nn in range(self.num_bands):

                _sorted = np.flip(np.argsort(_Pqk[nn,:]))
                for mm in _sorted:
                    if mm not in _order:
                        _order.append(int(mm))
                        break

            self.freqs[ii,:] = self.freqs[ii,_order]
            self.evecs[ii,...] = self.evecs[ii,_order,:]
            self.band_order[ii,:] = _order

    # ----------------------------------------------------------------------------------------------

    def _find_all_degeneracies(self):

        """
        loop over all q-points and find any degeneracies
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


    # ----------------------------------------------------------------------------------------------

    def connect_bands(self):

        pass
        
    # ----------------------------------------------------------------------------------------------

if __name__ == '__main__':

    connectivity = c_connectivity()