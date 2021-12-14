import numpy as np
from TriangleMatrix import swap_rows


def matrix_rank(A):
    A = A.astype(float)
    for k in range(len(A) - 1):
        print(A)
        for i in range(k, len(A) - 1):
            if A[k][k] == 0:
                if not swap_rows(A, k):
                    continue
            w = A[i + 1][k] / A[k][k]
            A[i + 1] = np.around(A[i + 1] - A[k] * w, 10)
    rank = 0
    for k in range(len(A)):
        if np.any(A[k]):
            rank += 1
    return rank
