import numpy as np
from TriangleMatrix import swap_rows


def matrix_rank(A):
    A = A.astype(float)
    i, j = 0, 0
    while i < len(A) - 1 and j < len(A[0]) - 1:
        if A[i][j] == 0:
            if not swap_rows(A, j):
                j += 1
                continue
        for k in range(i, len(A) - 1):
            w = A[k + 1][j] / A[i][j]
            A[k + 1] = np.around(A[k + 1] - A[i] * w, 10)
        i += 1
        j += 1
    rank = 0
    for j in range(len(A)):
        if np.any(A[j]):
            rank += 1
    return rank
