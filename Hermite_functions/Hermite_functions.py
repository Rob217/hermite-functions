import numpy as np

try:
    from .is_integer import is_integer
except:
    from is_integer import is_integer


def Hermite_functions(n=0, x=0, transform_axes=()):
    """
    Calculate all Hermite functions psi_m(x) from 0 <= m <= n

    Uses the recursion relation:
        psi_{m}(x) = np.sqrt(2/m) * x * psi_{m-1}(x) - np.sqrt((m-1)/m) * psi_{m-2}(x)

    Returns np.ndarray with an extra dimension of size n.
    If transform_axes not given, this extra dimension is the first dimension.
    Else the dimensions are transformed using the values given in transform_axes.

    Examples
    --------

    >>> n = 10
    >>> x = np.random.rand(2, 3, 4) # shape = [2, 3, 4]
    >>> psi = Hermite_functions(n, x)
    >>> print(psi.shape)
    [11, 2, 3, 4]

    >>> transform_axes = ([0, 1, 2, 3], [3, 0, 1, 2])
    >>> psi = Hermite_functions(n, x, transform_axes)
    >>> print(psi.shape)
    [2, 3, 4, 11]

    Parameters
    ----------
        n : non-negative integer
        x : number or np.ndarray
        transform_axes : list or tuple of the form (old_dims, new_dims)
            old_dims and new_dims are lists of dimension indices (see https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html)

    Returns
    -------
        psi : np.ndarray
    """

    if not is_integer(n):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    try:
        psi = np.zeros((n + 1,) + x.shape)
    except AttributeError:  # x does not have property 'shape'
        psi = np.zeros((n + 1, 1))

    psi[0, :] = np.pi ** (-1 / 4) * np.exp(-(x ** 2) / 2)
    if n == 0:
        return psi

    psi[1, :] = np.sqrt(2) * np.pi ** (-1 / 4) * x * np.exp(-(x ** 2) / 2)
    if n == 1:
        return psi

    for m in range(2, n + 1):
        psi[m, :] = (
            np.sqrt(2 / m) * x * psi[m - 1, :] - np.sqrt((m - 1) / m) * psi[m - 2, :]
        )

    if transform_axes:
        return np.moveaxis(psi, transform_axes[0], transform_axes[1])

    return psi


if __name__ == "__main__":

    x_test = [5, np.random.rand(1), np.random.rand(5), np.random.rand(2, 3, 4)]

    n_test = [0, 10, 1000]

    for x in x_test:
        for n in n_test:
            psi = Hermite_functions(n, x)
            print(psi.shape)

    transform_axes = ([0, 1, 2, 3], [3, 0, 1, 2])
    psi = Hermite_functions(n_test[-1], x_test[-1], transform_axes)
    print(psi.shape)

    print("testing successful")
