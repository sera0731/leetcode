class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False]*(n+1)
        
        for i in range(n+1) :
            
            maxsize = int(i**0.5)+1
            
            for j in range(1, maxsize) :
                if dp[i-j*j] == False :
                    dp[i] = True
                    break
                    
        return dp[-1]
    
