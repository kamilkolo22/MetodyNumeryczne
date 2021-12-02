import numpy as np


def upper_matrix(A):
    A = A.astype(float)
    for k in range(len(A)-1):
        for i in range(k, len(A)-1):
            if A[k][k] == 0:
                swap_rows(A, k)
            w = A[i+1][k] / A[k][k]
            A[i+1] = A[i+1] - A[k]*w
    return A


def swap_rows(A, k):
    for n in range(k+1, len(A)):
        if A[n][k] != 0:
            A[[k, n]] = A[[n, k]]
            break


def solve_upper(A):
    if (len(A) + 1) == len(A[0]):
        A, b = np.hsplit(A, [len(A)])
    else:
        raise ValueError('Macierz A ma błędne wymiary')
    n = len(A)
    x = [0. for x in range(len(A))]
    for k in range(1, len(A)+1):
        sum_k = sum([A[n - k][n-k+i]*x[n-k+i] for i in range(k)])
        x[n-k] = float((b[n-k] - sum_k) / A[n-k][n-k])
    return x


def lower_matrix(A):
    A = A.astype(float)
    for k in range(len(A)-1, -1, -1):
        for i in range(k, 0, -1):
            if A[k][k] == 0:
                swap_rows_up(A, k)
            w = A[i-1][k] / A[k][k]
            A[i-1] = A[i-1] - A[k]*w
    return A


def swap_rows_up(A, k):
    for n in range(k):
        if A[n][k] != 0:
            A[[k, n]] = A[[n, k]]
            break


def solve_lower(A):
    if (len(A) + 1) == len(A[0]):
        A, b = np.hsplit(A, [len(A)])
    else:
        raise ValueError('Macierz A ma błędne wymiary')
    n = len(A)
    x = [0. for x in range(len(A))]
    for k in range(len(A)):
        sum_k = sum([A[k][i] * x[i] for i in range(k)])
        x[k] = float((b[k] - sum_k) / A[k][k])
    return x


def LU_decomposition(A):
    U = A.copy().astype(float)
    L = np.identity(len(A))

    for k in range(len(U) - 1):
        for i in range(k, len(U) - 1):
            if U[k][k] == 0:
                raise ValueError('Macierzy nie mozna rozlozyc do postaci LU')
            w = U[i + 1][k] / U[k][k]
            L[i+1][k] = w
            U[i + 1] = U[i + 1] - U[k] * w
    return L, U
