class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        l = None
        output = _sum = _max = 0
        
        for i in range(len(s)) :
            
            if l != s[i] :
                _sum += _max
                _max = 0
                
            l = s[i]
            _max = max(_max, cost[i])
            output += cost[i]
            
        return output - _sum - _max
    
