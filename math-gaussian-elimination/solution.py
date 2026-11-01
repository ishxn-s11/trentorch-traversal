
import numpy as np


def gaussian_eliminate(A, b):

    A = np.array(A, dtype=float).copy()
    b = np.array(b, dtype=float).copy()

    n = len(b)

    for i in range(n - 1):

        for j in range(i + 1, n):

            f = A[j, i] / A[i, i]

            A[j, :] = A[j, :] - f * A[i, :]
            b[j] = b[j] - f * b[i]

    return A, b


def back_substitute(U, c):

    n = len(c)
    x = np.zeros(n, dtype=float)

    for i in range(n - 1, -1, -1):

        total = np.dot(U[i, i + 1:], x[i + 1:])

        x[i] = (c[i] - total) / U[i, i]

    return x
