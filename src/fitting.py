import numpy as np


def IV_Fitting(v, i_s, q, nkT, cst, v_list=[], c_list=[]):
    polyfit_iv = np.polyfit(v_list, c_list, 12)
    fit_iv = np.poly1d(polyfit_iv)
    return abs(i_s * (np.exp(q * v / nkT) - 1)) + cst * fit_iv(v)
