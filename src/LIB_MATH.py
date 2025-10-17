def nCr(n, a):
    if a == 0:
        return 1
    if n == a:
        return 1
    
    return nCr(n-1, a-1) + nCr(n-1, a)

def binopdf(n, p, a):
    return nCr(n, a)*(p**a)*(1-p)**(n-a)

def binocdf(n, p, a):
    cdf = 0
    for i in range(a+1):
        cdf += binopdf(n,p,i)
    return cdf