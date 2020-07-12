class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 0 :
            return 0
        
        dp = [0]*(n+1)
        
        dp[0] = nums[0]
        
        for i in range(1, n) :
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
        return dp[n-1]
            
