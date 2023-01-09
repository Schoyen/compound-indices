import math

from compound_indices.dense import (
    inds_to_comp,
    comp_to_inds,
)


def test_single_sq():
    L = 5
    counter = 0

    for i in range(L):
        comp = inds_to_comp((i,), L)
        assert comp == counter
        inds = comp_to_inds(comp, L, 1)
        assert inds == [i]
        counter += 1

    assert counter == L


def test_single_as():
    L = [5]
    counter = 0

    for i in range(L[0]):
        comp = inds_to_comp((i,), L)
        assert comp == counter
        inds = comp_to_inds(comp, L, 1)
        assert inds == [i]
        counter += 1

    assert counter == math.prod(L)


def test_pair_sq():
    L = 5
    counter = 0

    for i in range(L):
        for j in range(L):
            comp = inds_to_comp((i, j), L)
            assert comp == counter
            inds = comp_to_inds(comp, L, 2)
            assert inds == [i, j]
            counter += 1

    assert counter == L**2


def test_pair_as():
    L = [5, 6]
    counter = 0

    for i in range(L[0]):
        for j in range(L[1]):
            comp = inds_to_comp((i, j), L)
            assert comp == counter
            inds = comp_to_inds(comp, L, 2)
            assert inds == [i, j]
            counter += 1

    assert counter == math.prod(L)


def test_triple_sq():
    L = 6
    counter = 0

    for i in range(L):
        for j in range(L):
            for k in range(L):
                comp = inds_to_comp((i, j, k), L)
                assert comp == counter
                inds = comp_to_inds(comp, L, 3)
                assert inds == [i, j, k]
                counter += 1

    assert counter == L**3


def test_triple_as():
    L = [6, 3, 7]
    counter = 0

    for i in range(L[0]):
        for j in range(L[1]):
            for k in range(L[2]):
                comp = inds_to_comp((i, j, k), L)
                assert comp == counter
                inds = comp_to_inds(comp, L, 3)
                assert inds == [i, j, k]
                counter += 1

    assert counter == math.prod(L)


def test_quad_sq():
    L = 7
    counter = 0

    for i in range(L):
        for j in range(L):
            for k in range(L):
                for l in range(L):
                    comp = inds_to_comp((i, j, k, l), L)
                    assert comp == counter
                    inds = comp_to_inds(comp, L, 4)
                    assert inds == [i, j, k, l]
                    counter += 1

    assert counter == L**4


def test_quad_sq():
    L = [7, 7, 10, 3]
    counter = 0

    for i in range(L[0]):
        for j in range(L[1]):
            for k in range(L[2]):
                for l in range(L[3]):
                    comp = inds_to_comp((i, j, k, l), L)
                    assert comp == counter
                    inds = comp_to_inds(comp, L, 4)
                    assert inds == [i, j, k, l]
                    counter += 1

    assert counter == math.prod(L)
