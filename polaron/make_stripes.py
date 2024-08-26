
import numpy as np
import sys
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

        # mag and charge densities
        self.mag = np.zeros(self.num_atoms)
        self.den = np.ones(self.num_atoms,dtype=float) * self.num_electrons/self.num_atoms 

        # set the O atom spins to 0
        self.mask = (self.types == 'Cu').astype(float)

    # ----------------------------------------------------------------------------------------------

    def get_afm_order(self,q=[1/2,1/2,0],offset=[0,0,0]):

        """
        AFM order w/ wavevector q. default is the well known (pi,pi,0) order.

        n = up + down
        mag = up-down

        up = (n+mag)/2
        down = (n-mag)/2
        """

        q = self._get_cartesian_primitive_wavevector(q)
        q = self._tile(q)

        _modulation = np.cos(np.sum(self.cart*q,axis=1))

        up = (_modulation+1)*self.mask
        down = (-_modulation+1)*self.mask
        
        up, down = self._normalize_up_and_down(up, down)
        den, mag = self._get_den_and_mag(up,down)

        return up, down, den, mag

    # ----------------------------------------------------------------------------------------------

    def get_fm_order(self):

        """
        paramagnetic order
        """

        up = np.ones(self.num_atoms)*self.mask
        down = np.zeros(self.num_atoms)
        
        up, down = self._normalize_up_and_down(up, down)
        den, mag = self._get_den_and_mag(up,down)
        
        return up, down, den, mag

    # ----------------------------------------------------------------------------------------------

    def get_pm_order(self):
        
        """
        paramagnetic order
        """

        up = np.ones(self.num_atoms)*self.mask
        down = np.ones(self.num_atoms)*self.mask
        
        up, down = self._normalize_up_and_down(up, down)
        den, mag = self._get_den_and_mag(up,down)
        
        return up, down, den, mag

    # ----------------------------------------------------------------------------------------------

    def set_order(self,up,down,left,right):
        
        """
        set the order 
        """
        
        self.up = up
        self.down = down
        self.den = den 
        self.mag = mag
        
    # ----------------------------------------------------------------------------------------------

    def _get_cartesian_primitive_wavevector(self,q):

        """
        self explantory. note, q is in primitive basis
        """

        q = np.array(q,dtype=float)
        return self.prim_recip_vecs@q

    # ----------------------------------------------------------------------------------------------

    def _tile(self,arr):

        """
        tile to the same shape as positions        

        """

        arr = np.tile(arr.reshape(1,3),reps=(self.num_atoms,1))
        return arr

    # ----------------------------------------------------------------------------------------------

    def _get_up_and_down(self,den,mag):
        
        """
        calculate up and down densities
        
        n = up + down
        mag = up-down

        up = (n + mag)/2
        down = (n - mag)/2
        """

        up = (den+mag)/2
        down = (den-mag)/2
       
        return up, down

    # ----------------------------------------------------------------------------------------------
    
    def _get_den_and_mag(self,up,down):
        
        """
        calculate density and magnetization
        
        n = up + down
        mag = up - down

        up = (n + mag)/2
        down = (n - mag)/2
        """

        den = up+down
        mag = up-down

        return den, mag

    # ----------------------------------------------------------------------------------------------
    
    def _normalize_den_and_mag(self,den,mag):
        
        """
        normalize den and mag to the number of electrons
        """

        _norm = self.num_electrons/den.sum()
        den *= _norm
        mag *= _norm
        
        return den, mag

    # ----------------------------------------------------------------------------------------------    
    
    def _normalize_up_and_down(self,up,down):
        
        """
        normalize den and mag to the number of electrons
        """

        _norm = self.num_electrons/(up.sum()+down.sum())
        up *= _norm
        down *= _norm
        
        return up, down

    # ---------------------------------------------------------------------------------------------- 
    
    def sdw_order(self,q=[0,0,0],offset=[0,0,0]):

        """
        modulate the existing mag density by this wave vector
        """

        q = self._get_cartesian_primitive_wavevector(q)
        q = self._tile(q)

        #_modulation = (1+np.cos(np.sum(self.cart*q,axis=1)))*self.mask/2
        _modulation = np.cos(np.sum(self.cart*q,axis=1))*self.mask

        self.mag *= _modulation
        self.up = (self.den+self.mag)/2
        self.down = (self.den-self.mag)/2
        _norm = self.up.sum()+self.down.sum()
        self.up *= self.num_electrons/_norm
        self.down *= self.num_electrons/_norm

        self.den = self.up+self.down
        self.mag = self.up-self.down

        print('\n*** sdw ***')
        self.print()

    # ----------------------------------------------------------------------------------------------

    def cdw_order(self,q=[0,0,0],offset=[0,0,0],amplitude=1.0):
        
        """
        modulate the existing charge density by this wave vector
        """

        q = self._get_cartesian_primitive_wavevector(q)
        q = self._tile(q)

        _modulation = (1+np.cos(np.sum(self.cart*q,axis=1)))*self.mask/2

        self.up *= _modulation
        self.down *= _modulation

        _norm = self.up.sum()+self.down.sum()
        self.up *= self.num_electrons/_norm
        self.down *= self.num_electrons/_norm

        self.den = self.up+self.down
        self.mag = self.up-self.down

        print('\n*** cdw ***')
        self.print()

    # ----------------------------------------------------------------------------------------------

    def get_fim_gaussian(self,center=[0,0,0],width=[0,0,0],amplitude=None):

        """
        localized charge FM density in a PM background
        """

        # convert fwhm to stddev
        width = [fwhm/2.35482 for fwhm in width]

        center = np.array(center,dtype=float)
        center = self._tile(center)
        _r = self.cart-center

        _gauss = np.exp(-0.5*( ((_r[:,0])/(width[0]))**2  + ((_r[:,1])/(width[1]))**2  +
                               ((_r[:,2])/(width[2]))**2 ) )*self.mask*amplitude

        _, _, _, _afm_mag = self.get_afm_order()
        _afm_mag /= _afm_mag.max() # normalize to 1
        _gauss_mag = _afm_mag*_gauss

        _, _, den, mag = self.get_afm_order()

        mag += _gauss_mag
        den += _gauss

        den, mag = self._normalize_den_and_mag(den,mag)
        up, down = self._get_up_and_down(den, mag)

        return up, down, den, mag

    # ----------------------------------------------------------------------------------------------

    def get_afm_gaussian(self,center=[0,0,0],width=[0,0,0],amplitude=None):

        """
        localized charge FM density in a PM background
        """

        # convert fwhm to stddev
        width = [fwhm/2.35482 for fwhm in width]
        
        center = np.array(center,dtype=float)
        center = self._tile(center)
        _r = self.cart-center

        _gauss = np.exp(-0.5*( ((_r[:,0])/(width[0]))**2  + ((_r[:,1])/(width[1]))**2  +
                               ((_r[:,2])/(width[2]))**2 ) )*self.mask*amplitude
        
        _, _, _, _afm_mag = self.get_afm_order()
        _afm_mag /= _afm_mag.max() # normalize to 1
        _gauss_mag = _afm_mag*_gauss
        
        _, _, den, mag = self.get_pm_order()
        
        mag += _gauss_mag
        den += _gauss

        den, mag = self._normalize_den_and_mag(den,mag)
        up, down = self._get_up_and_down(den, mag)

        return up, down, den, mag

    # ----------------------------------------------------------------------------------------------

    def get_fm_gaussian(self,center=[0,0,0],width=[0,0,0],amplitude=None):

        """
        localized charge FM density in a PM background
        """

        # convert fwhm to stddev
        width = [fwhm/2.35482 for fwhm in width]

        center = np.array(center,dtype=float)
        center = self._tile(center)
        _r = self.cart-center

        _gauss = np.exp(-0.5*( ((_r[:,0])/(width[0]))**2  + ((_r[:,1])/(width[1]))**2  +
                               ((_r[:,2])/(width[2]))**2 ) )*self.mask*amplitude

        _, _, _, _fm_mag = self.get_fm_order()
        _fm_mag /= _fm_mag.max() # normalize to 1
        _gauss_mag = _fm_mag*_gauss
        
        _, _, den, mag = self.get_pm_order()
        
        mag += _gauss_mag
        den += _gauss
    
        den, mag = self._normalize_den_and_mag(den,mag)
        up, down = self._get_up_and_down(den, mag)

        return up, down, den, mag
    
    # ----------------------------------------------------------------------------------------------
    
    def get_pm_gaussian(self,center=[0,0,0],width=[0,0,0],amplitude=None):

        """
        localized PM density in a PM background
        """

        # convert fwhm to stddev
        width = [fwhm/2.35482 for fwhm in width]

        center = np.array(center,dtype=float)
        center = self._tile(center)
        _r = self.cart-center

        _gauss = np.exp(-0.5*( ((_r[:,0])/(width[0]))**2  + ((_r[:,1])/(width[1]))**2  +
                               ((_r[:,2])/(width[2]))**2 ) )*amplitude*self.mask

        _, _, den, mag = self.get_pm_order()
        den += _gauss

        den, mag = self._normalize_den_and_mag(den,mag)
        up, down = self._get_up_and_down(den, mag)

        return up, down, den, mag

    # ----------------------------------------------------------------------------------------------

    def print_model(self,title='model'):
        
        """
        print stuff to screen
        """

        _pre = 3
        print(f'\n*** {title} ***')
        print('up:\n',self.up.round(_pre))
        print('down:\n',self.down.round(_pre))
        print('den:\n',self.den.round(_pre))
        print('mag:\n',self.mag.round(_pre))
        print('num_e:\n',self.den.sum().round(_pre)) 
        print('mag:\n',self.mag.sum().round(_pre)) 
        print('')
        
    # ----------------------------------------------------------------------------------------------
    
    def plot_model(self,title='model'):

        """
        plot the model
        """

        fig, ax = plt.subplots(num=1,clear=True,figsize=(6,6))
        
        _cart = self.cart
        _types = self.types

        _Cu_inds = np.flatnonzero(_types == 'Cu')
        _O_inds = np.flatnonzero(_types == 'O')

        _colors = np.zeros((self.num_atoms,3))
        _colors[_Cu_inds,:] = 1.0

        _size = np.copy(self.den)*500/self.den.max() #np.zeros(_types.size)
        _size[np.flatnonzero(_types == 'O')] = 10.0

        ax.scatter(_cart[:,0],_cart[:,1],c=_colors,s=_size,edgecolors='k')

        scale = 2
        ax.quiver(_cart[:,0],_cart[:,1]-self.mag/(2*scale),np.zeros(self.num_atoms),self.mag,
                  angles='xy',scale_units='xy',scale=scale)
        
        ax.set_title(title)

        plt.savefig('model.pdf',dpi=300,bbox_inches='tight')
        #plt.show()

    # ----------------------------------------------------------------------------------------------

    def write_model(self,model_file='model.py'):

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

        with open(model_file,'w') as f:

            msg = 'atom_types = ['
            for ii in range(_num_atoms):
                msg += f'\'{_types[ii]}\','
                if (ii+1) % 20 == 0:
                    msg += '\n\t '
            msg = msg[:-1]+']\n\n'
            f.write(msg)

            msg = 'spin_up_site_density = ['
            for ii in range(_num_atoms):
                msg += f'{_up[ii]: 7.3f},'
                if (ii+1) % 5 == 0:
                    msg += '\n\t\t\t '
            msg = msg[:-1]+']\n\n'
            f.write(msg)
            
            msg = 'spin_down_site_density = ['
            for ii in range(_num_atoms):
                msg += f'{_down[ii]: 7.3f},'
                if (ii+1) % 5 == 0:
                    msg += '\n\t\t\t '
            msg = msg[:-1]+']\n\n'
            f.write(msg)

            msg = 'atom_positions =  ['
            for ii in range(_num_atoms):
                msg += f'[{_pos[ii,0]: 14.10f},{_pos[ii,1]: 14.10f},{_pos[ii,2]: 14.10f}],\n\t\t\t'
            msg = msg[:-5]+']\n\n'
            f.write(msg)

            msg = 'lattice_vectors = ['
            for ii in range(3):
                msg += f'[{_vecs[ii,0]: 14.10f},{_vecs[ii,1]: 14.10f},{_vecs[ii,2]: 14.10f}],\n\t\t   '
            msg = msg[:-7]+']\n\n'
            f.write(msg)

            msg = f'num_electrons = {_num_e: 7.3f}\n\n'
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
    num_holes = 0.1

    # define supercell
    nx = 7; ny = 7
    mult = [nx,ny,1]

    # class for the model
    stripes = c_stripes(pos,vecs,types,num_holes,mult)

    # localized fm gaussian in afm background
    up, down, den, mag = stripes.get_fim_gaussian([3,3,0],[1,1,1],amplitude=-0.7)
    stripes.set_order(up,down,den,mag)
    stripes.print_model('fim_gaussian')
    stripes.plot_model('fim_gaussian')
    
    """
    # paramagnetic order
    up, down, den, mag = stripes.get_pm_order()
    stripes.set_order(up,down,den,mag)
    stripes.print_model('pm')
    stripes.plot_model('pm')
    """
    
    """
    # set underlying AFM order
    up, down, den, mag = stripes.get_afm_order()
    stripes.set_order(up,down,den,mag)
    stripes.print_model('afm')
    stripes.plot_model('afm')
    """

    """
    # ferromagnetic order
    up, down, den, mag = stripes.get_fm_order()
    stripes.set_order(up,down,den,mag)
    stripes.print_model('fm')
    stripes.plot_model('fm')
    """
    
    """
    # localized afm gaussian in pm background
    up, down, den, mag = stripes.get_afm_gaussian([4,4,0],[2,2,1],amplitude=-0.4)
    stripes.set_order(up,down,den,mag)
    stripes.print_model('afm_gaussian')
    stripes.plot_model('afm_gaussian')
    """

    # localized fm gaussian in pm background
    #up, down, den, mag = stripes.get_fm_gaussian([3,3,0],[1,1,1],amplitude=-0.2)
    #stripes.set_order(up,down,den,mag)
    #stripes.print_model('fm_gaussian')
    #stripes.plot_model('fm_gaussian')

    # localized pm gaussian in pm background - converges to pure pm w/o elph
    #up, down, den, mag = stripes.get_pm_gaussian([3,3,0],[3,3,3],amplitude=-0.9)
    #stripes.set_order(up,down,den,mag)
    #stripes.print_model('pm_gaussian')
    #stripes.plot_model('pm_gaussian')

    """
    # localized pm gaussian in afm background
    #up, down, den, mag = stripes.get_pm_gaussian_in_afm([3,3,0],[3,3,3],amplitude=-0.75)
    stripes.set_order(up,down,den,mag)
    stripes.print_model('pm_gaussian_afm')
    stripes.plot_model('pm_gaussian_afm')  
    """

    """
    # set spin-density wave order
    q = [1/nx,1/nx,0]
    stripes.sdw_order(q)

    # set charde-density wave order
    q = [2/nx,2/nx,0]
    stripes.cdw_order(q)
    """

    # write the model
    stripes.write_model()
    

