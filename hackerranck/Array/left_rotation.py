def rotLeft(a, d):
    x = d % len(a)
    return a[x:] + a[:x]
    
