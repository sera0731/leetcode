class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(l, r) :
            
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
                    
            return (l+1, r)
        
        dist = lambda x : x[1]-x[0]
        pos = (0, 0)
        
        for i in range(len(s)) :
            
            x = helper(i, i)
            y = helper(i, i+1)
            
            pos = max(pos, x, y, key=dist)
            
        l, r = pos
        return s[l:r]
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False]*n for i in range(n)]
        output = ''
        
        for end in range(n) :
            for start in range(end+1) :
                
                if s[start] == s[end] :
                    
                    l = end-start+1
                    dp[start][end] = l<3 or dp[start+1][end-1] 
                    
                    if l > len(output) and dp[start][end] :
                        output = s[start:end+1]
        
        return output
        
