class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        n = days[-1]
        dp = [0 for i in range(n+1)]
        
        valid = set(days)
        
        for i in range(1, n+1) :
            
            if i not in valid :
                dp[i] = dp[i-1]
            else :
                day = max(0, i-1)
                week = max(0, i-7)
                month = max(0, i-30)
                
                dp[i] = min(dp[day]+costs[0], 
                            dp[week]+costs[1], 
                            dp[month]+costs[2])
                
        return dp[n]
        
