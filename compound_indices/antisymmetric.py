import math


def inds_to_comp(indices, L):
    # Modified solution from PHYSICAL REVIEW A 81, 022124 (2010)
    # Assuming sorted indices as indices[0] < indices[1] < ... < indices[L]

    N = len(indices)
    assert N <= L

    M = L - N

    comp = 0

    for k in range(N):
        comp += math.comb(L - (indices[k] + 1), N - k)

    return math.comb(L, M) - 1 - comp


def comp_to_inds(comp, L, N):
    indices = [0] * N
    x = 1
    for i in range(1, N + 1):
        while comp >= math.comb(L - x, N - i):
            comp -= math.comb(L - x, N - i)
            x += 1

        indices[i - 1] = x - 1
        x += 1

    return indices


def sign_of_inds(indices):
    N = len(indices)
    sign = 1
    prev_value = -1

    for i in range(N):
        index_min = min(range(len(indices)), key=indices.__getitem__)

        # Two or more equal values
        if indices[index_min] == prev_value:
            return 0

        prev_value = indices[index_min]
        sign *= (-1) ** index_min
        indices = indices[:index_min] + indices[index_min + 1 :]

    return sign
