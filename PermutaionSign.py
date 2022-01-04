def permutation_sign(plist):
    wages = []
    for n in plist:
        wages.append(sum([n > x for x in plist[plist.index(n):]]))
    return (-1)**sum(wages)


def permutation_sign2(plist):
    used = []
    cycles = []
    for n in plist:
        if n not in used:
            cycle = get_cycle(plist, plist.index(n))
            used += cycle
            cycles.append(len(cycle)-1)
    return (-1)**sum(cycles)


def get_cycle(plist, pointer):
    if (pointer + 1) == plist[pointer]:
        return [pointer + 1]
    else:
        cycle = [pointer + 1]
        start = pointer + 1
        pointer = plist[pointer] - 1

    while True:
        if pointer + 1 == start:
            return cycle
        else:
            cycle.append(pointer+1)
            pointer = plist[pointer] - 1
