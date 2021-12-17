import math
from vector import Vector
import copy

class Matrix:

    def __init__(self, list=None):
        if list != None:
            assert(type(list) == type([]) and len(list) == 4 and all(len(row) == 4 for row in list))
            self.data = copy.deepcopy(list)
        else:
            self.data = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

    def fromTranslation(translation):
        assert((type(translation) == type([]) and len(translation) == 3))
        m = Matrix()
        m.data[0:3,3] = translation
        return m

    def fromAxisAngle(axis, angle_rad):
        """
        Return the rotation matrix associated with counterclockwise rotation about
        the given axis by angle_rad radians.
        """
        assert((type(axis) == Vector) or (type(axis) == type([]) and len(axis) == 3))
        if type(axis) == type([]):
            axis = Vector.fromList(axis)

        axis.normalize()
        a = math.cos(angle_rad / 2.0)
        b, c, d = -axis * math.sin(angle_rad / 2.0)
        aa, bb, cc, dd = a * a, b * b, c * c, d * d
        bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
        return Matrix(
                [[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac), 0],
                [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab), 0],
                [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc, 0],
                [0,0,0,1]
                ])

    def isClose(self, other, rel_tol=1e-09, abs_tol=0.0):
        res = True
        for i in range(4):
            for j in range(4):
                res &= math.isclose(self.data[i][j], other.data[i][j], rel_tol=rel_tol, abs_tol=abs_tol)
        return res

    def __str__(self):
        return str(self.data)

    def basis_description(self):
        return f'{self}\napplied to [1,0,0]: {self@Vector.fromList([1,0,0])}'

    def __matmul__(self, o):
        if (type(o) == Matrix):
            r = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        r[i][j] += self.data[i][k] * o.data[k][j]
            return Matrix(r)
        elif (type(o) == Vector):
            res = Vector()
            w = o.x * self.data[3][0] + o.y * self.data[3][1] + o.z * self.data[3][2] + self.data[3][3]
            res.x = (o.x * self.data[0][0] + o.y * self.data[0][1] + o.z * self.data[0][2] + self.data[0][3]) / w
            res.y = (o.x * self.data[1][0] + o.y * self.data[1][1] + o.z * self.data[1][2] + self.data[1][3]) / w
            res.z = (o.x * self.data[2][0] + o.y * self.data[2][1] + o.z * self.data[2][2] + self.data[2][3]) / w
            return res
        else:
            assert(False)
