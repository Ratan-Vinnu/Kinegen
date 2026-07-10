import numpy as np
from poe import exp_twist

def check_se3(T):
    R = T[:3, :3]

    rot_ok = np.allclose(R.T @ R, np.eye(3), atol=1e-6)
    det_ok = np.isclose(np.linalg.det(R), 1.0, atol=1e-6)

    return rot_ok and det_ok

def forward_kinematics(robot, thetas, return_all=False):

    if len(thetas) != len(robot.joints):
        raise ValueError("Theta count mismatch")

    T = np.eye(4)

    Ts = [T.copy()]

    for i, joint in enumerate(robot.joints):

        xi = joint.twist
        theta = thetas[i]

        T_i = exp_twist(xi, theta)

        T = T @ T_i
        Ts.append(T.copy())
        
    T = T @ robot.M

    if return_all:
        Ts.append(T.copy())
        return Ts
    else:
        return T

def get_joint_positions(robot, thetas):
    
    Ts = forward_kinematics(robot, thetas, return_all=True)
    pts = np.array([T[:3, 3] for T in Ts])
    return pts