import numpy as np
from Gram_Schimdt import orthonormalization


def qr_decomposition(A):
    n = len(A)
    m = len(A[0])
    Q = orthonormalization(A)
    r = min(len(Q), len(Q[0]))

    R = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i, m):
            R[i, j] = np.dot(A[:, j], Q[:, i])
    return Q, R


def qr_factorization(A):
   #source: http://mlwiki.org/index.php/Gram-Schmidt_Process
    # https://ichi.pro/pl/rozklad-qr-158598317599403
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j - 1):
            q = Q[:, i]
            R[i, j] = q @ v
            v = v - R[i, j] * q
        norm = np.linalg.norm(v)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R
