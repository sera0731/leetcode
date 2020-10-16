class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0] :
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = m*n-1
        
        while l <= r :
            
            mid = (r-l)//2 + l
            current = matrix[mid//n][mid%n]
            
            if current == target :
                return True
            elif current < target :
                l = mid + 1
            else :
                r = mid - 1
            
        return False
        
