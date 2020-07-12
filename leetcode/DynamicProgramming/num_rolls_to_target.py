class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        mod = 10**9 + 7
        
        dp = [[0]*(target+1) for j in range(d + 1)]
        dp[0][0] = 1
        
        for r in range(1, d+1):
            for t in range(target+1):
                for curr in range(1, min(t, f)+1):
                    dp[r][t] = (dp[r][t] + dp[r-1][t-curr]) % mod
                    
        return dp[d][target] % mod
        
