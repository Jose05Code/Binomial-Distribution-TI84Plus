from src import LIB_MATH as math

def test_nCr():
    n = 20
    r = 4
    assert math.nCr(n, r) == 4845

def test_binopdf():
    n = 10
    p = 0.5
    a = 6
    assert math.binopdf(n, p, a) == 0.205078125