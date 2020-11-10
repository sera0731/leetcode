class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        row = len(A)
        
        if not row :
            return []
        
        col = len(A[0])
        
        if not col :
            return []
        
        for i in range(row) :
            
            for j in range(ceil(col/2)) :
                
                k = col-j-1
                A[i][j], A[i][k] = 1^A[i][k], 1^A[i][j]
        
        return A
        
