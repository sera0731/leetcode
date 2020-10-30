class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == '0' :
            return 0
        
        n = len(s)
        
        dp = [0]*(n)
        dp[0] = 1
        
        for i in range(1, n) :
            
            if 0 < int(s[i]) < 10:
                dp[i] += dp[i-1]
                
            if 9 < int(s[i-1]+s[i]) < 27 :
                dp[i] += dp[i-2] if i-2 >= 0 else 1
                    
        return dp[-1]
                
