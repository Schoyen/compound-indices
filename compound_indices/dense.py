import math


def inds_to_comp(indices, L):
    N = len(indices)

    comp = 0

    for i in range(N):
        comp += indices[i] * L ** (N - i - 1)

    return comp


def comp_to_inds(I, L, N):
    indices = [0] * N

    for i in range(N - 1):
        indices[i] = (I // (L ** (N - i - 1))) % L

    indices[-1] = I % L

    return indices


def inds_to_comp_as(indices, L):
    N = len(indices)
    assert len(L) == N

    comp = 0

    for i in range(N):
        val = indices[i] * math.prod(L[i + 1 :])
        comp += val

    return comp


def comp_to_inds_as(I, L, N):
    indices = [0] * N
    assert len(L) == N

    for i in range(N - 1):
        indices[i] = (I // math.prod(L[i + 1 :])) % L[i]

    indices[-1] = I % L[-1]

    return indices
