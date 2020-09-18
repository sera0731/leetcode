# Memoization
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        if total % 2 :
            return False
        
        self.memo = {}
        return self.dfs(nums, 0, total // 2)
    
    def dfs(self, nums, i, ss) :
        
        if ss == 0 :
            return True
        
        if i == len(nums) or ss < 0 :
            return False
        
        if (i, ss) in self.memo :
            return self.memo[(i, ss)]
        
        result = self.dfs(nums, i+1, ss) or self.dfs(nums, i+1, ss-nums[i])
        self.memo[(i, ss)] = result
        
        return result

# Dynamic programming
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 :
            return False
        
        ss = total // 2
        n = len(nums)
        
        dp = [[False]*(ss+1) for i in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n+1) :
            curr = nums[i-1]
            for j in range(ss+1) :
                if j < curr :
                    dp[i][j] = dp[i-1][j]
                else :
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
                    
        return dp[-1][-1]
    
