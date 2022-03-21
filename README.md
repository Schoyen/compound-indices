# Compound indices

This library provides functions for mapping index sets `(i, j, k, l, ...)` to a single compound index `I`, and back again! The most common example comes from indexing a matrix `A[i, j]` with `N_i` rows and `N_j` columns, as a one-dimensional array `A[I] = A[i * N_j + j]`. The reverse is found by `(i, j) = (I // N_j, I % N_j)`, where `//` is integer division and `%` gives the remainder.
