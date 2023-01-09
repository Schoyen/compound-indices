import math


def J(hole_inds, num_fermions, num_orbitals):
    assert num_fermions <= num_orbitals

    num_holes = num_orbitals - num_fermions
    assert len(hole_inds) == num_holes

    ind = 1

    for k in range(1, num_holes + 1):
        ind += math.comb(
            num_fermions + num_holes - hole_inds[k - 1], num_holes + 1 - k
        )

    # To reverse the counting order, uncomment the line below
    # return math.comb(num_orbitals, num_fermions) - ind
    return ind


def J_zero(hole_inds, num_fermions, num_orbitals):
    # Start counting from zero for both holes and the compound indices
    assert num_fermions <= num_orbitals

    num_holes = num_orbitals - num_fermions
    assert len(hole_inds) == num_holes

    ind = 0

    for k in range(1, num_holes + 1):
        ind += math.comb(
            num_fermions + num_holes - (hole_inds[k - 1] + 1), num_holes + 1 - k
        )

    # To reverse the counting order, uncomment the line below
    return math.comb(num_orbitals, num_fermions) - 1 - ind
    # return ind


def J_zero_p(particle_inds, num_fermions, num_orbitals):
    # Start counting from zero, and construct the compound indices from the set
    # particles instead of the set holes.
    assert num_fermions <= num_orbitals

    num_holes = num_orbitals - num_fermions
    hole_inds = list(set([i for i in range(num_orbitals)]) - set(particle_inds))
    assert len(hole_inds) == num_holes

    ind = 0

    for k in range(1, num_holes + 1):
        ind += math.comb(
            num_fermions + num_holes - (hole_inds[k - 1] + 1), num_holes + 1 - k
        )

    return ind


def J_zero_p2(particle_inds, num_fermions, num_orbitals):
    # Start counting from zero for both holes and the compound indices
    assert num_fermions <= num_orbitals

    num_holes = num_orbitals - num_fermions
    assert len(particle_inds) == num_fermions

    ind = 0

    for k in range(1, num_fermions + 1):
        ind += math.comb(
            num_orbitals - (particle_inds[k - 1] + 1), num_fermions + 1 - k
        )

    # To reverse the counting order, uncomment the line below
    return math.comb(num_orbitals, num_holes) - 1 - ind
    # return ind


N = 3
M = 6

for i in range(1, M + 1):
    for j in range(i + 1, M + 1):
        for k in range(j + 1, M + 1):
            inds = [i, j, k]
            print("")
            print(inds, J(inds, N, M))
            inds = [i - 1 for i in inds]
            print(inds, J_zero(inds, N, M))
            print(inds, J_zero_p(inds, M - N, M))


print("\n\n")

N = 6
M = 7
for i in range(1, M + 1):
    inds = [i]
    print("")
    print(inds, J(inds, N, M))
    inds = [i - 1 for i in inds]
    print(inds, J_zero(inds, N, M))
    print(inds, J_zero_p(inds, M - N, M))


print("\n\n")


N = 1
M = 7
for i in range(1, M + 1):
    for j in range(i + 1, M + 1):
        for k in range(j + 1, M + 1):
            for l in range(k + 1, M + 1):
                for p in range(l + 1, M + 1):
                    for q in range(p + 1, M + 1):
                        inds = [i, j, k, l, p, q]
                        print("")
                        print(inds, J(inds, N, M))
                        inds = [i - 1 for i in inds]
                        print(inds, J_zero(inds, N, M))
                        print(inds, J_zero_p(inds, M - N, M))


print("\n\n")


N = 4
M = 7
for i in range(1, M + 1):
    for j in range(i + 1, M + 1):
        for k in range(j + 1, M + 1):
            for l in range(k + 1, M + 1):
                inds = [i, j, k, l]
                print("")
                print(inds, J(inds, M - N, M))
                inds = [i - 1 for i in inds]
                print(inds, J_zero(inds, M - N, M))
                print(inds, J_zero_p(inds, N, M))
                print(inds, J_zero_p2(inds, N, M))
