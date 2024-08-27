import numpy as np

# --------------------------------------------------------------------------------------------------

class phase_getter:

    # ----------------------------------------------------------------------------------------------

    def __init__(self,phase_file='coarse_phases.txt'):

        """
        load data and metadata needed to check phases
        """

        self.phases = np.loadtxt(phase_file,dtype=int).T

        self.num_x, self.num_y = self.phases.shape
        _x = np.arange(0,self.num_x)
        _y = np.arange(0,self.num_y)

        self.phases = self.phases.flatten()

        self.x, self.y = np.meshgrid(_x,_y,indexing='ij')
        self.x = self.x.flatten()
        self.y = self.y.flatten()

    # ----------------------------------------------------------------------------------------------

    def get_phase(self,x,y):

        """
        expects x and y to be between 0 and 1. normalize if u have to.
        it simply finds the nearest phase and returns that.
        """

        _distances = np.sqrt((self.x-x)**2+(self.y-y)**2)
        index = np.argsort(_distances)[0]

        return self.phases[index]

    # ----------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------

class phase_diagram:
    
    # ----------------------------------------------------------------------------------------------

    def __init__(self,get_phase,num_x,num_y):

        """
        get_phase is call back that takes x and y coords and args and returns phase. expects
            that phases are integers > 0. 

        num_x, num_y is the grid spacing along x and y. grid is uniformly increasing and
            rectilinear; if you want non-rectilinear or non-uniform spacing, convert the 
            coordinates in your call back.  
        """

        self.get_phase = get_phase
        self.num_x = num_x
        self.num_y = num_y

        self._generate_coords()

        self.phases = np.zeros(self.grid_shape,dtype=int)

    # ----------------------------------------------------------------------------------------------

    def _generate_coords(self):
        
        """
        generate coordinate grid
        """

        _nx = self.num_x
        _ny = self.num_y
        self.grid_shape = [_nx,_ny]

        self.x = np.arange(0,_nx)
        self.y = np.arange(0,_ny)

    # ----------------------------------------------------------------------------------------------

    def uniform_drifters(self,num_drifters=1):

        """
        explore the phase diagram by launching num_drifters number of calculations that drift
        from right to left along the x-axis. one they hit a phase boundary, they stop drifting 
        and explore the phase boundary to its ends. if they cross known phases, they continue 
        driftin since any part of a known phase is connected a previous drift and the new drifter
        will, by design, retraverse the known phase boundary. continuing drifting  
        """

        _drifter_y = np.random.permutation(self.num_y)[:num_drifters]

        for y in _drifter_y:

            # get phase on left edge
            _phase = self.get_phase(0,y)
            self.phases[0,y] = _phase

            # drift right
            _last_phase = np.copy(_phase)
            for x in self.x[1:]:

                # if this point has been checked before, just keep drifting.
                if self.phases[x,y] != 0:
                    _last_phase = np.copy(self.phases[x,y])
                    continue

                # otherwise, check it.
                _phase = self.get_phase(x,y)
                self.phases[x,y] = _phase

                # if this phase is the same as the last one, we didnt cross a boundary
                if _phase == _last_phase:
                    continue
                
                # we crossed a boundary
                _last_phase = np.copy(_phase)

                # walk along the phase boundary
                self.count = 0
                self._explore(x,y)

        self._write_phase_file()

    # ----------------------------------------------------------------------------------------------

    def _get_neighbor_phases(self,x,y):

        """
        find the neighbors for this coord and get their phases if not already known
        """

        neighbor_x = []
        neighbor_y = []

        for _dx in [-1,0,1]:
            _dx += x

            # exclude inds that are outisde the grid
            if _dx < 0 or _dx >= self.num_x:
                continue

            for _dy in [-1,0,1]:
                _dy += y

                # exclude inds that are outisde the grid
                if _dy < 0 or _dy >= self.num_y:
                    continue

                # skip the x, y coord
                if _dx == x and _dy == y:
                    continue

                neighbor_x.append(_dx)
                neighbor_y.append(_dy)
       
        neighbor_x = np.array(neighbor_x)
        neighbor_y = np.array(neighbor_y)
        neighbor_phases = self.phases[neighbor_x,neighbor_y]

        # if phase at neighbor coord is 0, we need to calculate it
        _check = np.flatnonzero(neighbor_phases == 0)

        #neighbor_x = neighbor_x[_check]
        #neighbor_y = neighbor_y[_check]
        #neighbor_phases = neighbor_phases[_check]

        if _check.size == 0:
            return neighbor_x, neighbor_y, neighbor_phases

        # call get_phase for all neighbors.
        for ii in range(_check.size):
            
            _x = neighbor_x[ii]
            _y = neighbor_y[ii]

            _phase = self.get_phase(_x,_y)
            neighbor_phases[ii] = _phase
            self.phases[_x,_y] = _phase

        return neighbor_x, neighbor_y, neighbor_phases

    # ----------------------------------------------------------------------------------------------

    def _write_phase_file(self,phase_file='calc_phases.txt'):

        """
        write calculated phases to file
        """

        np.savetxt(phase_file,self.phases,fmt='%d')

    # ----------------------------------------------------------------------------------------------

    def _explore(self,x,y):

        """
        explore the phase boundary
        """

        self.count += 1
        print(self.count)
        if self.count % 500 == 0: 
            self._write_phase_file()

        _phase = self.phases[x,y]
        _neighbor_x, _neighbor_y, _neighbor_phases = self._get_neighbor_phases(x,y)

        # if no more neighbors to check, return
        if _neighbor_phases.size == 0:
            return

        _check = np.flatnonzero(_neighbor_phases != _phase)

        # return if none of the neighbor have diff phase, i.e. no phase boundary
        if _check.size == 0:
            return

        # otherwise, explore around all neighbors
        for _ind in _check:
                
            _x = _neighbor_x[_ind]
            _y = _neighbor_y[_ind]

            self._explore(_x,_y)

        return

    # ----------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

num_x = 100; num_y = 100
def get_phase(x,y):
    if (x/100)**2 + (y/100)**2 < 1/2:
        return 1
    else:
        return 2
    

if __name__ == '__main__':
 
    #phase_getter = phase_getter()
    
    phase_diag = phase_diagram(get_phase,100,100)
    phase_diag.uniform_drifters(10)







