import numpy as np
from scipy.special import eval_hermite, factorial


def hermite_functions(n, x, all_n=True, move_axes=(), method="recursive"):
    """
    Calculate the Hermite functions up to the nth order at position x, psi_n(x).

    For details see:
    https://en.wikipedia.org/wiki/Hermite_polynomials#Hermite_functions

    If all_n == True, then return all Hermite functions up to n
    If all_n == False, only return nth Hermite function
    If using recursive method, then the latter is more memory efficient as it only stores
    psi_n, psi_{n-1}, and psi_{n-2}

    The 'move_axes' option causes the output dimensions to be swapped around
    using np.moveaxis.

    Uses one of three possible calculation methods:
        'recursive' - Uses recursive method. Most efficient for n > 5.
        'direct'    - Calculates directly using Hermite polynomials.
                      Inefficient due to factorial and Hermite polynomial,
                      although useful for comparison when testing
        'analytic'  - Uses analytic expressions (only for n <= 5)

    Recursion relation:
        psi_n(x) = sqrt(2/n) * x * psi_{n-1}(x) - sqrt((n-1)/n) * psi_{n-2}(x)

    Examples:

    >>> x = np.mgrid[-2:3, 0:4]
    >>> x.shape
    (2, 5, 4)
    >>> n = 5
    >>> psi = hermite_functions(n, x, all_n=False)
    >>> psi.shape
    (2, 5, 4)
    >>> psi = hermite_functions(n, x, all_n=True)
    >>> psi.shape
    (6, 2, 5, 4)
    >>> reshape = ([0, 1, 2, 3], [1, 3, 2, 0])
    >>> psi = hermite_functions(n, x, all_n=True, move_axes=reshape)
    >>> psi.shape
    (4, 6, 5, 2)

    """

    if method not in ["recursive", "analytic", "direct"]:
        raise ValueError("Method not recognized.")
    if not (issubclass(type(n), int) or issubclass(type(n), np.integer)):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    if method == "analytic" and (n > 5):
        raise ValueError("n must not be greater than 5 for analytic calculation.")

    if all_n:
        psi_n = _Hermite_all_n(n, x, method)
    else:
        psi_n = _Hermite_single_n(n, x, method)

    if move_axes:
        psi_n = np.moveaxis(psi_n, move_axes[0], move_axes[1])

    return psi_n


def _Hermite_single_n(n, x, method):
    """
    Calculates psi_n(x) for a single value of n.
    """

    if method == "analytic":
        return _H_analytic(n, x)

    if method == "direct":
        return _H_direct(n, x)

    psi_m_minus_2 = _H_analytic(0, x)
    if n == 0:
        return psi_m_minus_2

    psi_m_minus_1 = _H_analytic(1, x)
    if n == 1:
        return psi_m_minus_1

    for m in range(2, n + 1):
        psi_m = _H_recursive(m, x, psi_m_minus_2, psi_m_minus_1)
        psi_m_minus_2 = psi_m_minus_1
        psi_m_minus_1 = psi_m

    return psi_m


def _Hermite_all_n(n, x, method):
    """
    Calcualtes psi_m(x) for all 0 <= m <= n.
    """

    try:
        psi_n = np.zeros((n + 1,) + x.shape)
    except AttributeError:  # x does not have property 'shape'
        psi_n = np.zeros((n + 1, 1))

    if method == "analytic":
        for m in range(n + 1):
            psi_n[m, :] = _H_analytic(m, x)
        return psi_n

    if method == "direct":
        for m in range(n + 1):
            psi_n[m, :] = _H_direct(m, x)
        return psi_n

    psi_n[0, :] = _H_analytic(0, x)
    if n == 0:
        return psi_n

    psi_n[1, :] = _H_analytic(1, x)
    if n == 1:
        return psi_n

    for m in range(2, n + 1):
        psi_n[m, :] = _H_recursive(m, x, psi_n[m - 2, :], psi_n[m - 1, :])

    return psi_n


def _H_recursive(m, x, psi_m_minus_2, psi_m_minus_1):
    """
    Calculate psi_m(x) using recursion relation.
    """
    return np.sqrt(2 / m) * x * psi_m_minus_1 - np.sqrt((m - 1) / m) * psi_m_minus_2


def _H_analytic(n, x):
    """
    Analytic expressions for psi_n(x) for 0 <= n <= 5.
    """

    if n == 0:
        return np.pi ** (-1 / 4) * np.exp(-(x ** 2) / 2)
    if n == 1:
        return np.sqrt(2) * np.pi ** (-1 / 4) * x * np.exp(-(x ** 2) / 2)
    if n == 2:
        return (
            (np.sqrt(2) * np.pi ** (1 / 4)) ** (-1)
            * (2 * x ** 2 - 1)
            * np.exp(-(x ** 2) / 2)
        )
    if n == 3:
        return (
            (np.sqrt(3) * np.pi ** (1 / 4)) ** (-1)
            * (2 * x ** 3 - 3 * x)
            * np.exp(-(x ** 2) / 2)
        )
    if n == 4:
        return (
            (2 * np.sqrt(6) * np.pi ** (1 / 4)) ** (-1)
            * (4 * x ** 4 - 12 * x ** 2 + 3)
            * np.exp(-(x ** 2) / 2)
        )
    if n == 5:
        return (
            (2 * np.sqrt(15) * np.pi ** (1 / 4)) ** (-1)
            * (4 * x ** 5 - 20 * x ** 3 + 15 * x)
            * np.exp(-(x ** 2) / 2)
        )
    raise ValueError("n must be an integer between 0 and 5")


def _H_direct(n, x):
    """
    Calculate psi_n(x) using explicit definition.
    """
    return (
        1
        / np.sqrt(2 ** n * factorial(n))
        * np.pi ** (-1 / 4)
        * np.exp(-(x ** 2) / 2)
        * eval_hermite(n, x)
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
