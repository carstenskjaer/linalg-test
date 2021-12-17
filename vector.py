import numpy as np

class Vector:
    ndarray = np.zeros((3,))

    def fromList(list):
        assert type(list) == type([]) and len(list) == 3
        m = Vector()
        m.ndarray = np.array(list)
        return m

    def fromNdArray(ndarray):
        assert type(ndarray) == np.ndarray and ndarray.shape == (3,)
        v = Vector()
        v.ndarray = ndarray.copy()
        return v

    def __str__(self):
        return str(self.ndarray)

