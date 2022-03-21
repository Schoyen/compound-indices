from compound_indices.dense import inds_to_comp_sq, comp_to_inds_sq


def test_pair_sq():
    L = 5
    counter = 0

    for i in range(L):
        for j in range(L):
            comp = inds_to_comp_sq((i, j), L)
            assert comp == counter
            inds = comp_to_inds_sq(comp, L, 2)
            assert inds == [i, j]
            counter += 1

    assert counter == L**2


def test_triple_sq():
    L = 6
    counter = 0

    for i in range(L):
        for j in range(L):
            for k in range(L):
                comp = inds_to_comp_sq((i, j, k), L)
                assert comp == counter
                inds = comp_to_inds_sq(comp, L, 3)
                assert inds == [i, j, k]
                counter += 1

    assert counter == L**3


def test_quad_sq():
    L = 7
    counter = 0

    for i in range(L):
        for j in range(L):
            for k in range(L):
                for l in range(L):
                    comp = inds_to_comp_sq((i, j, k, l), L)
                    assert comp == counter
                    inds = comp_to_inds_sq(comp, L, 4)
                    assert inds == [i, j, k, l]
                    counter += 1

    assert counter == L**4
