# Compound indices
![](https://github.com/Schoyen/compound-indices/actions/workflows/python-package.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This library provides functions for mapping index sets `(i, j, k, l, ...)` to a single compound index `I`, and back again! The most common example comes from indexing a matrix `A[i, j]` with `L` rows and columns, as a one-dimensional array `A[I] = A[i * L + j]`. The reverse is found by `(i, j) = (I // N, I % N)`, where `//` is integer division and `%` gives the remainder. We limit ourselves to "square" tensors where all axis' have the same length. The library provides functionality for "dense" tensors, that is, tensors where there is no symmetry when permuting the indices, and antisymmetric and symmetric tensors where `i < j < k < ...`, and permuting a pair of indices leads to a sign change and no sign change respectively.
