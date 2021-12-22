from matrix import Matrix

class Frame:
    parent = None
    localMatrix = Matrix()
    name = ''

    def getGlobalMatrix(self):
        if (self.parent != None):
            return self.parent.getGlobalMatrix() @ self.localMatrix
        return self.localMatrix




