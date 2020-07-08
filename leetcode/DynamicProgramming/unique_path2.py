class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 0 or n == 0 :
            return 0
        
        dp = [1]*m
        
        for j in range(1, n) :
            for i in range(1, m) :
                dp[i] = dp[i-1] + dp[i]
                
        return dp[-1]
        
