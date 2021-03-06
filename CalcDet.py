import Permutations as Per
import PermutaionSign as Sig
import numpy as np
from TriangleMatrix import swap_rows


def det_leibniz_formula(A):
    if not len(A) == len(A[0]):
        print("wrong matrix dimensions")
    perm = Per.generate_permutations1(len(A))
    summ = 0
    for p in perm:
        sign = Sig.permutation_sign(p)
        product = 1
        for k in p:
            product *= A[p.index(k), k-1]
        summ += product * sign
    return summ


def det_leibniz_formula2(A):
    if not len(A) == len(A[0]):
        print("wrong matrix dimensions")
    perm = Per.generate_permutations2(len(A))
    summ = 0
    for p in perm:
        sign = Sig.permutation_sign(p)
        product = 1
        for k in p:
            product *= A[p.index(k), k-1]
        summ += product * sign
    return summ


def det_leibniz_formula3(A):
    if not len(A) == len(A[0]):
        print("wrong matrix dimensions")
    perm = Per.generate_permutations3(len(A))
    summ = 0
    for p in perm:
        sign = Sig.permutation_sign(p)
        product = 1
        for k in p:
            product *= A[p.index(k), k-1]
        summ += product * sign
    return summ


def det_laplace_formula(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        summ = 0
        for i in range(n):
            B = np.delete(A, 0, axis=1)
            B = np.delete(B, i, axis=0)
            summ += (-1)**i * A[i][0] * det_laplace_formula(B)
        return summ

def det_laplace_formula_fast(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        summ = 0
        for i in range(n):
            B = np.concatenate((A[0:i, 1:], A[i + 1:len(A), 1:]), axis=0)
            summ += (-1)**i * A[i][0] * det_laplace_formula_fast(B)
        return summ


def det_gauss_elimination(A):
    A = A.astype(float)
    swap_number = 0
    for k in range(len(A)-1):
        for i in range(k, len(A)-1):
            if A[k][k] == 0:
                swap_rows(A, k)
                swap_number += 1
            w = A[i+1][k] / A[k][k]
            A[i+1] = A[i+1] - A[k]*w
    det = np.prod([A[k][k] for k in range(len(A))]) * (-1)**swap_number
    return det
