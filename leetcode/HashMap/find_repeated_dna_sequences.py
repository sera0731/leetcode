class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        # A C G T
        dna = {'A':0,'C':1,'G':2,'T':3}
        
        L = 10
        n = len(s)
        
        if n < L :
            return []
        
        nums = [dna[ch] for ch in s]
        bitmask = 0
        
        seen = set()
        output = set()
        
        for i in range(L) :
            bitmask <<= 2
            bitmask |= nums[i]
            
        seen.add(bitmask)
        
        for i in range(1, n-L+1) :
            
            bitmask <<= 2
            bitmask &= ~(3<<2*L)
            bitmask |= nums[i+L-1]
            
            if bitmask in seen :
                output.add(s[i:i+L])
            
            seen.add(bitmask)
        
        return output
        
