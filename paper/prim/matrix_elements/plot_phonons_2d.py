
import numpy as np
import matplotlib.pyplot as plt
import h5py 


# --------------------------------------------------------------------------------------------------

class plot_phonons:

    # ----------------------------------------------------------------------------------------------

    def __init__(self,phonon_file='phonon_out.hdf5'):

        with h5py.File(phonon_file,'r') as db:

            self.nums = db['atom_type_nums'][...]
            self.masses = db['atom_masses'][...]
            self.eigvecs = db['eigenvectors'][...]
            
            self.num_qpts = self.eigvecs.shape[0]
            self.num_atoms = self.nums.size
            self.num_modes = self.num_atoms*3
            
            self.freqs = db['frequencies'][...]
            self.qpts_rlu = db['qpts_rlu'][:,:2].round(3)
            self.qpts_cart = db['qpts_cartesian'][:,:2]
            if 'qpts_distances' in db.keys():
                self.qpts_dist = db['qpts_distances'][...]
            else:
                self.qpts_dist = np.arange(self.num_qpts)

            self.pos_r = db['atom_positions_reduced'][:,:2]
            self.latvecs = db['lattice_vectors'][:2,:2]

    # ----------------------------------------------------------------------------------------------

    def plot_qpts(self):
        
        msg = '\nprinting metadata in the file'
        msg += f'\nnumber of modes: {self.num_modes}'
        msg += f'\nnumber of qpts: {self.num_qpts}'
        msg += '\nqpoints in this file [in rlu]'
        for ii in range(self.num_qpts):
            _ = f'qpt[{ii}]:'
            msg += f'\n {_:>8} ({self.qpts_rlu[ii,0]: 5.3f}, {self.qpts_rlu[ii,1]: 5.3f})'
        print(msg)

    # ----------------------------------------------------------------------------------------------

    def get_qpt_ind(self,qpt=[0,0]):

        self.qpt = np.array(qpt,dtype=float).round(3)
        qpt_ind = np.flatnonzero(self.qpts_rlu[:,0] == self.qpt[0])
        qpt_ind = np.intersect1d(np.flatnonzero(self.qpts_rlu[:,1] == self.qpt[1]),qpt_ind)[0]

        return qpt_ind

    # ----------------------------------------------------------------------------------------------

    def _make_supercell(self,sc,eigs):
        
        self.mult = sc**2
        x = np.arange(sc)
        x, y = np.meshgrid(x,x,indexing='ij')
        x = x.flatten(); y = y.flatten()
        s = np.c_[x,y]
        s = np.tile(s.reshape(self.mult,1,2),
                reps=(1,self.num_atoms,1)).reshape(self.mult*self.num_atoms,2)
        pos_r = np.tile(self.pos_r,reps=(self.mult,1))
        pos_r += s
        pos_r /= sc

        latvecs = np.copy(self.latvecs)*sc

        pos = np.zeros(pos_r.shape)
        for ii in range(pos_r.shape[0]):
            pos[ii,:] = latvecs[0,:]*pos_r[ii,0]+latvecs[1,:]*pos_r[ii,1]

        eigs = np.tile(eigs,reps=(self.mult,1))
        nums = np.tile(self.nums,reps=(self.mult,1))

        return eigs, pos, nums
    
    # ----------------------------------------------------------------------------------------------

    def plot_displacements(self,qpt=[0,0],mode=0,sc=1,a=0.5):
        
        qpt = np.array(qpt,dtype=float)
        qpt_ind = self.get_qpt_ind(qpt)

        eigs = self.eigvecs[qpt_ind,mode,...]
        eigs = eigs.reshape(self.num_atoms,3)[:,:2]
        
        masses = np.tile(self.masses.reshape(self.num_atoms,1),reps=(1,2))
        eigs = eigs/np.sqrt(masses)

        eigs, pos, nums = self._make_supercell(sc,eigs)

        qc = self.qpts_cart[qpt_ind,:]
        qc = np.tile(qc.reshape(1,2),reps=(self.num_atoms*self.mult,1))
        exp_iqr = np.exp(1j*np.sum(qc*pos,axis=1))
        exp_iqr = np.tile(exp_iqr.reshape(self.num_atoms*self.mult,1),reps=(1,2))
        eigs = exp_iqr*eigs

        _eigs = eigs.flatten()
        ind = np.argmax(np.real(_eigs))
        phase = _eigs[ind]/np.abs(_eigs[ind])
        eigs /= phase

        disp = np.real(eigs)
        disp *= a/disp.max() # set amplitude

        fig, ax = plt.subplots(figsize=(10,10))

        cu = np.flatnonzero(nums==0)
        o = np.flatnonzero(nums==1)
        
        ax.quiver(pos[:,0],pos[:,1],disp[:,0],disp[:,1],angles='xy',scale_units='xy',
                scale=1,headwidth=3,headlength=3,headaxislength=3)
        ax.scatter(pos[cu,0],pos[cu,1],s=500,c='b',marker='o',edgecolors='k',linewidths=2)
        ax.scatter(pos[o,0],pos[o,1],s=200,c='r',marker='o',edgecolors='k',linewidths=2)

        lims = [pos[:,0].min()-1/2,pos[:,0].max()+1/2,pos[:,1].min()-1/2,pos[:,1].max()+1/2]
        ax.axis(lims)

        plt.show()

    # ----------------------------------------------------------------------------------------------

    def plot_dispersion(self,qpt=None,mode=None):
        
        fig, ax = plt.subplots(figsize=(10,10))
        for ii in range(self.num_modes):
            plt.plot(self.qpts_dist,self.freqs[:,ii],marker='o',ms=0,lw=2,ls='-',c='k')

        if qpt is not None and mode is not None:
            qpt = np.array(qpt,dtype=float)
            qpt_ind = self.get_qpt_ind(qpt)
            plt.plot(self.qpts_dist[qpt_ind],self.freqs[qpt_ind,mode],marker='o',ms=10,c='b')

        plt.show()

    # ----------------------------------------------------------------------------------------------

    def plot_both(self,qpt=[0,0],mode=0,sc=1,a=0.5,figname=None):
        
        qpt = np.array(qpt,dtype=float)
        qpt_ind = self.get_qpt_ind(qpt)

        eigs = self.eigvecs[qpt_ind,mode,...]
        eigs = eigs.reshape(self.num_atoms,3)[:,:2]
        
        masses = np.tile(self.masses.reshape(self.num_atoms,1),reps=(1,2))
        eigs = eigs/np.sqrt(masses)

        eigs, pos, nums = self._make_supercell(sc,eigs)

        qc = self.qpts_cart[qpt_ind,:]
        qc = np.tile(qc.reshape(1,2),reps=(self.num_atoms*self.mult,1))
        exp_iqr = np.exp(1j*np.sum(qc*pos,axis=1))
        exp_iqr = np.tile(exp_iqr.reshape(self.num_atoms*self.mult,1),reps=(1,2))
        eigs = exp_iqr*eigs

        _eigs = eigs.flatten()
        ind = np.argmax(np.real(_eigs))
        phase = _eigs[ind]/np.abs(_eigs[ind])
        eigs /= phase

        disp = np.real(eigs)
        disp *= a/disp.max() # set amplitude

        fig, ax = plt.subplots(1,2,figsize=(9,4),gridspec_kw={'width_ratios':[1,1]},
                               num=1,clear=True)

        cu = np.flatnonzero(nums==0)
        o = np.flatnonzero(nums==1)
        
        ax[1].quiver(pos[:,0],pos[:,1],disp[:,0],disp[:,1],angles='xy',scale_units='xy',
                scale=1,headwidth=3,headlength=3,headaxislength=3)
        ax[1].scatter(pos[cu,0],pos[cu,1],s=100,c='b',marker='o',edgecolors='k',linewidths=2)
        ax[1].scatter(pos[o,0],pos[o,1],s=50,c='r',marker='o',edgecolors='k',linewidths=2)

        lims = [pos[:,0].min()-1/2,pos[:,0].max()+1/2,pos[:,1].min()-1/2,pos[:,1].max()+1/2]
        ax[1].axis(lims)

        for ii in range(self.num_modes):
            ax[0].plot(self.qpts_dist,self.freqs[:,ii],marker='o',ms=0,lw=1,ls='-',c='k')

        if qpt is not None and mode is not None:
            qpt = np.array(qpt,dtype=float)
            qpt_ind = self.get_qpt_ind(qpt)
            ax[0].plot(self.qpts_dist[qpt_ind],self.freqs[qpt_ind,mode],marker='o',ms=10,c='b')

        fig.suptitle(f'qpt: {qpt[0]:.3f}, {qpt[1]:.3f} | mode: {mode}', fontsize=12)

        if figname is not None:
            plt.savefig(figname, bbox_inches='tight', dpi=300)

        plt.show()
        plt.close()
        # plt.clf()

    # ----------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    
    p = plot_phonons()

    # p.plot_qpts()

    # q = [0.5,0.5]
    # m = 8

    # p.plot_dispersion(q,m)
    # p.plot_displacements(q,m,sc=3,a=0.15)

    q = [0.5,0.5]
    m = 8
    p.plot_both(q,m,sc=2,a=0.15,figname='full_breathing.png')
    
    q = [0.5,0.5]
    m = 7
    p.plot_both(q,m,sc=2,a=0.15,figname='quadrupolar.png')
    
    q = [0.0,0.5]
    m = 8
    p.plot_both(q,m,sc=2,a=0.15,figname='buckling_or_smth.png')
    
    q = [0.0,0.5]
    m = 7
    p.plot_both(q,m,sc=2,a=0.15,figname='half_breathing.png')

    q = [0.0,0.0]
    m = 7
    p.plot_both(q,m,sc=2,a=0.15,figname='zone_center_7.png')

    q = [0.0,0.0]
    m = 8
    p.plot_both(q,m,sc=2,a=0.15,figname='zone_center_8.png')

    exit()

# --------------------------------------------------------------------------------------------------

