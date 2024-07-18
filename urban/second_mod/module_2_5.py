#!/usr/bin/env python


def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        matrix.append([])
        for _ in range(m):
            matrix[len(matrix) - 1].append(value)

    return matrix


print(get_matrix(4, 2, 13))
