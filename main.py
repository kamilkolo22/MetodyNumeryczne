import numpy as np


def generate_permutations(n):
    lista = [[x] for x in range(1, n+1)]
    for i in range(1, n+1):
        for l in lista:
            l.append(i)
    return lista


def leibniz_formula(A):
    pass


if __name__ == '__main__':
    m = np.array([[1, 5, 2],
                 [4, 6, 13],
                 [4, 7, 9]])
    print(np.linalg.det(m))

    print(generate_permutations(5))
