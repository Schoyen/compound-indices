import math


def inds_to_comp(indices, L):
    # Modified solution from PHYSICAL REVIEW A 81, 022124 (2010)
    # Assuming sorted indices as indices[0] <= indices[1] <= ... <= indices[L]

    N = len(indices)
    assert N <= L

    occ_vec = [0] * L

    for p in indices:
        occ_vec[p] += 1

    comp = 0

    for k in range(1, L):
        comp += math.comb(N + L - 1 - k - sum(occ_vec[:k]), L - k)

    return comp
