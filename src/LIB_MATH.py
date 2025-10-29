def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def nCr(n, a):
    if a < 0 or a > n:
        return 0
    return factorial(n)/(factorial(n-a)*factorial(a))

def binopdf(n, p, a):
    return nCr(n, a)*(p**a)*(1-p)**(n-a)

def binocdf(n, p, a):
    cdf = 0
    for i in range(a+1):
        cdf += binopdf(n,p,i)
    return cdf