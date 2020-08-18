class Solution:
    def numDecodings(self, s: str) -> int:
        
        def helper(i) :
            
            if i == n :
                return 1
            
            if  i > n or s[i] == "0":
                return 0
            
            if i in memo :
                return memo[i]
            
            first = helper(i+1)
            second = 0
            
            if int(s[i:i+2]) < 27 :
                second = helper(i+2)
                
            memo[i] = first + second
            return memo[i]
            
        n = len(s)
        memo = {}
        
        return helper(0)
        
class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == '0' :
            return 0
        
        n = len(s)
        dp = [0]*(n+1)
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            curr = int(s[i-2:i])
            
            if 9 < curr < 27 :
                dp[i] += dp[i-2]
        
        return dp[n]
    
