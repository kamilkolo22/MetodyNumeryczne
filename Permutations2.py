def swap_elements(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
    return lista


def generate_permutations(n):
    lista = [[x for x in range(1, n+1)]]
    for i in range(n-1):
        lista = [swap_elements(l.copy(), i, j) for l in lista
                 for j in range(i, n)]
    return lista
