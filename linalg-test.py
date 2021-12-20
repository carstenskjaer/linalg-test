import numpy as np

from matrix import Matrix
from vector import Vector

if __name__ == "__main__":
    '''
    m3 = Matrix.fromTranslation([1,-1,0])
    print(f'Matrix.fromTranslation([1,-1,0] = \n{m3}')

    v1 = Vector.fromList([1,0,-1])
    print(f'Vector.fromList([1,0,-1]) = {v1}')

    print(f'{Matrix()} @ {v1} = {Matrix()@v1}')

    m4 = Matrix.fromAxisAngle([1,0,0], np.deg2rad(90))
    print(f'Matrix.fromAxisAngle([1,0,0], np.deg2rad(90)) = \n{m4.basis_description()}')

    m4 = Matrix.fromAxisAngle([0,1,0], np.deg2rad(90))
    print(f'Matrix.fromAxisAngle([0,1,0], np.deg2rad(90)) = \n{m4.basis_description()}')

    m4 = Matrix.fromAxisAngle([0,0,1], np.deg2rad(90))
    print(f'Matrix.fromAxisAngle([0,0,1], np.deg2rad(90)) = \n{m4.basis_description()}')
    '''
    m1 = Matrix.fromAxisAngle([0,1,0], np.deg2rad(90))
    m2 = Matrix.fromTranslation([1,0,0])

    print(f'rot @ trans: \n{(m1@m2).basis_description()}')
    print(f'trans @ rot: \n{(m2@m1).basis_description()}')
    pass
