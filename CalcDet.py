import Permutations as Per
import PermutaionSign as Sig
import numpy as np



def det_leibniz_formula(A):
    if not len(A) == len(A[0]):
        print("wrong matrix dimensions")
    perm = Per.generate_permutations1(len(A))
    sum = 0
    for p in perm:
        sign = Sig.permutation_sign(p)
        product = 1
        for k in p:
            product *= A[p.index(k), k-1]
        sum += product * sign
    return sum


def det_laplace_formula(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        sum = 0
        for i in range(n):
            B = np.delete(A, 0, axis=1)
            B = np.delete(B, i, axis=0)
            sum += (-1)**(2+i) * A[i][0] * det_laplace_formula(B)
        return sum
