class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 0 or n == 0 :
            return 0
        
        dp = [[0]*m for i in range(n)]
        
        for i in range(n) :
            dp[i][0] = 1
        
        for i in range(m) :
            dp[0][i] = 1
            
        for j in range(1, m) :
            for i in range(1, n) :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[n-1][m-1]
        
