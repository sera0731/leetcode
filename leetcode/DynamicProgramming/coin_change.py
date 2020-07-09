class Solution:
    def __init__(self) :
        self.coins = []
        self.memo = {}
    
    def helper(self, current) :
        
        if current < 0 :
            return -1
        if current == 0 :
            return 0
        if current in self.memo :
            return self.memo[current]
        
        _min = float('inf')
        
        for i in range(len(self.coins)) :
            result = self.helper(current-self.coins[i])
            if result > -1 and result < _min :
                _min = result+1
                
        self.memo[current] = -1 if _min == float('inf') else _min
        return self.memo[current]
        
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        return self.helper(amount)
        
