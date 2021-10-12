def add_number(lista, k):
    temp = []
    for i in range(0, len(lista)+1):
        t = lista.copy()
        t.insert(i, k)
        temp.append(t)
    return temp


def generate_permutations(n):
    lista = [[1]]
    for i in range(2, n+1):
        temp = []
        for t in lista:
            temp += add_number(t, i)
        lista = temp.copy()

    return lista