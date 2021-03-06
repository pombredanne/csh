#!/usr/bin/env python
import getopt, sys, os
import numpy as np
import pyfits
from pylab import matplotlib
import matplotlib.pyplot as plt
from linear_cut import linear_cut

# data
data_path = os.path.join(os.getenv('HOME'), 'data', 'csh', 'output') + os.sep
fname_ext = [data_path + 'ngc6946_cross_robust_noc_photproj.fits',
             data_path + 'ngc6946_cross_robust_noc.fits',
             data_path + 'ngc6946_cross_robust_ca.fits',
             data_path + 'ngc6946_cross_robust_cs.fits',
             data_path + 'ngc6946_cross_robust.fits',
             ]
letters = ['a', 'b', 'c', 'd', 'e']
letters = ['(' + l + ')' for l in letters]
markers = ['-o', '-v', '-s', '-p', '-*']
out_fname = data_path + 'ngc6946_cross_robust_line_cut_grid' + '.png'

# create grid
# figure
fig = plt.figure()

labels = ['PL', 'PLI', 'ACI', 'HCI', 'NOC']
labels = ['(' + l + ')' for l in labels]

# loop on each map
for i, fname in enumerate(fname_ext):
    data = np.flipud(pyfits.fitsopen(fname)[0].data.T)
    if i == 0:
        data /= 8.
    data[np.isnan(data)] = 0
    plt.plot(linear_cut(data, xmin=153, xmax=136, ymin=85, ymax=95, N=20), 
             markers[i], label = labels[i])

plt.legend()
plt.show()
fig.savefig(out_fname)
