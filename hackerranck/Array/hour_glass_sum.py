def hourglassSum(arr):

    n = len(arr)-2
    ans = float('-inf')
    
    hg = [[0]*n for i in range(n)]

    for i in range(0, n) :
        for j in range(0, n) :
            hg[i][j] = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            ans = max(hg[i][j], ans)

    return ans
    
