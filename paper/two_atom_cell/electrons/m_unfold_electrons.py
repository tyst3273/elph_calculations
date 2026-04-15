
import numpy as np
import h5py


precision = 9
epsilon = 1e-9

# --------------------------------------------------------------------------------------------------

class c_unfold_electrons:

    # ----------------------------------------------------------------------------------------------

    def __init__(self):

        """
        ...
        """

        pass

    # ----------------------------------------------------------------------------------------------

    def set_primitive_cell_file(self,prim_file):

        """
        ...
        """

        self.prim_file = prim_file

        with h5py.File(prim_file,'r') as db:

            self.prim_lat_vecs = db['lattice_vectors'][...]
            self.prim_recip_lat_vecs = db['reciprocal_lattice_vectors'][...]

            self.prim_eigs = db['eigenvalues'][...] # [ kpts, bands ]
            self.prim_eigvecs = db['eigenvectors'][...] # [ kpts, band, basis ]
            self.prim_ef = db['fermi_energy'][...] 

            self.prim_kpts_cart = db['kpts_cartesian'][...]
            self.prim_kpts_red = db['kpts_rlu'][...]

            self.prim_orb_coords_red = db['orbital_positions_reduced'][...]
            self.prim_orb_coords_cart = db['orbital_positions_cartesian'][...]
            
            self.prim_orb_nums = db['orbital_atom_type_nums'][...]

        self.prim_num_kpts = self.prim_eigs.shape[0]
        self.prim_num_bands = self.prim_eigs.shape[1]
        self.prim_num_spin = self.prim_eigs.shape[2]
        self.prim_num_orbs = self.prim_orb_nums.size

    # ----------------------------------------------------------------------------------------------

    def set_super_cell_file(self,sc_file):

        """
        ...
        """

        self.sc_file = sc_file

        with h5py.File(sc_file,'r') as db:

            self.sc_lat_vecs = db['lattice_vectors'][...]
            self.sc_recip_lat_vecs = db['reciprocal_lattice_vectors'][...]

            self.sc_eigs = db['eigenvalues'][...] # [ kpts, bands ]
            self.sc_eigvecs = db['eigenvectors'][...] # [ kpts, band, basis ]
            self.sc_ef = db['fermi_energy'][...] 

            self.sc_kpts_cart = db['kpts_cartesian'][...]
            self.sc_kpts_red = db['kpts_rlu'][...]

            self.sc_orb_coords_red = db['orbital_positions_reduced'][...]
            self.sc_orb_coords_cart = db['orbital_positions_cartesian'][...]

            self.sc_orb_nums = db['orbital_atom_type_nums'][...]

        self.sc_num_kpts = self.sc_eigs.shape[0]
        self.sc_num_bands = self.sc_eigs.shape[1]
        self.sc_num_spin = self.sc_eigs.shape[2]
        self.sc_num_orbs = self.sc_orb_nums.size

    # ----------------------------------------------------------------------------------------------

    def check_files(self):

        """
        ...
        """

        if self.sc_num_kpts != self.prim_num_kpts:
            msg = 'number of kpts in supercell calc. must be same as in primitive cell calc.'
            print(msg)
            exit()
        self.num_kpts = self.sc_num_kpts

        if self.sc_num_spin != self.prim_num_spin:
            msg = 'spin in supercell calc. must be same as in primitive cell calc.'
            print(msg)
            exit()
        self.num_spin = self.sc_num_spin
        
    # ----------------------------------------------------------------------------------------------

    def transform_prim_fs(self):

        """
        ...
        """

        _eigs = self.sc_eigs
        _ef = self.sc_ef
        fwhm = 0.005
        sigma = fwhm / 2.35482 
        fs_weights = np.exp(-0.5 * (_eigs-_ef)**2/sigma**2 ) 

        self.kpt_inds_to_keep = np.flatnonzero( 
            np.greater(fs_weights.sum(axis=(1,2))/_eigs.shape[1] * 2,
                       0.000001) )
        self.num_kpts_keep = self.kpt_inds_to_keep.size
        self.fs_weights = fs_weights[self.kpt_inds_to_keep,...]

        # -------------------------------
        # map prim kpts to supercell kpts

        _trans = np.linalg.inv( self.prim_recip_lat_vecs.T )
        self.sc_to_prim_kpt_map = np.zeros(self.num_kpts_keep,dtype=int)
        self.mapped_kpts = np.zeros((self.num_kpts_keep,3),dtype=float)

        for ii, kk in enumerate(self.kpt_inds_to_keep):  

            if ii % 1000 == 0:
                print(ii,'/',self.num_kpts_keep)

            _vec = _trans @ self.sc_kpts_cart[kk,:] 
            self.sc_to_prim_kpt_map[ii] = self._get_kpt_ind_in_supercell(_vec)
            self.mapped_kpts[ii,:] = _vec

        # -------------------------------
        # map prim evecs to supercell evecs

        _trans = np.linalg.inv( self.prim_lat_vecs.T )
        self.sc_to_prim_map = np.zeros(self.sc_num_orbs,dtype=int)

        for ii in range(self.sc_num_orbs):
            _vec = _trans @ self.sc_orb_coords_cart[ii,:] 
            self.sc_to_prim_map[ii] = self._get_ind_in_supercell(_vec)

        _prim_eigvecs = self.prim_eigvecs
        self.transformed_eigvecs = np.zeros((self.num_kpts_keep,
                                             self.prim_num_bands,self.sc_num_bands,
                                             self.num_spin),dtype=complex)
        
        for qq in range(self.num_kpts_keep):

            prim_ind = self.sc_to_prim_kpt_map[qq]

            for nn in range(self.prim_num_bands):
                for ss in range(self.num_spin):

                    _eigvec = _prim_eigvecs[prim_ind,nn,:,ss]

                    for ii, ind in enumerate(self.sc_to_prim_map):
                        self.transformed_eigvecs[qq,nn,ii,ss] = _eigvec[ind]
    
    # ----------------------------------------------------------------------------------------------

    def _get_kpt_ind_in_supercell(self,kpt):

        """
        ...
        """

        # _mod, _int = np.modf(kpt.round(precision))
        # _mod, _ = self._fold_to_first_bz(_mod)

        # _prim_kpts = self.prim_kpts_red
        
        # ind = np.flatnonzero( np.logical_and(np.logical_and(_prim_kpts[:,0] == _mod[0],  
        #                                                     _prim_kpts[:,1] == _mod[1]),
        #                                     _prim_kpts[:,2] == _mod[2] ))[0]

        _kpt = np.tile(kpt.reshape(1,3),reps=(self.num_kpts,1))
        ind = np.argmin( np.sqrt( np.sum( (self.prim_kpts_red-_kpt)**2, axis=1 )) ) 
    
        return ind
    
    # ----------------------------------------------------------------------------------------------

    def _fold_to_first_bz(self,kpt):

        """
        ...
        """

        # kpt = np.copy(np.atleast_2d(kpt))

        red, _ = np.modf(kpt)
        mill = np.round( kpt - (red.round(precision) == 0.5)*epsilon + 
                        (red.round(precision) == -0.5)*epsilon )
        
        red[red > 0.5] += -1
        red[red <= -0.5] += 1

        return red, mill 
        
    # ----------------------------------------------------------------------------------------------

    def transform_prim_bands(self):

        """
        ...
        """

        _trans = np.linalg.inv( self.prim_lat_vecs.T )
        self.sc_to_prim_map = np.zeros(self.sc_num_orbs,dtype=int)

        for ii in range(self.sc_num_orbs):
            _vec = _trans @ self.sc_orb_coords_cart[ii,:] 
            self.sc_to_prim_map[ii] = self._get_ind_in_supercell(_vec)

        _prim_eigvecs = self.prim_eigvecs
        self.transformed_eigvecs = np.zeros((self.num_kpts,self.prim_num_bands,self.sc_num_bands,
                                            self.num_spin),dtype=complex)
        
        for qq in range(self.num_kpts):
            for nn in range(self.prim_num_bands):
                for ss in range(self.num_spin):

                    _eigvec = _prim_eigvecs[qq,nn,:,ss]

                    for ii, ind in enumerate(self.sc_to_prim_map):
                        self.transformed_eigvecs[qq,nn,ii,ss] = _eigvec[ind]

    # ----------------------------------------------------------------------------------------------

    def _get_ind_in_supercell(self,vec):

        """
        ...
        """

        _mod, _int = np.modf(np.abs(vec).round(precision))
        
        _prim_vecs = self.prim_orb_coords_red
        
        ind = np.flatnonzero( np.logical_and(np.logical_and(_prim_vecs[:,0] == _mod[0],  
                                                            _prim_vecs[:,1] == _mod[1]),
                                            _prim_vecs[:,2] == _mod[2] ))[0]
        
        return ind
    
    # ----------------------------------------------------------------------------------------------

    def get_projection_weights(self):

        """
        ...
        """

        self.weights = np.zeros((self.num_kpts,self.sc_num_bands,self.num_spin))

        for qq in range(self.num_kpts):

                for ss in range(self.num_spin):
                         
                    for mm in range(self.sc_num_bands):
                            
                        _weight = 0.0
                        _sc_evec = self.sc_eigvecs[qq,mm,:,ss]

                        for nn in range(self.prim_num_bands):
                            _weight += np.abs(
                                _sc_evec.conj() @ self.transformed_eigvecs[qq,nn,:,ss])**2

                        self.weights[qq,mm,ss] = _weight

                    self.weights[qq,:,ss] *= \
                        self.prim_num_bands / self.weights[qq,:,ss].sum() 
                    
    # ----------------------------------------------------------------------------------------------

    def get_projection_weights_keep(self):

        """
        ...
        """

        self.weights = np.zeros((self.num_kpts_keep,self.sc_num_bands,self.num_spin))

        for qq in range(self.num_kpts_keep):
                
                ind = self.kpt_inds_to_keep[qq]

                for ss in range(self.num_spin):
                         
                    for mm in range(self.sc_num_bands):
                            
                        _weight = 0.0
                        _sc_evec = self.sc_eigvecs[ind,mm,:,ss]

                        for nn in range(self.prim_num_bands):
                            _weight += np.abs(
                                _sc_evec.conj() @ self.transformed_eigvecs[qq,nn,:,ss])**2

                        self.weights[qq,mm,ss] = _weight

                    self.weights[qq,:,ss] *= \
                        self.prim_num_bands / self.weights[qq,:,ss].sum() 

    # ----------------------------------------------------------------------------------------------

    def get_projection_weights(self):

        """
        ...
        """

        self.weights = np.zeros((self.num_kpts,self.sc_num_bands,self.num_spin))

        for qq in range(self.num_kpts):

                for ss in range(self.num_spin):
                         
                    for mm in range(self.sc_num_bands):
                            
                        _weight = 0.0
                        _sc_evec = self.sc_eigvecs[qq,mm,:,ss]

                        for nn in range(self.prim_num_bands):
                            _weight += np.abs(
                                _sc_evec.conj() @ self.transformed_eigvecs[qq,nn,:,ss])**2

                        self.weights[qq,mm,ss] = _weight

                    self.weights[qq,:,ss] *= \
                        self.prim_num_bands / self.weights[qq,:,ss].sum() 

    # ----------------------------------------------------------------------------------------------

    def write_projection_weights(self):

        """
        ...
        """

        with h5py.File(self.sc_file,'a') as db:

            if '_unfolding_weights' in db.keys():
                del db['_unfolding_weights']
            db.create_dataset('_unfolding_weights',data=self.weights)

    # ----------------------------------------------------------------------------------------------

    def write_fs_weights(self):

        """
        ...
        """

        with h5py.File(self.sc_file,'a') as db:

            if '_fs_weights' in db.keys():
                del db['_fs_weights']
            db.create_dataset('_fs_weights',data=self.fs_weights)
        
    # ----------------------------------------------------------------------------------------------

    def write_mapped_kpts(self):

        """
        ...
        """

        with h5py.File(self.sc_file,'a') as db:

            if '_mapped_kpts' in db.keys():
                del db['_mapped_kpts']
            db.create_dataset('_mapped_kpts',data=self.mapped_kpts)

# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

def unfold_bands(bands,nscf,prim_bands,prim_nscf):

    """
    ...
    """

    unfold = c_unfold_electrons()
    unfold.set_primitive_cell_file(prim_bands)
    unfold.set_super_cell_file(bands)
    unfold.check_files()

    unfold.transform_prim_bands()
    unfold.get_projection_weights()

    unfold.write_projection_weights()


    unfold = c_unfold_electrons()
    unfold.set_primitive_cell_file(prim_nscf)
    unfold.set_super_cell_file(nscf)
    unfold.check_files()

    unfold.transform_prim_fs()
    unfold.get_projection_weights_keep()

    unfold.write_projection_weights()
    unfold.write_fs_weights()
    unfold.write_mapped_kpts()

# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    unfold_bands('bands.hdf5','nscf.hdf5','prim/bands.hdf5','prim/nscf.hdf5')

    
    
