# Time complexity : O(M * N)
# Space complexity : O(M * N)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        visited = set()
        
        delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                
                if grid[i][j] == "1" and (i, j) not in visited :
                    islands += 1
                    stack = [(i, j)]
                    
                    while stack :
                        
                        x = stack.pop()
                        visited.add((x[0], x[1]))
                        
                        for di in delta :
                            dx = x[0] + di[0]
                            dy = x[1] + di[1]
                            
                            if dx >= 0 and dx < len(grid) and  dy >= 0 and dy < len(grid[0]):
                                if grid[dx][dy] == "1" and (dx, dy) not in visited :
                                    stack.append((dx, dy))
                                    
        return islands
