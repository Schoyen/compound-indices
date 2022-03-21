import math

from compound_indices.antisymmetric import inds_to_comp, sign_of_inds


def test_levi_civita_3():
    for i in range(3):
        assert sign_of_inds([i, i, i]) == 0

        for j in range(i + 1, 3):
            assert sign_of_inds([i, i, j]) == 0
            assert sign_of_inds([i, j, i]) == 0
            assert sign_of_inds([j, i, i]) == 0
            assert sign_of_inds([i, j, j]) == 0
            assert sign_of_inds([j, j, i]) == 0
            assert sign_of_inds([j, i, j]) == 0

            for k in range(j + 1, 3):
                assert sign_of_inds([i, j, k]) == 1
                assert sign_of_inds([i, k, j]) == -1
                assert sign_of_inds([k, i, j]) == 1
                assert sign_of_inds([j, i, k]) == -1
                assert sign_of_inds([j, k, i]) == 1
                assert sign_of_inds([k, j, i]) == -1


def test_single_to_comp():
    L = 5
    counter = 0

    for i in range(L):
        comp = inds_to_comp([i], L)
        assert sign_of_inds([i]) == 1
        assert counter == comp
        counter += 1

    assert counter == math.comb(L, 1)


def test_pair_to_comp():
    L = 6
    counter = 0

    for i in range(L):
        assert sign_of_inds([i, i]) == 0
        for j in range(i + 1, L):
            comp = inds_to_comp([i, j], L)
            assert sign_of_inds([i, j]) == 1
            assert sign_of_inds([j, i]) == -1
            assert counter == comp
            counter += 1

    assert counter == math.comb(L, 2)


def test_triple_to_comp():
    L = 7
    counter = 0

    for i in range(L):
        for j in range(i + 1, L):
            assert sign_of_inds([i, j, i]) == 0
            for k in range(j + 1, L):
                comp = inds_to_comp([i, j, k], L)
                assert sign_of_inds([i, j, k]) == 1
                assert sign_of_inds([j, i, k]) == -1
                assert sign_of_inds([j, k, i]) == 1
                assert sign_of_inds([k, j, i]) == -1
                assert counter == comp
                counter += 1

    assert counter == math.comb(L, 3)


def test_quad_to_comp():
    L = 8
    counter = 0

    for i in range(L):
        for j in range(i + 1, L):
            for k in range(j + 1, L):
                assert sign_of_inds([i, j, k, j]) == 0
                for l in range(k + 1, L):
                    comp = inds_to_comp([i, j, k, l], L)
                    assert sign_of_inds([i, j, k, l]) == 1
                    assert sign_of_inds([j, i, l, k]) == 1
                    assert sign_of_inds([j, i, k, l]) == -1
                    assert sign_of_inds([i, j, l, k]) == -1
                    assert sign_of_inds([l, i, j, k]) == -1
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
                            assert counter == comp
                            counter += 1

    assert counter == math.comb(L, 6)
