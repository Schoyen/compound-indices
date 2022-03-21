def inds_to_comp_sq(indices, L):
    N = len(indices)

    comp = 0

    for i in range(N):
        comp += indices[i] * L ** (N - i - 1)

    return comp


def comp_to_inds_sq(I, L, N):
    indices = [0] * N

    for i in range(N - 1):
        indices[i] = (I // (L ** (N - i - 1))) % L

    indices[-1] = I % L

    return indices
