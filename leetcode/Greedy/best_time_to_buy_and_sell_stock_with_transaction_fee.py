class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        if not prices :
            return 0
        
        profit = 0
        curr = prices[0]
        
        for stock in prices[1:] :
            
            delta = stock - curr - fee
            
            if stock < curr :
                curr = stock
            elif delta > 0 :
                profit += delta
                curr = stock - fee
                
        return profit
        
