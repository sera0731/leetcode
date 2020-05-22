class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        mi = 0
        mn = float("-inf")
        
        for i, x in enumerate(nums) :
            if x > mn :
                mi, mn = i, x
                
        mn /= 2
        
        for i, x in enumerate(nums) :    
            if i != mi :
                if x > mn :
                    return -1 
                
        return mi
