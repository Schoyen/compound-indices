import math


def inds_to_comp(indices, L):
    # Modified solution from PHYSICAL REVIEW A 81, 022124 (2010)
    # Assuming sorted indces as indices[0] < indices[1] < ... < indices[L]

    N = len(indices)
    assert N <= L

    M = L - N

    comp = 0

    for k in range(1, N + 1):
        comp += math.comb(L - (indices[k - 1] + 1), N + 1 - k)

    return math.comb(L, M) - 1 - comp


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


def comp_to_inds(I, L, N):
    assert 0 < N <= L

    if N == 1:
        return [I]

    if I == 0:
        return [i for i in range(N)]

    current_shell = math.comb(L, N)

    if I == current_shell - 1:
        return [L - N + i for i in range(N)]

    previous_shell = math.comb(L - 1, N)

    num_ahead = current_shell - previous_shell
    num_behind = 0

    for i in range(2, L):
        if num_behind <= I < num_ahead:
            indices = [i - 2] + [
                j + i - 1
                for j in comp_to_inds(I - num_behind, L - i + 1, N - 1)
            ]
            return indices

        current_shell = previous_shell
        previous_shell = math.comb(L - i, N)
        num_behind = num_ahead
        num_ahead += current_shell - previous_shell

    assert False, "You should not be here (☉_☉)"
