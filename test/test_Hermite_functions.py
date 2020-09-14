import pytest
import numpy as np
from hermite_functions.hermite_functions import hermite_functions


# test incorrect inputs
def test_non_integer_n():
    with pytest.raises(TypeError, match='n must be an integer'):
        hermite_functions(1.0, 0)

def test_negative_n():
    with pytest.raises(ValueError, match=r'n must be non-negative'):
        hermite_functions(-1, 0)

@pytest.mark.parametrize("n", [-1, 6,])
def test_n_outside_range(n):
    with pytest.raises(ValueError):
        hermite_functions(n, 0, method='analytic')

def test_incorrect_method():
    with pytest.raises(ValueError, match="Method not recognized."):
        hermite_functions(0, 0, method='incorrect method')


# test method: analytic
test_data_analytic = [
    (0, 0, 0.7511255444649425),
    (1, 0, 0),
    (2, 0, -0.5311259660135984),
    (3, 0, 0),
    (4, 0, 0.4599685791773267),
    (5, 0, 0),
    (0, 1, 0.45558067201133257),
    (1, 1, 0.6442883651134752),
    (1, np.array([-1, -0.5, 0]), np.array([-0.64428837, -0.46871702, 0.])),
]
@pytest.mark.parametrize("n,x,out", test_data_analytic)
def test_analytic(n,x,out):
    assert hermite_functions(n, x, all_n = False, method='analytic') == pytest.approx(out)

def test_analytic_all_n():
    x = np.linspace(-2, 2, 3)
    n = 5
    psi_expected = np.zeros([n+1, len(x)])
    for m in range(n+1):
        psi_expected[m, :] = hermite_functions(m, x, all_n=False, method='analytic')
    np.testing.assert_array_equal(
        hermite_functions(n, x, all_n=True, method='analytic'),
        psi_expected
    )


# test method: direct
@pytest.mark.parametrize("n,x,out", test_data_analytic)
def test_direct(n,x,out):
    assert hermite_functions(n, x, all_n = False, method='direct') == pytest.approx(out)

def test_direct_all_n():
    x = np.linspace(-2, 2, 11)
    n = 10
    psi_expected = np.zeros([n+1, len(x)])
    for m in range(n+1):
        psi_expected[m, :] = hermite_functions(m, x, all_n=False, method='direct')
    np.testing.assert_array_equal(
        hermite_functions(n, x, all_n=True, method='direct'),
        psi_expected
    )


# test method: recursive
test_data = [
    (0, 0),
    (1, 0),
    (1, 1),
    (2, 1),
    (3, 3.3),
    (10, 3.3),
    (5, np.array([0.0, 0.5, 1.2])),
]

@pytest.mark.parametrize("n,x", test_data)
def test_simple(n,x):
    assert hermite_functions(n, x, all_n=False) == pytest.approx(hermite_functions(n, x, all_n=False, method='direct'))

@pytest.mark.parametrize("n,x", test_data)
def test_all_n(n,x):
    assert hermite_functions(n, x, all_n=True) == pytest.approx(hermite_functions(n, x, all_n=True, method='direct'))

# test move_axes
@pytest.mark.parametrize('n,x', [
    (5, np.mgrid[-2:3, 0:4]),
    (0, np.mgrid[-2.1:4.5, 0:8]),
    (1, np.mgrid[-1:1, -2:2]),
])
def test_move_axes(n,x):
    reshape = ([0, 1, 2, 3], [1, 3, 2, 0])
    out = hermite_functions(n, x, all_n=True, move_axes=reshape)
    out_check = np.moveaxis(hermite_functions(n, x, all_n=True), reshape[0], reshape[1])
    np.testing.assert_array_equal(out, out_check)
