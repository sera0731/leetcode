class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev = 0
        curr = 0
        
        for num in nums :
            tmp = curr
            curr = max(curr, prev + num)
            prev = tmp
            
        return curr
