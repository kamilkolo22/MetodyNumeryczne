import numpy as np


def cholesky_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))

    for j in range(n):
        for i in range(j, n):
            if i == j:
                if i != 0:
                    L[i][j] = (A[i][i] - sum([L[i][k]**2 for k in range(j)]))**0.5
                else:
                    L[i][j] = (A[i][i]) ** 0.5
            else:
                L[i][j] = (A[i][j] - sum([L[i][k]*L[j][k] for k in range(j)])) / L[j][j]
    return L
