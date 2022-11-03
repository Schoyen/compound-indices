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


N = 3
M = 6

for i in range(1, M + 1):
    for j in range(i + 1, M + 1):
        for k in range(j + 1, M + 1):
            inds = [i, j, k]
            print(inds, J(inds, N, M))


print("")

N = 6
M = 7
for i in range(1, M + 1):
    inds = [i]
    print(inds, J(inds, N, M))


print("")


N = 1
M = 7
for i in range(1, M + 1):
    for j in range(i + 1, M + 1):
        for k in range(j + 1, M + 1):
            for l in range(k + 1, M + 1):
                for p in range(l + 1, M + 1):
                    for q in range(p + 1, M + 1):
                        inds = [i, j, k, l, p, q]
                        print(inds, J(inds, N, M))
