import math


def inds_to_comp(indices, L):
    N = len(indices)

    # Check if L is an iterable
    try:
        _ = iter(L)
    except TypeError:
        # Make L into an iterable
        L = [L] * N

    assert len(L) == N

    comp = 0

    for i in range(N):
        val = indices[i] * math.prod(L[i + 1 :])
        comp += val

    return comp


def comp_to_inds(I, L, N):
    indices = [0] * N

    # Check if L is an iterable
    try:
        _ = iter(L)
    except TypeError:
        # Make L into an iterable
        L = [L] * N

    assert len(L) == N

    for i in range(N - 1):
        indices[i] = (I // math.prod(L[i + 1 :])) % L[i]

    indices[-1] = I % L[-1]

    return indices
