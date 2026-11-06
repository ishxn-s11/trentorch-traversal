
import numpy as np


def rank(A):
    """
    Returns the rank of A using Gaussian elimination.
    """
    A = np.array(A, dtype=float)
    m, n = A.shape

    pivot_row = 0
    pivot_col = 0
    pivots = 0

    while pivot_row < m and pivot_col < n:

        # Find the row with the largest absolute value
        max_row = pivot_row + np.argmax(
            np.abs(A[pivot_row:, pivot_col])
        )

        # Skip column if no usable pivot exists
        if abs(A[max_row, pivot_col]) < 1e-10:
            pivot_col += 1
            continue

        # Swap rows
        A[[pivot_row, max_row]] = A[[max_row, pivot_row]]

        # Normalize pivot row
        A[pivot_row] /= A[pivot_row, pivot_col]

        # Eliminate entries below the pivot
        for i in range(pivot_row + 1, m):
            factor = A[i, pivot_col]
            A[i] -= factor * A[pivot_row]

        pivots += 1
        pivot_row += 1
        pivot_col += 1

    return pivots


def nullity(A):
    """
    Returns nullity using the Rank-Nullity Theorem.
    """
    return A.shape[1] - rank(A)
