class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        merged = []
        pp = 0 # positive
        
        while pp < len(A) and A[pp] < 0 :
            pp += 1
            
        np = pp-1 # negative
        
        while np >= 0 or pp < len(A) :
            
            if pp >= len(A) or (np >= 0 and abs(A[np]) < A[pp]) :
                merged.append(A[np]**2)
                np -= 1
            else :
                merged.append(A[pp]**2)
                pp += 1
                
        return merged
    
