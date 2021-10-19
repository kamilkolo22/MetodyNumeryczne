def generate_permutations1(n):
    lista = [[1]]
    for num in range(2, n+1):
        lista = [l[:j] + [num] + l[j:] for l in lista
                 for j in range(len(l) + 1)]
    return lista


def swap_elements(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
    return lista


def generate_permutations2(n):
    lista = [[x for x in range(1, n+1)]]
    for i in range(n-1):
        lista = [swap_elements(l.copy(), i, j) for l in lista
                 for j in range(i, n)]
    return lista


def generate_permutations3(n):
    lista = [[x] for x in range(1, n+1)]
    for t in range(n-1):
        lista = [[*x, i] for x in lista
                 for i in range(1, n+1) if i not in x]
    return lista
