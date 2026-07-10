# valid.py
import numpy as np


def is_unit_vector(v, tol=1e-3):
    v = np.array(v, dtype=float)
    norm = np.linalg.norm(v)
    return np.isclose(norm, 1.0, atol=tol)


def is_zero_vector(v, tol=1e-8):
    v = np.array(v, dtype=float)
    return np.linalg.norm(v) < tol


def is_valid_se3(M, tol=1e-3):
    """
    Check if M ∈ SE(3)
    """
    M = np.array(M, dtype=float)

    if M.shape != (4, 4):
        return False

    R = M[:3, :3]
    p = M[:3, 3]
    last_row = M[3, :]

    # rotation validity
    should_be_identity = R.T @ R
    rot_ok = np.allclose(should_be_identity, np.eye(3), atol=tol)

    # determinant check (proper rotation)
    det_ok = np.isclose(np.linalg.det(R), 1.0, atol=tol)

    # last row check
    last_row_ok = np.allclose(last_row, [0, 0, 0, 1], atol=tol)

    return rot_ok and det_ok and last_row_ok


def check_finite(arr, name="vector"):
    arr = np.array(arr, dtype=float)
    if not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} contains NaN or Inf")



def validate_joint(joint):
    check_finite(joint.axis, "joint.axis")
    check_finite(joint.point, "joint.point")

    if not isinstance(joint.name, str):
        raise ValueError("Joint name must be a string")

    axis = np.array(joint.axis, dtype=float)
    point = np.array(joint.point, dtype=float)

    if axis.shape != (3,):
        raise ValueError(f"{joint.name}: axis must be 3D")

    if point.shape != (3,):
        raise ValueError(f"{joint.name}: point must be 3D")

    if is_zero_vector(axis):
        raise ValueError(f"{joint.name}: axis is zero vector")

    if not is_unit_vector(axis):
        raise ValueError(f"{joint.name}: axis must be unit vector")

    if joint.limits is not None:
        if len(joint.limits) != 2:
            raise ValueError(f"{joint.name}: limits must be [min, max]")
        if joint.limits[0] >= joint.limits[1]:
            raise ValueError(f"{joint.name}: invalid limits order")



def validate_robot(robot):

    if not isinstance(robot.name, str):
        raise ValueError("Robot name must be a string")

    if not isinstance(robot.joints, list) or len(robot.joints) == 0:
        raise ValueError("Robot must have a non-empty joint list")

    if robot.frame != "space":
        raise ValueError("Only space-frame PoE supported")

    if not is_valid_se3(robot.M):
        raise ValueError("Invalid SE(3) matrix M")

    # validate each joint
    for j in robot.joints:
        validate_joint(j)

    return True