class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        i = 0
        farthest = nums[0]
        
        while i < n and i <= farthest :
            farthest = max(farthest, i+nums[i])
            i += 1
        
        return farthest >= n-1
            
