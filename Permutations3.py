def generate_permutations(n):
    lista = [[x] for x in range(1, n+1)]
    for t in range(n-1):
        lista = [[*x, i] for x in lista
                 for i in range(1, n+1) if i not in x]
    return lista
