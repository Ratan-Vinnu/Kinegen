def test_se3_invariance():
    from poe import exp_twist
    import numpy as np

    xi = [0.3, -0.2, 0.8, 0.5, 1.0, -0.3]

    for theta in np.linspace(-2, 2, 10):
        T = exp_twist(xi, theta)

        R = T[:3, :3]

        assert np.allclose(R.T @ R, np.eye(3), atol=1e-6)
        assert np.isclose(np.linalg.det(R), 1.0, atol=1e-6)
        
def test_zero_angle_identity():
    from poe import exp_twist
    import numpy as np

    xi = [1, 0, 0, 2, 3, 4]

    T = exp_twist(xi, 0)

    assert np.allclose(T, np.eye(4), atol=1e-9)
    
def test_exponential_additivity():
    from poe import exp_twist
    import numpy as np

    xi = [0.1, 0.3, 0.9, 1.0, -0.2, 0.5]

    t1 = 0.4
    t2 = 0.7

    T1 = exp_twist(xi, t1)
    T2 = exp_twist(xi, t2)
    T12 = exp_twist(xi, t1 + t2)

    assert np.allclose(T1 @ T2, T12, atol=1e-5)
    
def test_small_angle():
    from poe import exp_twist
    import numpy as np
    from poe import twist_hat

    xi = [0.2, 0.4, 0.7, 1.0, -0.5, 0.3]
    theta = 1e-6

    T = exp_twist(xi, theta)
    approx = np.eye(4) + twist_hat(xi) * theta

    assert np.allclose(T, approx, atol=1e-6)
    
def test_rotation_magnitude_stability():
    from poe import exp_twist
    import numpy as np

    xi = [0, 0, 1, 0, 0, 0]

    for theta in np.linspace(-10, 10, 50):
        T = exp_twist(xi, theta)
        R = T[:3, :3]

        angle_error = np.linalg.norm(R.T @ R - np.eye(3))

        assert angle_error < 1e-5
    
test_se3_invariance()
test_zero_angle_identity()
test_exponential_additivity()
test_small_angle()
test_rotation_magnitude_stability()

print("STRICT POE TESTS PASSED")