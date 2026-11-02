import numpy as np

def lu_decompose(A):
    """
    A: a square (n, n) NumPy array that does not require row swaps.

    Returns:
        (L, U): L is lower-triangular with 1s on the diagonal,
        U is upper-triangular, such that L @ U reconstructs A.
    """
    U=A.astype(float).copy()
    n=U.shape[0]
    L=np.eye(n)
    
    for i in range(n):

        for j in range(i+1,n):
            mult=U[j,i]/U[i,i]
            L[j,i]=mult
            U[j,i:]-=mult*U[i,i:]

    return L,U
