import numpy as np


def add_number(lista, n):
    temp = []
    for i in range(1, n+1):
        if i not in lista:
            lista_temp = lista.copy()
            lista_temp.append(i)
            temp.append(lista_temp)
    return temp


def generate_permutations(n):
    lista = [[x] for x in range(1, n+1)]

    for t in range(n-1):
        temp = []
        for x in lista:
            temp = temp + add_number(x, n)
        lista = temp.copy()

    return lista


def leibniz_formula(A):
    pass


if __name__ == '__main__':
    m = np.array([[1, 5, 2],
                 [4, 6, 13],
                 [4, 7, 9]])
    print(np.linalg.det(m))

    print(generate_permutations(3))
