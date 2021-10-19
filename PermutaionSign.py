def permutation_sign(list):
    wages = []
    for n in list:
        wages.append(sum([n > x for x in list[list.index(n):]]))
    return (-1)**sum(wages)


def permutation_sign2(list):
    index = [list.index(x)+1 for x in list]
    cycles = []
    for n in list:
        cycle = get_cycle(list[list.index(n):], index)
        cycles.append(cycle)

    return cycles


def get_cycle(list, index, i):
    perm = []
    temp = []
    for n in range(len(list)):
        if not i == list[index.index(i)]:
            perm += [i, index.index(i)]
    return perm
