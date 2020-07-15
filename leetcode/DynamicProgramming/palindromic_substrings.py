class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        dp = [[0]*(n) for i in range(n)]
        
        count = 0
        
        for i in range(n) :
            for j in range(i+1) :
                if s[i] == s[j] :
                    dp[j][i] = (i-j+1)<3 or dp[j+1][i-1]
                    count += dp[j][i]
                            
        return count
        
