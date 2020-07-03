class Solution:
    def merge(self, left, right, nums) :
        
        l = r = i = 0
        
        while l < len(left) and r < len(right) :
            
            if left[l] < right[r] :
                nums[i] = left[l]
                l += 1
            else :
                nums[i] = right[r]
                r += 1
                
            i += 1
            
        while l < len(left) :
            nums[i] = left[l]
            l += 1
            i += 1
        
        while r < len(right) : 
            nums[i] = right[r]
            r += 1
            i += 1
            
        return nums
        
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1 :
            return nums
        
        m = len(nums) // 2
        
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])
        
        return self.merge(left, right, nums)
        
