import math


def J(particle_inds, N, M):
    assert N <= M
    assert len(particle_inds) == N

    occ_vec = [0] * M

    for p in particle_inds:
        occ_vec[p] += 1

    comp = 0

    for k in range(1, M):
        comp += math.comb(N + M - 1 - k - sum(occ_vec[:k]), M - k)

    return comp


N = 2
M = 6

counter = 0

for i in range(M):
    for j in range(i, M):
        particle_inds = [i, j]

        comp = J(particle_inds, N, M)

        print(particle_inds, comp, counter)
        counter += 1
