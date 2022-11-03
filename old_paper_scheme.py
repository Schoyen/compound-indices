from math import comb


def Z(k, l, M, N):
    if M - N + k >= l >= k and k < N:
        z = 0

        for m in range(M - l + 1, M - k + 1):
            z += comb(m, N - k) - comb(m - 1, N - k - 1)

        return z

    assert M >= l >= N
    return l - N


def Phi(inds, M, N):
    assert len(inds) == N
    assert all([ind < M for ind in inds])

    phi = 1
    for i in range(1, N + 1):
        phi += Z(i, inds[i - 1], M, N)

    return phi


M = 5
N = 3

for i in range(1, M + 1):
    for j in range(i + 1, M + 1):
        for k in range(j + 1, M + 1):
            inds = [k, j, i]
            print(inds, Phi(inds, M, N))
