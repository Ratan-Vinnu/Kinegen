def test_skew_properties():
    import numpy as np
    from math_utils import skew

    w = [1, 2, 3]
    S = skew(w)

    assert np.allclose(S, -S.T)
    
from math_utils import skew, unskew
import numpy as np

def test_unskew_inverse():
    w = [0.3, -1.2, 2.0]

    S = skew(w)
    w2 = unskew(S)

    assert np.allclose(w, w2)

from math_utils import rodrigues
import numpy as np

def test_rodrigues_identity():
    omega = [1, 0, 0]
    theta = 0

    R = rodrigues(omega, theta)

    assert np.allclose(R, np.eye(3))
    
def test_rodrigues_90deg_z():
    import numpy as np
    from math_utils import rodrigues

    omega = [0, 0, 1]
    theta = np.pi / 2

    R = rodrigues(omega, theta)

    expected = np.array([
        [0, -1, 0],
        [1,  0, 0],
        [0,  0, 1]
    ])

    assert np.allclose(R, expected, atol=1e-6)

from math_utils import normalize
import numpy as np

def test_normalize():
    v = [3, 4, 0]

    u = normalize(v)

    assert np.isclose(np.linalg.norm(u), 1.0)
    
from math_utils import normalize

def test_normalize_zero_vector():
    try:
        normalize([0, 0, 0])
        assert False  # should not reach here
    except Exception:
        assert True

def test_rodrigues_is_rotation():
    import numpy as np
    from math_utils import rodrigues

    omega = [1, 2, 3]
    theta = 0.7

    R = rodrigues(omega, theta)

    I = np.eye(3)

    assert np.allclose(R.T @ R, I, atol=1e-6)
    assert np.isclose(np.linalg.det(R), 1.0, atol=1e-6)


test_skew_properties()
test_unskew_inverse()
test_rodrigues_identity()
test_rodrigues_90deg_z()
test_normalize()
test_normalize_zero_vector()
test_rodrigues_is_rotation()
