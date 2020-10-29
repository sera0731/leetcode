class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        output = []
        
        if not nums :
            return output
        
        n = len(nums)
        i = 0
        
        while i < n :
            
            j = i
            
            while i+1 < n and nums[i]+1 == nums[i+1] :
                i += 1
            
            if i == j :
                output.append(str(nums[i]))
            else :
                output.append('{}->{}'.format(nums[j],nums[i]))
                
            i += 1
            
        return output
        
