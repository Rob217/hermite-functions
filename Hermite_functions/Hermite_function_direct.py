import numpy as np
from scipy.special import eval_hermite, factorial
from .is_integer import is_integer


def Hermite_function_direct(n, x):
    """
    Calculate the nth Hermite function at position x, psi_n(x)

    Uses explicit direct form of the Hermite function:
        psi_n(x) = 1 / np.sqrt(2**n * n!) * np.pi**(-1/4) * np.exp(-x**2/2) * H_n(x)
    where H_n(x) is the physicist's Hermite polynomial

    Parameters
    ----------
        n : non-negative integer
        x : number or np.ndarray

    Returns
    -------
        number or np.ndarray (same format and shape as x)
    """

    if not is_integer(n):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    return (
        1
        / np.sqrt(2 ** n * factorial(n))
        * np.pi ** (-1 / 4)
        * np.exp(-(x ** 2) / 2)
        * eval_hermite(n, x)
    )
