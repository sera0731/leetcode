def jumpingOnClouds(c):

    i = 0
    steps = 0

    while i+2 < len(c) :
        
        _next = c[i+1]
        _nnext = c[i+2]

        if _nnext == 0 :
            i += 2
        elif _next == 0 :
            i += 1
        
        steps += 1

    return steps + (i != len(c)-1)
    
