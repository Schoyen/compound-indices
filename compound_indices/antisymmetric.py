import math


def inds_to_comp(ind, L):
    # Assuming sorted indces as ind[0] < ind[1] < ... < ind[L]
    I = 0

    for k in range(1, len(ind) + 1):
        I += math.comb(ind[k - 1], k)

    return I


def J(inds, N, L):
    # Solution from PHYSICAL REVIEW A 81, 022124 (2010)
    # This solution counts the number of holes, i.e., non-occupied states.
    M = L - N
    comp = 1
    for k in range(M):
        comp += comb(N + M - inds[k], M - k)
    return comp


# def pascal_shells(num_shells, N, i):
#     if i == 0:
#         return 0
#
#     num_ahead = 0
#
#     for _i in range(i):
#         num_ahead += math.comb(num_shells - _i, N - 1)
#
#     return num_ahead
#
#
# def inds_to_comp(indices, L):
#     N = len(indices)
#
#     assert 0 < N <= L
#
#     if N == 1:
#         return indices[0]
#
#     # Total number of shells
#     num_shells = L - 1
#     # Fetch the current shell
#     i = indices[0]
#     # Calculate how many indices are ahead of the current shell
#     num_ahead = pascal_shells(num_shells, N, i)
#
#     # The amount to subtract from each index and L
#     sub = i + 1
#
#     return num_ahead + inds_to_comp(
#         [ind - sub for ind in indices[1:]],
#         L - sub,
#     )


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
