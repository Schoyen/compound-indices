import math

# from compound_indices.antisymmetric import pascal_shells


def gen_gauss_sum(start, stop):
    return (stop - start + 1) * (stop - start + 2) / 2 + (start - 1) * (
        stop - start + 1
    )


def inds_to_comp(indices, L):
    N = len(indices)

    assert 0 < N <= L

    if N == 1:
        return indices[0]

    # Total number of shells
    num_shells = L
    # Fetch the current shell
    i = indices[0]

    if i == L - 1:
        return math.comb(L + N - 1, N) - 1

    # Calculate how many indices are ahead of the current shell
    # num_ahead = pascal_shells(num_shells, N, i)
    num_ahead = 0

    if i > 0:
        if len(indices) > 2:
            print(L, N, i)
            print(math.comb(L + N - 1, N - 1))
            print(math.comb(L + N - 2, N - 1))
            print(math.comb(L + N - 1 - i, N - 1))
            print("BLEH")
        num_ahead = sum(math.comb(L + 1 - _i, N - 1) - 1 for _i in range(i))
    print(num_ahead)

    # The amount to subtract from each index and L
    # sub = (i + 1 if i < indices[1] and len(indices[1:]) > 1 else i)
    sub = i

    return num_ahead + inds_to_comp(
        [ind - sub for ind in indices[1:]],
        L - sub,
    )


if __name__ == "__main__":
    import math

    L = 5
    shell_counter = 0
    prev_shell = 0
    counter = 0

    for i in range(L):
        print(L * (L - i + 1) - gen_gauss_sum(i, L - 1))
        print(f"Num above this shell: {shell_counter}")
        print(f"Shell difference: {shell_counter - prev_shell}")
        for j in range(i, L):
            print(f"({i}, {j}) -> {counter}")
            counter += 1

        prev_shell = shell_counter
        shell_counter += L - i

    print(gen_gauss_sum(i, L))
    print(f"Num above this shell: {shell_counter}")
    print(f"Shell difference: {shell_counter - prev_shell}")

    wat
    counter = 0
    shell_counter = 0
    prev_shell = 0

    for i in range(L):
        print(f"Num above this shell: {shell_counter}")
        print(f"Shell difference: {shell_counter - prev_shell}")
        for j in range(i, L):
            for k in range(j, L):
                print(f"({i}, {j}, {k}) -> {counter}")
                counter += 1

        prev_shell = shell_counter
        shell_counter += sum(L - j for j in range(i, L))

    wat
    counter = 0

    for i in range(L):
        for j in range(i, L):
            for k in range(j, L):
                for l in range(k, L):
                    print(f"({i}, {j}, {k}, {l}) -> {counter}")
                    counter += 1
