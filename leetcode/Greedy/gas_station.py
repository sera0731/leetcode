class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        
        total = current = 0
        start = 0
        
        for i in range(n) :
            
            amount = gas[i] - cost[i]
            
            total += amount
            current += amount
            
            if current < 0 :
                current = 0
                start = i+1
        
        return -1 if total < 0 else start
        
