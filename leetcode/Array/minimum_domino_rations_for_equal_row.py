class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        def helper(x) :
            
            cnt_a = cnt_b = 0
            
            for i in range(len(A)) :
            
                if x != A[i] and x != B[i] :
                    return -1
                elif A[i] != x :
                    cnt_a += 1
                elif B[i] != x :
                    cnt_b += 1
                
            return min(cnt_a, cnt_b)
        
        a = helper(A[0])
        
        if a != -1 or A[0] == B[0] :
            return a
        
        return helper(B[0])
        
