class Solution:
    def isPalindromic(self, l, r, s) :
        
        while l>=0 and r<len(s) and s[l] == s[r] :
            l -= 1
            r += 1
            
        return (l+1, r)
        
    def longestPalindrome(self, s: str) -> str:
        
        dist = lambda x : x[1] - x[0] 
        pos = (0, 0)
        
        for i in range(len(s)) :
            
            a = self.isPalindromic(i, i+1, s)
            b = self.isPalindromic(i, i, s)
            
            pos = max(pos, a, b, key=dist)
           
        l, r = pos
        
        return s[l:r]
    