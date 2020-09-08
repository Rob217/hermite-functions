import unittest
import os
import numpy as np

from Hermite_functions.Hermite_function import Hermite_function
from Hermite_functions.Hermite_function_direct import Hermite_function_direct

class TestHermiteFunction(unittest.TestCase):

    def testNegativeN(self):
        self.assertRaises(ValueError, Hermite_function, -1, 0)

    def testNotIntegerN(self):
        self.assertRaises(TypeError, Hermite_function, 1.0, 0)

    def testNVals(self):
        for n in range(0, 10):
            np.testing.assert_almost_equal(Hermite_function(n, 1),
                                           Hermite_function_direct(n, 1))

    def testXVals(self):

        x_vals = [np.linspace(-10, 10, 101),
                  10,
                  -0.5]
        for x in x_vals:
            np.testing.assert_almost_equal(Hermite_function(10, x),
                                           Hermite_function_direct(10, x))



if __name__ == '__main__':
    unittest.main()
