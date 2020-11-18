# Greedy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums :
            return 0
        
        curr_max = output = nums[0]
        
        for i in range(1, len(nums)) :
            curr_max = max(curr_max+nums[i], nums[i])          
            output = max(output, curr_max)
        
        return output
            
# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums :
            return 0
        
        n, output = len(nums), nums[0]
        dp = [0]*(n+1)
        
        for i in range(n) :
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            output = max(dp[i], output)
            
        return output
