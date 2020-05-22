
def merge(L, R, arr) :
    
    l = r = i = 0
    
    while l<len(L) and r<len(R) :
        
        if L[l]<=R[r] :
            arr[i] = L[l]
            l += 1
        else :
            arr[i] = R[r]
            r += 1
            
        i += 1
            
    while l < len(L) :
        arr[i] = L[l]
        i += 1
        l += 1
    
    while r < len(R) :
        arr[i] = R[r]
        i += 1
        r += 1
        
    return arr
    
def mergeSort(arr):
    
    if len(arr) <= 1:
        return arr
    
    m = len(arr) // 2
    
    L = mergeSort(arr[:m])
    R = mergeSort(arr[m:])
    
    merge(L, R, arr)
    return arr
