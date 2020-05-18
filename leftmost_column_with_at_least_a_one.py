# Time complexity : O(NlogM)
# Space complexity : O(1)

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        leftmost = float("inf")
        
        for i in range(rows) :
            
            l = 0
            r = cols-1
            
            while l < r :
                
                mid = l + (r-l)//2
                
                if binaryMatrix.get(i, mid) == 0 :
                    l = mid + 1
                else :
                    r = mid
            
            if binaryMatrix.get(i, l) == 1 :
                leftmost = min(leftmost, l)
            
        return leftmost if leftmost != float("inf") else -1
    

# Time complexity : O(N+M)
# Space complexity : O(1)

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        
        current_row = 0
        current_col = cols-1
        
        while current_row < rows and current_col >= 0 :
            if binaryMatrix.get(current_row, current_col) == 0 :
                current_row += 1
            else :
                current_col -= 1
        
        return current_col+1 if current_col != cols - 1 else -1

