from matrix import Matrix
import unittest

import numpy as np

class Matrix_test(unittest.TestCase):

    def test_fromNdArray(self):
        a = np.arange(16).reshape((4,4))
        m1 = Matrix.fromNdArray(a)
        self.assertTrue(np.allclose(m1.ndarray, a))

    

if __name__ == '__main__':
    unittest.main()