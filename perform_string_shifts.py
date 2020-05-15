# Time complexity : O(N+L)
# Space complexity : O(1)

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        left = 0
        
        for [direction, amount] in shift:
            if direction == 0 :
                left += amount
            else :
                left -= amount
        
        left %= len(s)
        
        return s[left:] + s[:left] 
