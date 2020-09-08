import numpy as np
from .is_integer import is_integer


def Hermite_function(n=0, x=0):
    """
    Calculate the nth Hermite function at position x

    Uses the recursion relation:
        psi_{n}(x) = np.sqrt(2/n) * x * psi_{n-1}(x) - np.sqrt((n-1)/n) * psi_{m-2}(x)

    Compared with Hermite_functions, Hermite_function is more memory efficient since it
    only stores psi_{m}, psi_{m-1}, and psi_{m-2} for each recursion step rather than
    storing all psi_{m} from 0 <= m <= n

    Parameters
    ----------
        n : non-negative integer
        x : number or np.ndarray

    Returns
    -------
        psi_2 : number or np.ndarray (same format and shape as x)
    """

    if not is_integer(n):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    psi_0 = np.pi ** (-1 / 4) * np.exp(-(x ** 2) / 2)
    if n == 0:
        return psi_0

    psi_1 = np.sqrt(2) * np.pi ** (-1 / 4) * x * np.exp(-(x ** 2) / 2)
    if n == 1:
        return psi_1

    for m in range(2, n + 1):
        psi_2 = np.sqrt(2 / m) * x * psi_1 - np.sqrt((m - 1) / m) * psi_0
        psi_0 = psi_1  # slower if use psi_0 = psi_1.copy()
        psi_1 = psi_2

    return psi_2
