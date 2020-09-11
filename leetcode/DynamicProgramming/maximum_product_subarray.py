class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxv = minv = nums[0]
        output = maxv
        
        for v in nums[1:] :
            
            if v < 0 :
                maxv, minv = minv, maxv
                
            maxv = max(v, maxv*v)
            minv = min(v, minv*v)
            
            output = max(output, maxv)
        
        return output
            
        
