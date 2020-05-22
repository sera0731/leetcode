# Time complexity : O(N)
# Space complexity : O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) < 1 :
            return 0
        
        max_global = max_current = nums[0]
        
        for i in nums[1:] : 
            max_current = max(i, i + max_current)
            if max_current > max_global :
                max_global = max_current
                
        return max_global
 
