class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        start = 0
        
        for end in range(len(A)) :
            
            K = K-(1^A[end])
            
            if K < 0 :
                K = K + (1^A[start])
                start += 1
                
        return end-start+1
		
