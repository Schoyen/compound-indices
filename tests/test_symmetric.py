import math

from compound_indices.symmetric import inds_to_comp

from helpers.utils import ind_gen


def test_single_to_comp():
    L = 5
    counter = 0

    for i in range(L):
        comp = inds_to_comp([i], L)
        # inds = comp_to_inds(comp, L, 1)
        # assert inds == [i]
        assert counter == comp
        counter += 1

    assert counter == math.comb(L, 1)


def test_pair_to_comp():
    L = 6
    counter = 0

    for i in range(L):
        for j in range(i, L):
            comp = inds_to_comp([i, j], L)
            # inds = comp_to_inds(comp, L, 2)
            # assert inds == [i, j]
            assert counter == comp
            counter += 1

    assert counter == math.comb(L + 1, 2)


def test_triple_to_comp():
    L = 7
    L = 5
    counter = 0

    for i in range(L):
        for j in range(i, L):
            for k in range(j, L):
                comp = inds_to_comp([i, j, k], L)
                # inds = comp_to_inds(comp, L, 3)
                # assert inds == [i, j, k]
                print([i, j, k])
                assert counter == comp
                counter += 1

    assert counter == math.comb(L + 2, 3)


def test_many_to_comp():
    L = 8

    for N in range(1, L + 1):
        for counter, inds in enumerate(ind_gen(0, L, N, kind="s")):
            comp = inds_to_comp(inds, L)
            # c_inds = comp_to_inds(comp, L, N)
            # assert inds == c_inds
            assert counter == comp

        # Counter does not count the final step (as in the manual loops)
        assert counter == (math.comb(L + N - 1, N) - 1)
