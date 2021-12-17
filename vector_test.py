from vector import Vector
import math
import unittest

import numpy as np

class Vector_test(unittest.TestCase):

    def test_default(self):
        v = Vector()
        self.assertEquals([0,0,0], [v.x, v.y, v.z])

    def test_fromList(self):
        v = Vector.fromList([1,2,3])
        self.assertEquals([1,2,3], [v.x, v.y, v.z])

    def test_getitem(self):
        v = Vector.fromList([1,2,3])
        self.assertEqual(1, v.x)
        self.assertEqual(2, v.y)
        self.assertEqual(3, v.z)
   
    def test_xyz(self):
        v = Vector.fromList([4,3,2])
        self.assertEqual(4, v.x)
        self.assertEqual(3, v.y)
        self.assertEqual(2, v.z)

    def test_length(self):
        v = Vector.fromList([4,3,2])
        self.assertEqual(math.sqrt(4**2+3**2+2**2), v.length())

    def test_normalize(self):
        self.assertEquals(Vector(1,0,0), Vector(2,0,0).normalize())
        self.assertEquals(Vector(0,1,0), Vector(0,2,0).normalize())
        self.assertEquals(Vector(0,0,1), Vector(0,0,2).normalize())
        v = Vector(3.4, 5.6, 7.8)
        l = v.length()
        self.assertTrue(Vector(v.x/l, v.y/l, v.z/l).isClose(v.normalize()))

    def test_dot(self):
        v0 = Vector(1,2,3)
        v1 = Vector(5,6,7)

        self.assertEqual(np.dot([1,2,3], [5,6,7]), v0.dot(v1))

if __name__ == '__main__':
    unittest.main()