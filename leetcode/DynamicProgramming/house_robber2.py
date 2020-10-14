class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums :
            return 0
        
        if len(nums) == 1 :
            return nums[0]
        
        # Delete first or last
        output = max(self.getMoney(nums[1:]), self.getMoney(nums[:-1]))
        return output
    
    def getMoney(self, nums):
        
        prev = curr = 0
        
        for i in nums :
            tmp = curr
            curr = max(prev + i, curr)
            prev = tmp
        
        return curr
        
