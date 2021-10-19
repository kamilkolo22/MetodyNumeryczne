import Permutations as Per
import PermutaionSign as Sig



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

