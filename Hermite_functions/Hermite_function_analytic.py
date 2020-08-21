import numpy as np
from .is_integer import is_integer

def Hermite_function_analytic(n, x):
    """
    Calculate the nth Hermite function at position x, psi_n(x)
    
    Use analytic expression for psi_n(x)
    
    Parameters:
        n : integer, must be between 0 and 5 inclusive
        x : number or np.ndarray
        
    Returns
    -------
        number or np.ndarray (same format and shape as x)
    """
    
    if not is_integer(n):
        raise TypeError('n must be an integer')
    if n < 0 or n > 5:
        raise ValueError('n must be between 0 and 5')
    
    if n == 0:
        return np.pi**(-1/4) * np.exp(-x**2/2)
    if n == 1:
        return np.sqrt(2) * np.pi**(-1/4) * x * np.exp(-x**2/2)
    if n == 2:
        return (np.sqrt(2) * np.pi**(1/4))**(-1) * (2*x**2 - 1) * np.exp(-x**2/2)
    if n == 3:
        return (np.sqrt(3) * np.pi**(1/4))**(-1) * (2*x**3 - 3*x) * np.exp(-x**2/2)
    if n == 4:
        return (2 * np.sqrt(6) * np.pi**(1/4))**(-1) * (4*x**4 - 12*x**2 + 3) * np.exp(-x**2/2)
    if n == 5:
        return (2 * np.sqrt(15) * np.pi**(1/4))**(-1) * (4*x**5 - 20*x**3 + 15*x) * np.exp(-x**2/2)