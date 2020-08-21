import numpy as np
from .is_integer import is_integer

def Hermite_functions(n=0, x=0):
    """
    Calculate all Hermite functions psi_m(x) from 0 <= m <= n
    
    Uses the recursion relation:
        psi_{m}(x) = np.sqrt(2/m) * x * psi_{m-1}(x) - np.sqrt((m-1)/m) * psi_{m-2}(x)
    
    Parameters
    ----------
        n : non-negative integer
        x : number or np.ndarray
    
    Returns
    -------
        psi : dict
            keys -> values of m
            values -> psi_m(x), same format as x
    """
    
    if not is_integer(n):
        raise TypeError('n must be an integer')
    if n < 0:
        raise ValueError('n must be non-negative')
        
    psi = {}
    
    psi[0] = np.pi**(-1/4) * np.exp(-x**2/2)
    if n == 0:
        return psi
    
    psi[1] = np.sqrt(2) * np.pi**(-1/4) * x * np.exp(-x**2/2)
    if n == 1:
        return psi

    for m in range(2, n+1):
        psi[m] = np.sqrt(2/m) * x * psi[m-1] - np.sqrt((m-1)/m) * psi[m-2]
        
    return psi