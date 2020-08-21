import numpy as np

def is_integer(n):
    """
    Checks whether n is an integer or numpy.integer
    
    Parameters
    ----------
        n :number
    
    Returns
    -------
        True -> type(n) is a subclass of int or np.integer
        False -> otherwise
    """
    
    return issubclass(type(n), int) or issubclass(type(n), np.integer)