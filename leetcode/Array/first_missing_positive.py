class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if 1 not in nums :
            return 1
        
        n = len(nums)
        
        for i in range(n) :
            if nums[i] <= 0 or nums[i] > n :
                nums[i] = 1
        
        for i in range(n) :
            t = abs(nums[i])
            if t <= n :
                nums[t-1] = -abs(nums[t-1])
                
        for i in range(1, n+1) :
            if nums[i-1] > 0 :
                return i
            
        return n+1
            
