import numpy as np
import TriangleMatrix as TrM
import Plots as P
import CalcDet as Det
import Cholesky as Ch


if __name__ == '__main__':
    A = np.array([[1, 5, 2],
                  [4, 6, 13],
                  [4, 7, 9]])
    B = np.array([[-1, 5, 2, 3],
                  [4, 6, 13, 4],
                  [4, 7, 9, 5],
                  [1, 2, 3, 4]])
    C = np.array([[1, 1, 1],
                  [1, 1, 3],
                  [7, 5, 4]])
    D = np.array([[3, 2],
                  [1, 4]])
    b = np.array([[1, 2, 3, 4]])

    # print(np.linalg.solve(B, b.T))
    # B = np.concatenate((B, b.T), axis=1)
    # B_lower = TrM.lower_matrix(B.copy())
    # print(B_lower)
    # print(TrM.solve_lower(B_lower))

    # dec_LU = TrM.LU_decomposition(B)
    # print(dec_LU[0])
    # print(dec_LU[1])
    # print(dec_LU[0] @ dec_LU[1])
    # print(B)

    L = Ch.cholesky_decomposition(D)
    print(L)
    print(L @ L.T)
    print(D)
