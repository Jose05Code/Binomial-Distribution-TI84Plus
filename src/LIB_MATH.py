def nCr(n, a):
    if a == 0:
        return 1
    if n == a:
        return 1
    
    return nCr(n-1, a-1) + nCr(n-1, a)


