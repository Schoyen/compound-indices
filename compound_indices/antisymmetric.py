import math


def pascal_shells(num_shells, N, i):
    if i == 0:
        return 0

    num_ahead = 0

    for _i in range(i):
        num_ahead += math.comb(num_shells - _i, N - 1)

    return num_ahead


def inds_to_comp_sq(indices, L):
    N = len(indices)

    assert 0 < N <= L

    if N == 1:
        return indices[0]

    # Total number of shells
    num_shells = L - 1
    # Fetch the current shell
    i = indices[0]
    # Calculate how many indices are ahead of the current shell
    # This should be *something-something-Pascal's-triangle*
    num_ahead = pascal_shells(num_shells, N, i)

    # The amount to subtract from each index and L
    sub = i + 1

    return num_ahead + inds_to_comp_sq(
        [ind - sub for ind in indices[1:]],
        L - sub,
    )
