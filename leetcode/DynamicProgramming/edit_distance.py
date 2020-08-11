# Space complexity : O(N^2)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)
        
        if n == 0 or m == 0 :
            return n + m
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n+1) :
            dp[i][0] = i
            
        for j in range(m+1) :
            dp[0][j] = j
        
        for i in range(1, n+1) :
            for j in range(1, m+1) :
                
                left = dp[i][j-1]
                up = dp[i-1][j]
                left_up = dp[i-1][j-1]
                
                if word1[i-1] == word2[j-1] :
                    dp[i][j] = left_up
                else :
                    dp[i][j] = min(left, up, left_up) + 1
                    
        return dp[-1][-1]
        
# Space complexity : O(N)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)
        dp = [i for i in range(n+1)]
        
        for i in range(1, m+1) :
            
            left_up, dp[0] = dp[0], i
            
            for j in range(1, n+1) :
                
                left = dp[j-1]
                up = dp[j]
                
                if word1[j-1] == word2[i-1] :
                    dp[j] = left_up
                else :
                    dp[j] = min(left, up, left_up) + 1
                    
                left_up = up
                    
        return dp[-1]
                   
                
