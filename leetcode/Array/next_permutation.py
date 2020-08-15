class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums :
            return
        
        n = len(nums)
        
        for l in range(n-1, -1, -1) :
            if nums[l-1] < nums[l] :
                break
        
        if l != 0 :
            for r in range(n-1, -1, -1) :
                if nums[l-1] < nums[r] :
                    break
            nums[l-1], nums[r] = nums[r], nums[l-1]
        
        nums[l:] = reversed(nums[l:])
        
