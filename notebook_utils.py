"""Helper functions for running and processing numerical experiments."""

import numpy as np
import torch as pt


def set_seed(seed):
    pt.manual_seed(seed)
    np.random.seed(seed)
    

def get_sorted_spectrum(filename, f_min = 0.0, i_min = 0.0):
    spectrum = pt.load(filename)
    f, f_std, ci_f = spectrum["frequency"]
    i, i_std, ci_i = spectrum["integral_contribution"]
    f_in_range = f >= f_min
    i_in_range = i >= i_min
    in_range = pt.logical_and(f_in_range, i_in_range)
    f_sort = f[in_range].sort()
    return f_sort.values, f_std[in_range][f_sort.indices], ci_f[in_range][f_sort.indices],\
           i[in_range][f_sort.indices], i_std[in_range][f_sort.indices], ci_i[in_range][f_sort.indices]