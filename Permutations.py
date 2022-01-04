def generate_permutations1(n):
    plist = [[1]]
    for num in range(2, n+1):
        plist = [l[:j] + [num] + l[j:] for l in plist
                 for j in range(len(l) + 1)]
    return plist


def swap_elements(plist, pos1, pos2):
    plist[pos1], plist[pos2] = plist[pos2], plist[pos1]
    return plist


def generate_permutations2(n):
    plist = [[x for x in range(1, n+1)]]
    for i in range(n-1):
        plist = [swap_elements(l.copy(), i, j) for l in plist
                 for j in range(i, n)]
    return plist


def generate_permutations3(n):
    plist = [[x] for x in range(1, n+1)]
    for t in range(n-1):
        plist = [[*x, i] for x in plist
                 for i in range(1, n+1) if i not in x]
    return plist
