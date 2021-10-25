def permutation_sign(list):
    wages = []
    for n in list:
        wages.append(sum([n > x for x in list[list.index(n):]]))
    return (-1)**sum(wages)


def permutation_sign2(list):
    used = []
    cycles = []
    for n in list:
        if n not in used:
            cycle = get_cycle(list, list.index(n))
            used += cycle
            cycles.append(len(cycle)-1)
    return (-1)**sum(cycles)


def get_cycle(list, pointer):
    if (pointer + 1) == list[pointer]:
        return [pointer + 1]
    else:
        cycle = [pointer + 1]
        start = pointer + 1
        pointer = list[pointer] - 1

    while True:
        if pointer + 1 == start:
            return cycle
        else:
            cycle.append(pointer+1)
            pointer = list[pointer] - 1
