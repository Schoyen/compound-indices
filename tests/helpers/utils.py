def ind_gen(start, n, k, kind="d"):
    assert kind in ["d", "a", "s"]
    assert start >= 0
    assert n >= k
    assert k > 0

    if k == 1:
        for i in range(start, n):
            yield [i]
        return

    for i in range(start, n):
        start_der = 0

        if kind == "a":
            start_der = i + 1
        elif kind == "s":
            start_der = i

        for s_ind in ind_gen(start_der, n, k - 1, kind=kind):
            yield [i] + s_ind


if __name__ == "__main__":
    for i in ind_gen(0, 5, 1):
        print(i)

    for i in ind_gen(0, 5, 2, kind="a"):
        print(i)

    for i in ind_gen(0, 5, 3, kind="a"):
        print(i)

    for i in ind_gen(0, 6, 3, kind="a"):
        print(i)
