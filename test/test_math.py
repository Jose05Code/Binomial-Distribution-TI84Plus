from src import LIB_MATH as math

def test_nCr():
    n = 20
    r = 4
    assert math.nCr(n, r) == 4845