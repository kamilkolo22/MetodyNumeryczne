def generate_permutations(n):
    lista = [[1]]
    for num in range(2, n+1):
        lista = [l[:j] + [num] + l[j:] for l in lista
                 for j in range(len(l) + 1)]
    return lista
