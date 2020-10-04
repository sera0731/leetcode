class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        output = []
        
        for i in nums :
            t = abs(i)-1
            if nums[t] > 0 :
                nums[t] *= -1
        
        for i in range(len(nums)) :
            if nums[i] > 0 :
                output.append(i+1)
        
        return output
               
