class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s :
            return True
        
        l = 0
        r = len(s)-1
        
        while l < r :
            
            while l < len(s) and s[l].isalnum() == False :
                l += 1
            
            while r >= 0 and s[r].isalnum() == False :
                r -= 1
            
            if l < r and s[l].lower() != s[r].lower() :
                return False
            
            l += 1
            r -= 1
            
        return True
        
