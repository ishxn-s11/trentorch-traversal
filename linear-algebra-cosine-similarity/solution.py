import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    a, b: 1-D vectors of equal length.

    Returns:
        the cosine of the angle between a and b, or 0.0 if either has
        zero length.
    """
    # TODO: Dot product divided by the product of the norms.
    pass
    
    if a.shape!=b.shape:
        
        raise ValueError("Vectors must have the same shape")

    if a.size == 0:
        
        raise ValueError("Vector cannot be empty")

    a_norm=np.linalg.norm(a)
    b_norm=np.linalg.norm(b)

    if a_norm==0 or b_norm==0:
        
        return 0.0

    return float(np.dot(a,b)/(a_norm*b_norm))
