
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------------------------------

class c_stripes:

    # ----------------------------------------------------------------------------------------------

    def __init__(self,pos,vecs,types,num_holes,mult=[1,1,1]):

        """
        take primitive vectors and positions and make a supercell to embed stripe order in
        """

        self.pos = np.array(pos,dtype=float)
        self.vecs = np.array(vecs,dtype=float)
        self.types = np.array(types,dtype=object)

        self.prim_num_electrons = 1-num_holes
        self.num_holes = num_holes

        self.num_atoms = self.pos.shape[0]

        self.cart = np.zeros(self.pos.shape,dtype=float)
        for ii in range(self.pos.shape[0]):
            self.cart[ii,:] = self.pos[ii,0]*self.vecs[0,:]+self.pos[ii,1]*self.vecs[1,:]+ \
                        self.pos[ii,2]*self.vecs[2,:]

        self.prim_vecs = np.copy(self.vecs)
        self.prim_recip_vecs = np.linalg.solve(self.vecs,2*np.pi*np.eye(3)).T

        self.make_supercell(mult)
    
    # ----------------------------------------------------------------------------------------------

    def make_supercell(self,mult=[1,1,1]):
        
        """
        make the supercell
        """

        # supercell multiplicity
        mult = np.array(mult,dtype=int)

        # number of electrons in supercell
        self.num_reps = np.prod(mult)
        self.num_electrons = self.prim_num_electrons*self.num_reps

        _num_basis = self.pos.shape[0]

        _vecs = np.copy(self.vecs)
        _pos = np.copy(self.pos)
        _types = np.copy(self.types)

        _vecs[0] *= mult[0]
        _vecs[1] *= mult[1]
        _vecs[2] *= mult[2]
        self.vecs = _vecs
        
        self.recip_vecs = (np.linalg.inv(self.vecs)@np.eye(3)*2*np.pi).T

        _x = np.arange(mult[0])
        _y = np.arange(mult[1])
        _z = np.arange(mult[2])

        _x, _y, _z = np.meshgrid(_x,_y,_z,indexing='xy')
        _x = _x.flatten(); _y = _y.flatten(); _z = _z.flatten()

        _num_reps = _x.size
        _shifts = np.zeros((_num_reps,3),dtype=int)
        _shifts[:,0] = _x
        _shifts[:,1] = _y
        _shifts[:,2] = _z

        # number of atoms in the supercell
        self.num_atoms = _num_basis*_num_reps
        _shifts = np.tile(_shifts.reshape(_num_reps,1,3),
                reps=(1,_num_basis,1)).reshape(self.num_atoms,3)
        _pos = np.tile(_pos.reshape(1,_num_basis,3),
                reps=(_num_reps,1,1)).reshape(self.num_atoms,3)

        # reduced position of the atoms in the unitcell
        _pos += _shifts
        _pos[:,0] /= mult[0]
        _pos[:,1] /= mult[1]
        _pos[:,2] /= mult[2]
        self.pos = _pos

        # cartesian position of the atoms
        self.cart = np.zeros(_pos.shape,dtype=float)
        for ii in range(self.num_atoms):
            self.cart[ii,:] = self.pos[ii,0]*self.vecs[0,:]+self.pos[ii,1]*self.vecs[1,:]+ \
                        self.pos[ii,2]*self.vecs[2,:]

        # atom types
        self.types = np.tile(self.types.reshape(1,_num_basis),
                reps=(_num_reps,1)).reshape(self.num_atoms)

        # spin and charge densities
        self.spin = np.zeros(self.num_atoms)
        self.den = np.ones(self.num_atoms,dtype=float) * self.num_electrons/self.num_atoms 

        # set the O atom spins to 0
        self.mask = (self.types == 'Cu').astype(float)

    # ----------------------------------------------------------------------------------------------

    def fm_order(self):

        """
        paramagnetic order
        """

        self.up = np.ones(self.num_atoms)*self.mask
        self.down = np.zeros(self.num_atoms)
        _norm = self.up.sum()+self.down.sum()
        self.up *= self.num_electrons/_norm
        self.down *= self.num_electrons/_norm
        self.den = self.up+self.down
        self.spin = self.up-self.down

        print('\n*** fm ***')
        self.print()

    # ----------------------------------------------------------------------------------------------

    def pm_order(self):
        
        """
        paramagnetic order
        """

        self.up = np.ones(self.num_atoms)*self.mask
        self.down = np.ones(self.num_atoms)*self.mask
        _norm = self.up.sum()+self.down.sum()
        self.up *= self.num_electrons/_norm
        self.down *= self.num_electrons/_norm
        self.den = self.up+self.down
        self.spin = self.up-self.down

        print('\n*** pm ***')
        self.print()

    # ----------------------------------------------------------------------------------------------

    def print(self):
        
        """
        print stuff to screen
        """

        _pre = 3
        print('up:\n',self.up.round(_pre))
        print('down:\n',self.down.round(_pre))
        print('den:\n',self.den.round(_pre))
        print('spin:\n',self.spin.round(_pre))
        print('num_e:\n',self.den.sum()) 
        print('mag:\n',self.spin.sum()) 
        print('')
        
    # ----------------------------------------------------------------------------------------------

    def _get_cartesian_wavevector(self,q):

        """
        self explantory. note, q is in primitive basis
        """

        q = np.array(q,dtype=float)
        return self.prim_recip_vecs@q

    # ----------------------------------------------------------------------------------------------

    def _tile_q(self,q):

        """
        tile q to the same shape as positions
        """

        q = np.tile(q.reshape(1,3),reps=(self.num_atoms,1))
        return q

    # ----------------------------------------------------------------------------------------------

    def neel_order(self,q=[1/2,1/2,0],offset=[0,0,0]):
        
        """
        AFM order w/ wavevector q. default is the well known (pi,pi,0) order.

        n = up + down
        spin = up-down

        up = (n+spin)/2
        down = (n-spin)/2
        """

        q = self._get_cartesian_wavevector(q)
        q = self._tile_q(q)

        _modulation = np.cos(np.sum(self.cart*q,axis=1))

        self.up = (_modulation+1)*self.mask
        self.down = (-_modulation+1)*self.mask
        _norm = self.up.sum()+self.down.sum()
        self.up *= self.num_electrons/_norm
        self.down *= self.num_electrons/_norm
        self.den = self.up+self.down
        self.spin = self.up-self.down

        print('\n*** neel ***')
        self.print()

    # ----------------------------------------------------------------------------------------------

    def sdw_order(self,q=[0,0,0],offset=[0,0,0]):

        """
        modulate the existing spin density by this wave vector

        n = up + down
        spin = up-down

        up = (n+spin)/2
        down = (n-spin)/2
        """

        q = self._get_cartesian_wavevector(q)
        q = self._tile_q(q)

        #_modulation = (1+np.cos(np.sum(self.cart*q,axis=1)))*self.mask/2
        _modulation = np.cos(np.sum(self.cart*q,axis=1))*self.mask

        self.spin *= _modulation
        self.up = (self.den+self.spin)/2
        self.down = (self.den-self.spin)/2
        _norm = self.up.sum()+self.down.sum()
        self.up *= self.num_electrons/_norm
        self.down *= self.num_electrons/_norm


        self.den = self.up+self.down
        self.spin = self.up-self.down

        print('\n*** sdw ***')
        self.print()

    # ----------------------------------------------------------------------------------------------

    def cdw_order(self,q=[0,0,0],offset=[0,0,0],amplitude=1.0):
        
        """
        modulate the existing charge density by this wave vector

        n = up + down
        spin = up-down

        up = (n+spin)/2
        down = (n-spin)/2
        """

        q = self._get_cartesian_wavevector(q)
        q = self._tile_q(q)

        _modulation = (1+np.cos(np.sum(self.cart*q,axis=1)))*self.mask/2

        self.up *= _modulation
        self.down *= _modulation

        _norm = self.up.sum()+self.down.sum()
        self.up *= self.num_electrons/_norm
        self.down *= self.num_electrons/_norm

        self.den = self.up+self.down
        self.spin = self.up-self.down

        print('\n*** cdw ***')
        self.print()

    # ----------------------------------------------------------------------------------------------

    def gaussian(self,center=[0,0,0],width=[0,0,0],amplitude=0.1):

        """
        localized charge density 
        """

        q = self._get_cartesian_wavevector(q)
        pass
    
    # ----------------------------------------------------------------------------------------------

    def plot_model(self):

        """
        plot it
        """

        fig, ax = plt.subplots(num=1,clear=True,figsize=(6,6))
        
        _cart = self.cart
        _types = self.types

        _Cu_inds = np.flatnonzero(_types == 'Cu')
        _O_inds = np.flatnonzero(_types == 'O')

        _colors = np.zeros((self.num_atoms,3))
        _colors[_Cu_inds,:] = 1.0

        _size = np.copy(self.den)*100/self.den.max() #np.zeros(_types.size)
        _size[np.flatnonzero(_types == 'O')] = 10.0

        ax.scatter(_cart[:,0],_cart[:,1],c=_colors,s=_size,edgecolors='k')

        scale = 5
        ax.quiver(_cart[:,0],_cart[:,1]-self.spin/(2*scale),np.zeros(self.num_atoms),self.spin,
                  angles='xy',scale_units='xy',scale=scale)

        plt.savefig('model.pdf',dpi=300,bbox_inches='tight')
        #plt.show()

    # ----------------------------------------------------------------------------------------------

    def write(self,output_file):

        """
        write the model to a file
        """

        _num_atoms = self.num_atoms
        _up = self.up
        _down = self.down
        _pos = self.pos
        _types = self.types
        _vecs = self.vecs
        _num_e = self.num_electrons

        with open(output_file,'w') as f:

            msg = 'types = ['
            for ii in range(_num_atoms):
                msg += f'\'{_types[ii]}\','
                if (ii+1) % 20 == 0:
                    msg += '\n\t '
            msg = msg[:-1]+']\n'
            f.write(msg)

            msg = 'spin_up_site_density = ['
            for ii in range(_num_atoms):
                msg += f'{_up[ii]: 7.3f},'
                if (ii+1) % 5 == 0:
                    msg += '\n\t\t\t '
            msg = msg[:-1]+']\n'
            f.write(msg)
            
            msg = 'spin_down_site_density = ['
            for ii in range(_num_atoms):
                msg += f'{_down[ii]: 7.3f},'
                if (ii+1) % 5 == 0:
                    msg += '\n\t\t\t '
            msg = msg[:-1]+']\n'
            f.write(msg)

            msg = 'pos =  ['
            for ii in range(_num_atoms):
                msg += f'[{_pos[ii,0]: 10.6f},{_pos[ii,1]: 10.6f},{_pos[ii,2]: 10.6f}],\n\t'
            msg = msg[:-3]+']\n'
            f.write(msg)

            msg = 'lattice_vectors = ['
            for ii in range(3):
                msg += f'[{_vecs[ii,0]: 10.6f},{_vecs[ii,1]: 10.6f},{_vecs[ii,2]: 10.6f}],\n\t\t   '
            msg = msg[:-7]+']\n'
            f.write(msg)

            msg = f'num_electrons = {_num_e: 7.3f}\n'
            f.write(msg)
            
    # ----------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # define primitive unitcell
    pos = [[ 0.0, 0.0, 0.0],
           [ 0.5, 0.0, 0.0],
           [ 0.0, 0.5, 0.0]]
    vecs = [[ 1.0, 0.0, 0.0],
            [ 0.0, 1.0, 0.0],
            [ 0.0, 0.0,10.0]]
    types = ['Cu','O','O']
    num_holes = 0.0

    # define supercell
    nx = 8; ny = 8
    mult = [nx,ny,1]

    # class for the model
    stripes = c_stripes(pos,vecs,types,num_holes,mult)

    # paramagnetic order
    #stripes.pm_order()

    # set underlying AFM order
    stripes.neel_order()

    # ferromagnetic order
    #stripes.fm_order()

    # set spin-density wave order
    n = 8
    q = [1/nx,1/nx,0]
    stripes.sdw_order(q)

    # set charde-density wave order
    q = [2/nx,2/nx,0]
    stripes.cdw_order(q)

    # show the model
    stripes.plot_model()

    # write the model
    stripes.write('model.txt')
    


