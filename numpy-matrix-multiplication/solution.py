import numpy as np


def matmul_from_scratch(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    m, n = a.shape
    n2, p = b.shape

    if n != n2:
        raise ValueError("Incompatible matrix dimensions")

    result = np.zeros((m, p))

    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i, j] += a[i, k] * b[k, j]

    return result


def matmul_builtin(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b


def compare_matmul_and_elementwise(a: np.ndarray, b: np.ndarray) -> dict:
    if a.shape != b.shape:
        raise ValueError("Matrices must have the same shape")

    matmul_result = a @ b
    elementwise_result = a * b

    return {
        "matmul_result": matmul_result,
        "elementwise_result": elementwise_result,
        "results_are_different": not np.array_equal(
            matmul_result, elementwise_result
        )
    }
