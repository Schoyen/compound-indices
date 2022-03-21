import math

from compound_indices.antisymmetric import inds_to_comp


def test_single_to_comp():
    L = 5
    counter = 0

    for i in range(L):
        comp = inds_to_comp([i], L)
        assert counter == comp
        counter += 1

    assert counter == math.comb(L, 1)


def test_pair_to_comp():
    L = 6
    counter = 0

    for i in range(L):
        for j in range(i + 1, L):
            comp = inds_to_comp([i, j], L)
            assert counter == comp
            counter += 1

    assert counter == math.comb(L, 2)


def test_triple_to_comp():
    L = 7
    counter = 0

    for i in range(L):
        for j in range(i + 1, L):
            for k in range(j + 1, L):
                comp = inds_to_comp([i, j, k], L)
                assert counter == comp
                counter += 1

    assert counter == math.comb(L, 3)


def test_quad_to_comp():
    L = 8
    counter = 0

    for i in range(L):
        for j in range(i + 1, L):
            for k in range(j + 1, L):
                for l in range(k + 1, L):
                    comp = inds_to_comp([i, j, k, l], L)
                    # print(counter, (i, j, k), comp)
                    assert counter == comp
                    counter += 1

    assert counter == math.comb(L, 4)


def test_5_to_comp():
    L = 9
    counter = 0

    for i in range(L):
        for j in range(i + 1, L):
            for k in range(j + 1, L):
                for l in range(k + 1, L):
                    for p in range(l + 1, L):
                        comp = inds_to_comp([i, j, k, l, p], L)
                        # print(counter, (i, j, k), comp)
                        assert counter == comp
                        counter += 1

    assert counter == math.comb(L, 5)


def test_6_to_comp():
    L = 11
    counter = 0

    for i in range(L):
        for j in range(i + 1, L):
            for k in range(j + 1, L):
                for l in range(k + 1, L):
                    for p in range(l + 1, L):
                        for q in range(p + 1, L):
                            comp = inds_to_comp([i, j, k, l, p, q], L)
                            # print(counter, (i, j, k), comp)
                            assert counter == comp
                            counter += 1

    assert counter == math.comb(L, 6)
