
import numpy as np
import h5py


precision = 9

# --------------------------------------------------------------------------------------------------

class c_unfold_phonons:

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
            self.prim_coords_red = db['atom_positions_reduced'][...]
            self.prim_coords_cart = db['atom_positions_cartesian'][...]
            self.prim_freqs = db['frequencies'][...] # [ qpts, bands ]
            self.prim_eigvecs = db['eigenvectors'][...] # [ qpts, band, basis ]
            self.prim_atoms_nums = db['atom_type_nums'][...]

        self.prim_num_atoms = self.prim_atoms_nums.size
        self.prim_num_qpts = self.prim_freqs.shape[0]
        self.prim_num_bands = self.prim_freqs.shape[1]

    # ----------------------------------------------------------------------------------------------

    def set_super_cell_file(self,sc_file):

        """
        ...
        """

        self.sc_file = sc_file

        with h5py.File(sc_file,'r') as db:

            self.sc_lat_vecs = db['lattice_vectors'][...]
            self.sc_coords_red = db['atom_positions_reduced'][...]
            self.sc_coords_cart = db['atom_positions_cartesian'][...]
            self.sc_freqs = db['frequencies'][...] # [ qpts, bands ]
            self.sc_eigvecs = db['eigenvectors'][...] # [ qpts, band, basis ]
            self.sc_atoms_nums = db['atom_type_nums'][...]

        self.sc_num_atoms = self.sc_atoms_nums.size
        self.sc_num_qpts = self.sc_freqs.shape[0]
        self.sc_num_bands = self.sc_freqs.shape[1]

    # ----------------------------------------------------------------------------------------------

    def check_files(self):

        """
        ...
        """

        if self.sc_num_qpts != self.prim_num_qpts:
            msg = 'number of qpts in supercell calc. must be same as in primitive cell calc.'
            print(msg)
            exit()
        self.num_qpts = self.sc_num_qpts

    # ----------------------------------------------------------------------------------------------

    def transform_prim_calc(self):

        """
        ...
        """

        _trans = np.linalg.inv( self.prim_lat_vecs.T )
        self.sc_to_prim_map = np.zeros(self.sc_num_atoms,dtype=int)

        for ii in range(self.sc_num_atoms):
            _vec = _trans @ self.sc_coords_cart[ii,:] 
            self.sc_to_prim_map[ii] = self._get_ind_in_supercell(_vec)

        _prim_eigvecs = self.prim_eigvecs
        self.transformed_eigvecs = np.zeros((self.num_qpts,self.prim_num_bands,self.sc_num_bands),
                                            dtype=complex)
        
        _new_eigvec = np.zeros((self.sc_num_atoms,3),dtype=complex)

        for qq in range(self.num_qpts):
            for nn in range(self.prim_num_bands):

                _eigvec = _prim_eigvecs[qq,nn,:].reshape(self.prim_num_atoms,3)

                for ii, ind in enumerate(self.sc_to_prim_map):
                    _new_eigvec[ii,:] = _eigvec[ind,:]

                self.transformed_eigvecs[qq,nn,:] = _new_eigvec.flatten()

    # ----------------------------------------------------------------------------------------------

    def _get_ind_in_supercell(self,vec):

        """
        ...
        """

        _mod, _int = np.modf(np.abs(vec).round(precision))
        
        _prim_vecs = self.prim_coords_red
        
        ind = np.flatnonzero( np.logical_and(np.logical_and(_prim_vecs[:,0] == _mod[0],  
                                                            _prim_vecs[:,1] == _mod[1]),
                                            _prim_vecs[:,2] == _mod[2] ))[0]
        
        return ind
    
    # ----------------------------------------------------------------------------------------------

    def _transform_prim_eigvec(self,eigvec):

        """
        ...
        """

        new_eigvec = np.zeros(self.sc_num_bands,dtype=complex)

    # ----------------------------------------------------------------------------------------------

    def get_projection_weights(self):

        """
        ...
        """

        self.weights = np.zeros((self.num_qpts,self.sc_num_bands))

        for qq in range(self.num_qpts):

                for mm in range(self.sc_num_bands):

                    _weight = 0.0
                    _sc_evec = self.sc_eigvecs[qq,mm,:]

                    for nn in range(self.prim_num_bands):
                        _weight += np.abs(_sc_evec.conj() @ self.transformed_eigvecs[qq,nn,:])**2

                    self.weights[qq,mm] = _weight

                self.weights[qq,:] *= self.prim_num_bands / self.weights[qq,:].sum() 

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

    def unfold(self,prim_file,sc_file):

        """
        ...
        """

        self.set_primitive_cell_file(prim_file)
        self.set_super_cell_file(sc_file)
        self.check_files()

        self.transform_prim_calc()
        self.get_projection_weights()

        self.write_projection_weights()

    # ----------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    from calcs import calcs
    num_calcs = len(calcs)

    for ii in range(num_calcs):
        
        n, U, order = calcs[ii]
        n *= 4.0
        
        unfold = c_unfold_phonons()
        unfold.unfold('prim_phonons/phonons.hdf5',f'specfun/{order}_U_{U:3.2f}_N_{n:3.2f}.hdf5')
    
    
