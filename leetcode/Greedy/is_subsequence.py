# Time complexity : O(T)
# Space complexity : O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s :
            return True
        
        if len(s) > len(t) :
            return False
        
        i, j = 0, 0
        left, right = len(s), len(t)
        
        while i < left and j < right :
            
            if s[i] == t[j] :
                i += 1
                
            j += 1
        
        return i == len(s)
        
