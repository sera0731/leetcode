class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(start=0) :
            
            if start == len(nums) :
                output.append(nums[:])
                return
            
            for i in range(start, len(nums)) :
                nums[start], nums[i] = nums[i], nums[start]
                helper(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        
        output = []
        
        helper()
        return output
        
