
import sys
from elph_tools.plot_fs import plot_fs

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'electrons_out.hdf5'

plot_fs(input_file)


