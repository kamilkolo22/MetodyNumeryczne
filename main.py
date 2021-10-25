import numpy as np
import CalcDet as Det
import PermutaionSign as Sig


if __name__ == '__main__':
    m = np.array([[1, 5, 2],
                 [4, 6, 13],
                 [4, 7, 9]])
    # print(np.linalg.det(m))
    #
    # print(Per1.generate_permutations(3))
    # print(len(Per1.generate_permutations(3)))
    # print(Per1.permutation_sign([3,2,1]))

    # print(Det.det_leibniz_formula(m))
    # print(Sig.permutation_sign([3,2,1]))
    print(Sig.permutation_sign2([3, 6, 4, 1, 5, 2]))
    print(Sig.permutation_sign2([2, 6, 5, 1, 3, 4]))


