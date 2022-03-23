from compound_indices.antisymmetric import pascal_shells


def inds_to_comp(indices, L):
    N = len(indices)

    assert 0 < N <= L

    if N == 1:
        return indices[0]

    # Total number of shells
    num_shells = L
    # Fetch the current shell
    i = indices[0]
    # Calculate how many indices are ahead of the current shell
    num_ahead = pascal_shells(num_shells, N, i)
    print(num_ahead)

    # The amount to subtract from each index and L
    sub = i

    return num_ahead + inds_to_comp(
        [ind - sub for ind in indices[1:]],
        L - sub,
    )


if __name__ == "__main__":
    import math

    L = 5
    counter = 0

    for i in range(L):
        for j in range(i, L):
            print(f"({i}, {j}) -> {counter}")
            counter += 1

    counter = 0

    for i in range(L):
        for j in range(i, L):
            for k in range(j, L):
                print(f"({i}, {j}, {k}) -> {counter}")
                counter += 1

    counter = 0

    for i in range(L):
        for j in range(i, L):
            for k in range(j, L):
                for l in range(k, L):
                    print(f"({i}, {j}, {k}, {l}) -> {counter}")
                    counter += 1
