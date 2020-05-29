# Time complexity : O(J+S)
# Space complexity : O(J)

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        ans = 0
        hs = set(J)
        
        for s in S :
            if s in hs :
                ans += 1
        
        return ans
