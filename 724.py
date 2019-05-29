class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        S = sum(nums)
        left = 0
        
        for i, x in enumerate(nums) :
            if left == S-left-x :
                return i
            left += x
        
        return -1
        