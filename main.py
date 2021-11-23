import numpy as np
import TriangleMatrix as TrM
import Plots as P
import CalcDet as Det


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
    b = np.array([[1, 2, 3, 4]])

    # print(np.linalg.solve(B, b.T))
    # B = np.concatenate((B, b.T), axis=1)
    # B_upper = TrM.upper_matrix(B.copy())
    # print(TrM.solve_upper(B_upper))

    # print(TrM.lower_matrix(B))
    # P.plot_laplace_leibniz_comp(wym=9)
