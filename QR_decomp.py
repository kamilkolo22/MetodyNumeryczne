import numpy as np
from Gram_Schimdt import orthonormalization


def qr_decomposition(A):
    n = len(A)
    Q = orthonormalization(A)
    R = np.zeros((n, n), dtype=float)

    for i in range(n):
        for j in range(n):
            R[i][j] = np.dot(A[:][j], Q[:][i])
    return Q, R
