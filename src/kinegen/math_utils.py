
import numpy as np

def skew(w):
    
    w = np.array(w, dtype=float)
    
    if w.shape != (3,):
        raise ValueError("skew() expects 3D vector")
    
    return np.array([[0, -w[2], w[1]],
                    [w[2], 0, -w[0]],
                    [-w[1], w[0], 0]
                    ])
    
def normalize(v):
    v = np.array(v, dtype=float)

    mag = np.linalg.norm(v)

    if np.isclose(mag, 0):
        raise ValueError("Cannot normalize zero vector.")

    return v / mag

def unskew(M):
    
    M = np.array(M, dtype=float)
    
    if not np.allclose(M, -M.T):
        raise ValueError("Matrix is not skew-symmetric")

    return np.array([
        M[2, 1],
        M[0, 2],
        M[1, 0]
    ])

def rodrigues(omega, theta):
    omega = normalize(omega)
    omega_skew = skew(omega)

    return (
        np.eye(3)
        + np.sin(theta) * omega_skew
        + (1 - np.cos(theta)) * (omega_skew @ omega_skew)
    )
