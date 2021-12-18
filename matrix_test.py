from matrix import Matrix
from vector import Vector
import unittest
import math
import numpy as np

class Matrix_test(unittest.TestCase):

    def test_init(self):
        m = Matrix()
        for i in range(4):
            for j in range(4):
                self.assertEqual(m.data[i][j], 1 if i == j else 0, f'default init failed at {i},{j}')
        
        testData = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        m = Matrix(testData)
        for i in range(4):
            for j in range(4):
                self.assertEqual(m.data[i][j], testData[i][j], f'init with list failed at {i},{j}')

    def test_getitem(self):
        m = Matrix()
        for i in range(4):
            for j in range(4):
                self.assertEqual(m[(i,j)], 1 if i == j else 0, f'getitem default init failed at {i},{j}')
        
        testData = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        m = Matrix(testData)
        for i in range(4):
            for j in range(4):
                self.assertEqual(m[(i,j)], testData[i][j], f'getitem with list init failed at {i},{j}')

    def test_isClose(self):
        testData = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        m1 = Matrix(testData)
        m2 = Matrix(testData)
        self.assertTrue(m1.isClose(m2))

        for i in range(4):
            for j in range(4):
                testData = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
                m1 = Matrix(testData)
                testData[i][j] = -42
                m2 = Matrix(testData)
                self.assertFalse(m1.isClose(m2), f'isClose with difference at {i},{j} failed')

    def test_matmul(self):
        m1 = Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        m2 = Matrix([[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32]])

        self.assertTrue(m1.isClose(Matrix() @ m1))
        self.assertTrue(m2.isClose(m2 @ Matrix()))

        m = m1 @ m2
        exp = Matrix([
            [1*17+2*21+3*25+4*29, 1*18+2*22+3*26+4*30, 1*19+2*23+3*27+4*31, 1*20+2*24+3*28+4*32],
            [5*17+6*21+7*25+8*29, 5*18+6*22+7*26+8*30, 5*19+6*23+7*27+8*31, 5*20+6*24+7*28+8*32],
            [9*17+10*21+11*25+12*29, 9*18+10*22+11*26+12*30, 9*19+10*23+11*27+12*31, 9*20+10*24+11*28+12*32],
            [13*17+14*21+15*25+16*29, 13*18+14*22+15*26+16*30, 13*19+14*23+15*27+16*31, 13*20+14*24+15*28+16*32]])
        self.assertTrue(exp.isClose(m))
    
        v = Vector(10,11,12)

        self.assertTrue(v.isClose(Matrix()@v))

        w = 10*13+11*14+12*15+16
        exp = Vector(
            (10*1+11*2+12*3+4)/w,
            (10*5+11*6+12*7+8)/w,
            (10*9+11*10+12*11+12)/w
        )
        self.assertTrue(exp.isClose(m1 @ v))

    def test_fromAxisAngle(self):
        m = Matrix.fromAxisAngle(Vector(1,0,0),0)
        self.assertTrue(Matrix().isClose(m))
        m = Matrix.fromAxisAngle(Vector(0,1,0),np.deg2rad(360))
        self.assertTrue(Matrix().isClose(m, abs_tol=1e-15))
        m = Matrix.fromAxisAngle(Vector(0,0,2),np.deg2rad(3*360))
        self.assertTrue(Matrix().isClose(m, abs_tol=1e-15))

    def test_fromTranslation(self):
        m = Matrix.fromTranslation([0,0,0])
        self.assertTrue(Matrix().isClose(m))
        m = Matrix.fromTranslation(Vector(1,0,0))
        self.assertTrue(Vector(1,0,0).isClose(m@Vector()))
        m = Matrix.fromTranslation([1,2,3])
        self.assertTrue(Vector(1,2,3).isClose(m@Vector()))


if __name__ == '__main__':
    unittest.main()