import math

def nCr(n, a):
    if a < 0 or a > n:
        return 0
    return math.factorial(n) // (math.factorial(a) * math.factorial(n - a))

def binopdf(n, p, a):
    return nCr(n, a)*(p**a)*(1-p)**(n-a)

def binocdf(n, p, a):
    cdf = 0
    for i in range(a+1):
        cdf += binopdf(n,p,i)
    return cdf