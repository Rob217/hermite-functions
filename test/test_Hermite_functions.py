import unittest
import os
import numpy as np

from Hermite_functions.Hermite_functions import Hermite_functions
from Hermite_functions.Hermite_function_direct import Hermite_function_direct


class TestHermiteFunction(unittest.TestCase):
    def testNegativeN(self):
        self.assertRaises(ValueError, Hermite_functions, -1, 0)

    def testNotIntegerN(self):
        self.assertRaises(TypeError, Hermite_functions, 1.0, 0)

    def testXVals(self):

        n_max = 10
        x_vals = [np.linspace(-10, 10, 101), 10, np.array([-0.5])]
        for x in x_vals:
            try:
                expected_vals = np.zeros((n_max + 1, len(x)))
            except TypeError:
                expected_vals = np.zeros((n_max + 1, 1))
            for n in range(n_max + 1):
                expected_vals[n, :] = Hermite_function_direct(n, x)
            np.testing.assert_almost_equal(
                Hermite_functions(n_max, x), expected_vals
            )

    def testReshape(self):
        n = 10
        x = np.ones((2, 3, 4))
        transform_axes = ([0, 1, 2, 3], [3, 1, 0, 2])
        new_dims = (3, 2, 4, 11)
        self.assertEqual(
            Hermite_functions(n, x, transform_axes).shape, new_dims
        )


if __name__ == "__main__":
    unittest.main()
