class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev = 0
        curr = 0
        
        for n in nums :
            tmp = curr
            curr = max(prev + n, curr)
            prev = tmp
        
        return curr
        
