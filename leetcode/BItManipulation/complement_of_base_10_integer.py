class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        if N == 0 :
            return 1
        
        output = N
        counter = N
        
        bit = 1
        
        while counter :
            
            output = output ^ bit
            bit <<= 1
            counter >>= 1
            
        return output
    
