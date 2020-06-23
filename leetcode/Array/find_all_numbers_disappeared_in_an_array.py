# Time complexity : O(N)
# Space complexity : O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        output = []
        
        for n in nums :
            
            idx = abs(n)-1
            
            if nums[idx] > 0 :
                nums[idx] *= -1
                
        for i in range(len(nums)) :
            if nums[i] > 0 :
                output.append(i+1)
                
        return output
        
