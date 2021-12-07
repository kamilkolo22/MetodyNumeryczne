import numpy as np
from TriangleMatrix import swap_rows


def matrix_rank(A):
    A = A.astype(float)
    rank = 1
    for k in range(len(A) - 1):
        for i in range(k, len(A) - 1):
            if A[k][k] == 0:
                swap_rows(A, k)
            w = A[i + 1][k] / A[k][k]
            A[i + 1] = np.around(A[i + 1] - A[k] * w, 10)
        if np.any(A[k+1]):
            rank += 1
    return rank
