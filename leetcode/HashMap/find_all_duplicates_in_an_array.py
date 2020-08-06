# Space complexity : O(N)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        output = []
        seen = set()
        
        for n in nums :
            if n in seen :
                output.append(n)
            else :
                seen.add(n)
                
        return output

# Space complexity : O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        output = []
        
        for n in nums :
            
            i = abs(n)-1
            
            if nums[i] < 0 :
                output.append(i+1)
            else :
                nums[i] *= -1
        
        return output
            
