import numpy as np
from matplotlib import pyplot as plt

from m_phase_calculator import c_text_file_phase_calculator, c_example_phase_calculator


# --------------------------------------------------------------------------------------------------

class _c_random_drifter:

    # ----------------------------------------------------------------------------------------------

    def __init__(self,phase_diagram,count):
    
        """
        drifter that explores the phase diagram by drifting from left to right along the x-axis.
        one they hit a phase boundary, they stop drifting  and explore the phase boundary to its 
        ends. if they cross known phases, they continue  drifting since any part of a known phase 
        is connected a previous drift and the new drifter will, by design, retraverse the known 
        phase boundary. so instead, it continues drifting.
        """

        self.phase_diagram = phase_diagram
        self.count = count

    # ----------------------------------------------------------------------------------------------

    def _init_pos(self):
    
        """
        initialize the position of the drifter. we dont want to land on a previously checked point,
        so we keep guessing until we find a point that has not been checked.
        """

        _inds = np.copy(self.phase_diagram.inds)   
        _num_inds = _inds.shape[0]
        np.random.shuffle(_inds)

        for ii in range(_num_inds):

            x, y = _inds[ii,:]
            if self.phase_diagram.phases[x,y] < 0:
                return x, y
            
        msg = '\n!!! ERROR !!!\ncould not find an unvisited point in the phase diagram!\n'
        print(msg)

    # ----------------------------------------------------------------------------------------------

    def drift(self):
    
        """
        run the drifting algorithm. start driting and keep taking steps until we hit a phase 
        boundary or go out of bounds. if out of bonds, stop drifting. if we hit a phase
        boundary, we switch over to algorithm for traversing the phase boundary.
        """

        x, y = self._init_pos()
        phase = self.check_phase(x,y)
        self.phase_diagram.phases[x,y] = phase

        # randomly choose between vertical and horizontal drift
        if np.random.rand() < 0.5:
            step = np.array([1,0],dtype=int)
        else:
            step = np.array([0,1],dtype=int)
        
        # randomly choose between increasing and decreasing steps
        if np.random.rand() < 0.5:
            sign = 1
        else:
            sign = -1

        # keep stepping until we hit a phase boundary or go out of bounds
        while True:

            # take steps until we find a point that has not been checked
            new_phase, new_x, new_y = self._step(x,y,step,sign)
            x, y = new_x, new_y

            # # take steps until we find a point that has not been checked
            # new_phase, new_x, new_y = self._random_step(x,y)
            # x, y = new_x, new_y

            # if new point is same phase as this point, continue drifting
            if new_phase == phase:
                continue

            # if now point is out of bounds, stop drifting
            elif new_phase is None:
                msg = '\nreached boundary\n'
                print(msg)
                break
            
            # if we crossed a phase boundary, switch to phase boundary traversal algorithm
            else:

                msg = '\ncrossed a phase boundary!\n'
                print(msg)

                phase = new_phase
                self._traverse_boundary(phase,x,y)
                # new_phase, new_x, new_y = self._random_step(phase,x,y)

                break
    
    # ----------------------------------------------------------------------------------------------

    def _traverse_boundary(self,phase,x,y):
    
        """
        ...
        """

        x = int(x)
        y = int(y)
        previous_coords = [] 
        previous_phase = []

        count = 0
        while True:

            print('\ncount:',count)
            print('previous coords:',previous_coords)
            print('previous phase:',previous_phase)
            print('current coords:',(x,y))
            print('current phase:',phase)  
            count += 1
            # if count == 100:
            #     break

            neighbor_inds, num_neighbors = self._get_neighbor_inds(x,y)
            back_track = True

            for ii in range(num_neighbors):

                new_x, new_y = neighbor_inds[ii]
        
                # this point already checked, so check next neighbor
                if self.phase_diagram.phases[new_x,new_y] >= 0:
                    continue

                # this point not checked, so check it
                new_phase = self.check_phase(new_x,new_y)
                self.phase_diagram.phases[new_x,new_y] = new_phase

                # if new_phase is same as current, we didnt cross the boundary so step again
                if new_phase == phase: 
                    continue

                # if we crossed the phase boundary, the phase changed - we step in that direction
                else:
                    
                    # add this point to the queue
                    previous_coords.append((x,y))
                    previous_phase.append(phase)

                    x = new_x
                    y = new_y
                    phase = new_phase

                    # don't step backwards
                    back_track = False

                    break

            if back_track:

                # if the stack of previous coordinates is empty, we are done!
                if len(previous_coords) == 0:

                    msg = '\nfinished!\n'
                    print(msg)

                    break

                msg = '\nno step taken, going back to previous point\n'
                print(msg)

                x, y = previous_coords[-1]
                previous_coords.pop(-1)
                                
                phase = previous_phase[-1]
                previous_phase.pop(-1)

    # ----------------------------------------------------------------------------------------------

    def _step(self,x,y,step,sign):
    
        """
        take a step along "step" in the direction of "sign". if the step lands on a previously 
        checked point, just step again. keep stepping until we find an unchecked point or go out 
        of bounds. if the step goes out of bounds, return None. 
        """
    
        dx = step[0]*sign
        dy = step[1]*sign

        new_x = np.copy(x)
        new_y = np.copy(y)

        while True:

            # take a step         
            new_x += dx
            new_y += dy

            # out of bounds check
            flag = False
            if new_x < 0:
                flag = True
                new_x = 0
            if new_x >= self.phase_diagram.num_x:
                flag = True
                new_x = self.phase_diagram.num_x-1
            if new_y < 0:
                flag = True
                new_y = 0
            if new_y >= self.phase_diagram.num_y:
                flag = True
                new_y = self.phase_diagram.num_y-1
            if flag:
                return None, new_x, new_y
            
            # if the point has already been checked, skip it and step again
            if self.phase_diagram.phases[new_x,new_y] >= 0:
                continue

            # if the point has not been checked, check it
            else:
                
                new_phase = self.check_phase(new_x,new_y)
                self.phase_diagram.phases[new_x,new_y] = new_phase

                return new_phase, new_x, new_y

    # ----------------------------------------------------------------------------------------------

    def _random_step(self,x,y):
    
        """
        take a random step to a neighboring point. if the point has already been visited,
        skip it.
        """

        neighbor_inds, num_neighbors = self._get_neighbor_inds(x,y,rectilinear=True)
        np.random.shuffle(neighbor_inds)

        for ii in range(num_neighbors):

            new_x, new_y = neighbor_inds[ii]

            if self.phase_diagram.phases[new_x,new_y] >= 0:
                continue

            if self.phase_diagram.phases[new_x,new_y] < 0:

                new_phase = self.check_phase(new_x,new_y)
                self.phase_diagram.phases[new_x,new_y] = new_phase

                return new_phase, new_x, new_y
        
        return None, new_x, new_y

    # ----------------------------------------------------------------------------------------------

    def _get_neighbor_inds(self,x,y,rectilinear=False):

        """
        get inds for all neighbors within bounds
        """

        _num_x = self.phase_diagram.num_x
        _num_y = self.phase_diagram.num_y
    
        if x == 0:
            _x_inds = [0,1]
        elif x == _num_x-1:
            _x_inds = [_num_x-2,_num_x-1]
        else:
            _x_inds = [x-1,x,x+1]

        if y == 0:
            _y_inds = [0,1]
        elif y == _num_y-1:
            _y_inds = [_num_y-2,_num_y-1]
        else:
            _y_inds = [y-1,y,y+1]

        _neighbor_x, _neighbor_y = np.meshgrid(_x_inds,_y_inds,indexing='ij')
        neighbor_inds = np.c_[ _neighbor_x.flatten(), _neighbor_y.flatten() ]

        _dist = neighbor_inds - np.tile(np.array([x,y]),reps=(neighbor_inds.shape[0],1))
        _dist = np.linalg.norm(_dist,axis=1)

        if rectilinear:

            # remove diagonal neighbors
            _inds = np.flatnonzero(_dist == 1)
            neighbor_inds = neighbor_inds[_inds,:]
        else:
            # remove the point itself
            _inds = np.flatnonzero(_dist > 0)
            neighbor_inds = neighbor_inds[_inds,:]

        return neighbor_inds, neighbor_inds.shape[0]

    # ----------------------------------------------------------------------------------------------

    def _check_neighbors(self,x,y):

        """
        check phase of all neighboring points. 
        """

        neighbor_inds, num_neighbors = self._get_neighbor_inds(x,y)
    
        neighbor_phases = -1*np.zeros(num_neighbors)
        neighbor_checked = False*np.zeros(num_neighbors,dtype=bool)

        for ii in range(num_neighbors):

            _x, _y = neighbor_inds[ii]

            if self.phase_diagram.phases[_x,_y] < 0:

                _phase = self.check_phase(_x,_y)

                self.phase_diagram.phases[_x,_y] = _phase

                neighbor_phases[ii] = _phase
                neighbor_checked[ii] = True

            else:

                _phase = self.phase_diagram.phases[_x,_y]
                neighbor_phases[ii] = _phase
                neighbor_checked[ii] = False

        return neighbor_inds, neighbor_phases, neighbor_checked
                
    # ----------------------------------------------------------------------------------------------

    def check_phase(self,x_ind,y_ind):
    
        """
        interface to phase calculator. have to convert the x and y indices to coordinates 
        in range [0,1] 
        """

        x = self.phase_diagram.x[x_ind]
        y = self.phase_diagram.y[y_ind]

        # this expects x and y to be in the range [0,1]
        phase = self.phase_diagram.check_phase(x,y)

        return phase

    # ----------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

class c_phase_diagram:
    
    # ----------------------------------------------------------------------------------------------

    def __init__(self,check_phase,num_x,num_y,phase_diagram=None):

        """
        check_phase is call back that takes x and y coords and args and returns phase. expects
            that phases are integers > 0. 

        num_x, num_y is the grid spacing along x and y. grid is uniformly increasing and
            rectilinear; if you want non-rectilinear or non-uniform spacing, convert the 
            coordinates in your call back.  

        init_x, init_y is the number of initial x and y coordinates to start the exploration.
        """

        self.check_phase = check_phase
        self.num_x = num_x
        self.num_y = num_y

        self._generate_coords()

        # unchecked phases are -1
        if phase_diagram is None:
            self.phases = -1*np.ones(self.grid_shape,dtype=int)
        else:
            self.phases = phase_diagram

    # ----------------------------------------------------------------------------------------------

    def _generate_coords(self):
        
        """
        generate coordinate grid
        """

        self.x = np.linspace(0,1,self.num_x)
        self.y = np.linspace(0,1,self.num_y)
        
        self.x_grid, self.y_grid = np.meshgrid(self.x,self.y,indexing='ij')
        self.coords = np.c_[self.x_grid.flatten(), self.y_grid.flatten()]
        self.grid_shape = self.x_grid.shape

        self.x_inds = np.arange(0,self.num_x)
        self.y_inds = np.arange(0,self.num_y)

        self.x_inds_grid, self.y_inds_grid = np.meshgrid(self.x_inds,self.y_inds,indexing='ij')
        self.inds = np.c_[self.x_inds_grid.flatten(),self.y_inds_grid.flatten()]

    # ----------------------------------------------------------------------------------------------

    def random_drifters(self,num_drifters=1):

        """
        explore the phase diagram by seeding num_drifters number of "drifters". they start and a 
        random point and random walk until they hit a phase boundary. once they hit a phase 
        boundary, they traverse it until its end. 
        """

        self.num_drifters = num_drifters
        self.drifters = []

        for ii in range(self.num_drifters):
            
            # create a random drifter
            _drifter = _c_random_drifter(self,ii)
            _drifter.drift()

            # add to the list of drifters
            self.drifters.append(_drifter)

    # ----------------------------------------------------------------------------------------------

    def plot_phase_diagram(self):

        """
        plot the phase diagram on a uniform grid
        """

        num_x = self.num_x
        num_y = self.num_y

        fig, ax = plt.subplots(figsize=(6,6))

        unique_phases = np.unique(self.phases)
        _inds = np.flatnonzero(unique_phases >= 0)
        unique_phases = unique_phases[_inds]
        num_phases = unique_phases.size

        _flat_phases = self.phases.flatten()
        for ii in range(num_phases):
            _inds = np.flatnonzero(_flat_phases == unique_phases[ii])
            _x = self.coords[_inds,0]
            _y = self.coords[_inds,1]
            ax.scatter(_x,_y,s=2)

        plt.show()

    # ----------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
    
if __name__ == '__main__':

    num_x = 100
    num_y = 100

    example = c_example_phase_calculator(num_x,num_y)
    # example.plot_phase_diagram()
    check_phase = example.check_phase

    # phase_checker = c_phase_checker()
    # check_phase = phase_checker.check_phase
    
    phase_diagram = c_phase_diagram(check_phase,num_x,num_y)
    phase_diagram.random_drifters(10)
    phase_diagram.plot_phase_diagram()







