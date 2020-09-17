class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        mask = 0
        output = 0
        
        n = len(bin(max(nums)))-2
        
        for i in range(n-1, -1, -1) :
            
            mask = mask | (1<<i)
            prefix = set()
            
            for j in nums :
                prefix.add(j&mask)
            
            tmp = output | (1 << i)
            for p in prefix :
                
                if tmp ^ p in prefix :
                    output = tmp
                    break
                    
        return output
               
