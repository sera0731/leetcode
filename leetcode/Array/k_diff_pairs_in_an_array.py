class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if len(nums) < 2 :
            return 0
        
        nums.sort()
        
        n = len(nums)
        start, end = 0, 1
        output = 0
        
        while start < n and end < n :
            
            diff = nums[end] - nums[start]
            
            if diff > k :
                start += 1
            elif start == end or diff < k :
                end += 1
            else :
                
                output += 1
                start += 1
                
                while start < n and nums[start] == nums[start-1] :
                    start += 1
                    
        return output
        
