import math

from compound_indices.symmetric import inds_to_comp


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


# def test_quad_to_comp():
#     L = 8
#     counter = 0
#
#     for i in range(L):
#         for j in range(i, L):
#             for k in range(j, L):
#                 for l in range(k, L):
#                     comp = inds_to_comp([i, j, k, l], L)
#                     # inds = comp_to_inds(comp, L, 4)
#                     # assert inds == [i, j, k, l]
#                     print([i, j, k, l])
#                     assert counter == comp
#                     counter += 1
#
#     assert counter == math.comb(L + 3, 4)
