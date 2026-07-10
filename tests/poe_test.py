import numpy as np
from poe import exp_twist

def test_identity():
    xi = [0, 0, 1, 0, 0, 0]

    T = exp_twist(xi, 0)

    assert np.allclose(T, np.eye(4))
    
def test_rotation_z():
    xi = [0, 0, 1, 0, 0, 0]

    T = exp_twist(xi, np.pi/2)

    expected = np.array([
        [0, -1, 0, 0],
        [1,  0, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])

    assert np.allclose(T, expected, atol=1e-6)
    
def test_se3_validity():
    xi = [0, 1, 0, 1, 0, 0]

    T = exp_twist(xi, 0.7)

    R = T[:3, :3]

    I = np.eye(3)

    assert np.allclose(R.T @ R, I, atol=1e-6)
    assert np.isclose(np.linalg.det(R), 1.0, atol=1e-6)
    
def test_translation():
    xi = [0, 0, 0, 0, 0, 1]

    T = exp_twist(xi, 2.0)

    expected = np.eye(4)
    expected[2, 3] = 2.0

    assert np.allclose(T, expected)
    
test_identity()
test_rotation_z()
test_se3_validity()
test_translation()
print("All tests passed for poe_test.py")