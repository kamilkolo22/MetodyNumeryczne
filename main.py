import numpy as np
import TriangleMatrix as TrM



if __name__ == '__main__':
    A = np.array([[1, 5, 2],
                  [4, 6, 13],
                  [4, 7, 9]])

    print(TrM.upper_matrix(A.copy()))

