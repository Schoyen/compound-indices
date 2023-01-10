# Compound indices
![](https://github.com/Schoyen/compound-indices/actions/workflows/python-package.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This library provides functions for mapping index sets $(i, j, k, l, ...)$ to a
single compound index $I$, and back again.
That is, a form of ranking and unranking.
The most common example comes from indexing a matrix `A[i, j]` with `L` rows
and columns, as a one-dimensional array `A[I] = A[i * L + j]`.
The reverse is found by `(i, j) = (I // N, I % N)`, where `//` is integer
division and `%` gives the remainder.

## Dense indexing
The library provides functionality for "dense" tensors, that is, tensors where
there is no symmetry when permuting the indices.
These tensors can also be of variable length in each axis.

## Antisymmetric indexing
There is functionality for mapping antisymmetric indices to a compound index,
and back again.
Here antisymmetric indices are on the form $i < j < k < \dots$, and a tensor made
from these will induce a sign change when swapping two indices.
That is, $t^{ij}\_{kl} = -t^{ji}\_{kl} = -t^{ij}\_{lk} = t^{ji}\_{lk}$,
when $t^{ij}\_{kl}$ is an antisymmetric tensor of rank 4.
There is also a function computing the sign of a given permutation of indices.

## Symmetric indexing
Finally, there is functionality for the mapping of symmetric indices to a
compound index, but _not_ back again (so far).
Symmetric indices are on the form $i \leq j \leq k \leq \dots$, and a symmetric
tensor will satisfy $t^{ij}\_{kl} = t^{ji}\_{kl} = t^{ij}\_{lk} = t^{ji}\_{lk}$


## Limitations
Note that only the indices of the dense tensors support variable length for
each axis.
The symmetric and antisymmetric indices assumes that each axis are of the same
length.

There are little to no optimizations done for the algorithms, and most likely
there exists way faster implementations elsewhere.
