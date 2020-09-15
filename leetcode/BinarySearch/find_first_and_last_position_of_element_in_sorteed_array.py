class Solution:
    def binarySearch(self, nums, target, l=0) :
        
        r = len(nums) - 1
        
        while l <= r :
            
            mid = l + (r-l)//2
            
            if nums[mid] < target :
                l = mid+1
            else :
                r = mid-1
        
        return l
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = self.binarySearch(nums, target)
        
        if l >= len(nums) or nums[l] != target :
            return [-1, -1]
        
        r = self.binarySearch(nums, target+1, l)
        
        return [l, r-1]
    
