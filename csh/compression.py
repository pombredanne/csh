"""Define compression modes"""
import numpy as np
from copy import copy
import lo

def averaging(shape, factor):
    """Averaging compression mode"""
    return lo.binning(shape, factor=8, axis=1, dtype=np.float64)

def cs(shape, factor):
    """ Compressed sensing compression mode"""
    # transform
    H = lo.fht(shape, axes=0)
    # mask
    start_ind = np.resize(np.arange(factor), shape[0])
    mask = np.zeros(shape)
    for i in xrange(mask.shape[0]):
        mask[i, start_ind[i]::factor] = 1.
    M = lo.mask(mask, dtype=np.float64)
    C = M * H
    return C

def binning3d(shape, factors):
    if len(shape) is not 3:
        raise ValueError('Expected 3d shape')
    B0 = lo.binning(shape, factor=factors[0], axis=0, dtype=np.float64)
    shape1 = np.asarray(copy(shape))
    shape1[0] /= factors[0]
    B1 = lo.binning(shape1, factor=factors[1], axis=1, dtype=np.float64)
    shape2 = np.asarray(copy(shape1))
    shape2[1] /= factors[1]
    B2 = lo.binning(shape2, factor=factors[2], axis=2, dtype=np.float64)
    return B2 * B1 * B0