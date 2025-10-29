from src import LIB_MATH as math

def test_factorial():
    n = 5
    assert math.factorial(5) == 120

def test_nCr():
    n = 20
    r = 4
    assert math.nCr(n, r) == 4845

def test_binopdf():
    n = 10
    p = 0.5
    a = 6
    assert math.binopdf(n, p, a) == 0.205078125

def test_binocdf():
    n = 10
    p = 0.5
    a = 6
    assert math.binocdf(n, p, a) == 0.828125