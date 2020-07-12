class Solution:
    
    # Iterative
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        mod = 10**9 + 7
        
        dp = [[0]*(target+1) for j in range(d + 1)]
        dp[0][0] = 1
        
        for r in range(1, d+1):
            for t in range(target+1):
                for curr in range(1, min(t, f)+1):
                    dp[r][t] = (dp[r][t] + dp[r-1][t-curr]) % mod
                    
        return dp[d][target] % mod
    
     # Recursive
     def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        memo = {}
        
        def helper(remain, t) :
            
            if remain == 0 :
                return 0 if t > 0 else 1
            if (remain, t) in memo :
                return memo[(remain, t)]
            
            total = 0
            
            for i in range(max(0, t-f), t) :
                total += helper(remain-1, i)
            
            memo[(remain, t)] = total
            return total
        
        return helper(d, target)%(10**9+7)
