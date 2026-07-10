import numpy as np
from math_utils import normalize, rodrigues, skew


def compute_twist(axis, point):
    
    axis = normalize(axis)
    point = np.array(point, dtype=float)

    v = -np.cross(axis, point)
    twist = np.concatenate((axis, v))

    return twist

def twist_hat(twist):

    twist = np.array(twist, dtype=float)

    if twist.shape != (6,):
        raise ValueError("twist must be a 6D vector")

    omega = twist[:3]
    v = twist[3:]

    omega_hat = skew(omega)
    
    upper = np.hstack((omega_hat, v.reshape(3, 1)))
    
    lower = np.array([[0.0, 0.0, 0.0, 0.0]])
    
    xi_hat = np.vstack((upper, lower))

    return xi_hat

def exp_twist(twist, theta):

    twist = np.array(twist, dtype=float)

    if twist.shape != (6,):
        raise ValueError("twist must be a 6D vector")

    omega = twist[:3]
    v = twist[3:]

    omega_norm = np.linalg.norm(omega)

    T = np.eye(4)

    if omega_norm > 1e-12:

        omega = normalize(omega)
        omega_hat = skew(omega)

        R = rodrigues(omega, theta)

        I = np.eye(3)

        p = (
            (I * theta)
            + (1 - np.cos(theta)) * omega_hat
            + (theta - np.sin(theta)) * (omega_hat @ omega_hat)
        ) @ v

        T[:3, :3] = R
        T[:3, 3] = p

    else:
        T[:3, 3] = v * theta

    return T
