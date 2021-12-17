import numpy as np

from matrix import Matrix
from vector import Vector


    
if __name__ == "__main__":
    m1 = Matrix()
    m2 = Matrix()
    print(f'{m1} @ \n{m2} = \n{m1@m2}')

    m3 = Matrix.fromTranslation([1,-1,0])
    print(f'Matrix.fromTranslation([1,-1,0] = \n{m3}')

    v1 = Vector.fromList([1,0,-1])
    print(f'Vector.fromList([1,0,-1]) = {v1}')

    print(f'{m1} @ {v1} = {m1@v1}')

    m4 = Matrix.fromAxisAngle([1,0,0], np.deg2rad(90))
    print(m4.basis_description())
