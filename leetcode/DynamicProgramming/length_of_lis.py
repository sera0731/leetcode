# Brute Force
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(prev=float('-inf'), i=0) :
            
            if i == len(nums) :
                return 0
            
            include = 1 + dfs(nums[i], i+1) if nums[i] > prev else 0
            exclude = dfs(prev, i+1)
            return max(include, exclude)
            
        return dfs()
        
# Memoization
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(prev=-1, i=0) :
            
            if i == n :
                return 0
            
            if memo[prev+1][i] >= 0 :
                return memo[prev+1][i]
            
            include = 1 + dfs(i, i+1) if prev < 0 or nums[i] > nums[prev] else 0
            exclude = dfs(prev, i+1)
            
            memo[prev+1][i] = max(include, exclude)
            return memo[prev+1][i]
        
        n = len(nums)
        memo = [[-1]*n for i in range(n+1)]
        
        return dfs()
 
# Dynamic Programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums :
            return 0
        
        n = len(nums)
        
        dp = [0]*n
        dp[0] = 1
        
        lis = 1
        
        for i in range(1, n) :
            curr = 0
            for j in range(i) :
                if nums[i] > nums[j] :
                    curr = max(curr, dp[j])
            dp[i] = curr + 1
            lis = max(lis, dp[i])
            
        return lis
    
    
