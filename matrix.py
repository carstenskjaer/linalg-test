import numpy as np
import math
from vector import Vector

class Matrix:
    ndarray = np.eye(4, dtype=float)

    def fromNdArray(ndarray):
        assert type(ndarray) == np.ndarray and ndarray.shape == (4,4)
        m = Matrix()
        m.ndarray = ndarray.copy()
        return m

    def fromTranslation(translation):
        m = Matrix()
        m.ndarray[0:3,3] = translation
        return m

    def fromAxisAngle(axis, angle_rad):
        """
        Return the rotation matrix associated with counterclockwise rotation about
        the given axis by angle_rad radians.
        """
        assert((type(axis) == np.array and axis.shape==(3,)) or (type(axis) == type([]) and len(axis) == 3))

        axis = np.asarray(axis)
        axis = axis / math.sqrt(np.dot(axis, axis))
        a = math.cos(angle_rad / 2.0)
        b, c, d = -axis * math.sin(angle_rad / 2.0)
        aa, bb, cc, dd = a * a, b * b, c * c, d * d
        bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
        return Matrix.fromNdArray(
            np.array(
                [[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac), 0],
                [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab), 0],
                [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc, 0],
                [0,0,0,1]
                ]))

    def close(self, m):
        return np.allclose(self.ndarray, m.ndarray)

    def __str__(self):
        return str(self.ndarray)

    def description(self):
        pass

    def __matmul__(self, m):
        if (type(m) == Matrix):
            return Matrix.fromNdArray(self.ndarray@m.ndarray)
        elif (type(m) == Vector):
            return Vector.fromNdArray((self.ndarray@np.append(m.ndarray, 1))[0:3])
        else:
            assert(False)
