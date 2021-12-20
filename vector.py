import math

class Vector:
    x = 0
    y = 0
    z = 0

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def fromList(list):
        assert type(list) == type([]) and len(list) == 3
        return Vector(list[0], list[1], list[2])

    def __getitem__(self, index):
        assert(index >= 0 and index <= 2)
        return self.x if index == 0 else (self.y if index == 1 else self.z)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __mul__(self, f):
        if isinstance(f, Vector):
            return Vector(self.x*f.x, self.y*f.y, self.z*f.z)
        else:
            return Vector(self.x*f, self.y*f, self.z*f)
    
    def __add__(self, f):
        if isinstance(f, Vector):
            return Vector(self.x+f.x, self.y+f.y, self.z+f.z)
        else:
            return Vector(self.x+f, self.y+f, self.z+f)
    
    def __sub__(self, f):
        if isinstance(f, Vector):
            return Vector(self.x-f.x, self.y-f.y, self.z-f.z)
        else:
            return Vector(self.x-f, self.y-f, self.z-f)

    def __iadd__(self, f):
        if isinstance(f, Vector):
            self.x += f.x
            self.y += f.y
            self.z += f.z
        else:
            self.x += f
            self.y += f
            self.z += f
        return self

    def __isub__(self, f):
        if isinstance(f, Vector):
            self.x -= f.x
            self.y -= f.y
            self.z -= f.z
        else:
            self.x -= f
            self.y -= f
            self.z -= f
        return self

    def __imul__(self, f):
        if isinstance(f, Vector):
            self.x *= f.x
            self.y *= f.y
            self.z *= f.z
        else:
            self.x *= f
            self.y *= f
            self.z *= f
        return self

    def cross(self, other):
        return Vector(self.y*other.z-other.y*self.z, self.z*other.x-other.z*self.x, self.x*other.y-other.x*self.y)

    def __str__(self):
        return f'[{self.x:10.7f}, {self.y:10.7f}, {self.z:10.7f}]'

    def isClose(self, other, rel_tol=1e-09, abs_tol=0.0):
        return \
            math.isclose(self.x, other.x, rel_tol=rel_tol, abs_tol=abs_tol) and \
            math.isclose(self.y, other.y, rel_tol=rel_tol, abs_tol=abs_tol) and \
            math.isclose(self.z, other.z, rel_tol=rel_tol, abs_tol=abs_tol)

    def length(self):
        return math.sqrt(self[0]**2 + self[1]**2 + self[2]**2)

    def normalize(self):
        l = self.length()
        self.x /= l
        self.y /= l
        self.z /= l
        return self

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


