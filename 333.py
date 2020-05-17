# Time complexity : O(M*N)
# Space complexity : O(1)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid :
            return 0
        
        x = len(grid)
        y = len(grid[0])
        
        for i in range(x) :
            for j in range(y) :
                if i == 0 and j > 0 :
                    grid[i][j] += grid[i][j-1]
                elif j == 0 and i > 0 :
                    grid[i][j] += grid[i-1][j]
                elif i > 0 and j > 0 :
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                
        return grid[-1][-1]
        
