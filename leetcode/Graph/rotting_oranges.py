class Solution:
    def bfs(self, grid, total) :
        
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        
        days = 0
        curr = 0
        
        while self.queue :
            
            n = len(self.queue)
            for _ in range(n) :
                
                x, y = self.queue.popleft()
            
                for k in range(len(dx)) :
                
                    nx = x + dx[k]
                    ny = y + dy[k]
                
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 :
                        grid[nx][ny] = 2
                        curr += 1
                        self.queue.append((nx, ny))
                    
            days += 1
            
        return -1 if total != curr else days-1
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        orgs = 0
        self.queue = collections.deque([])
        
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    orgs += 1
                elif grid[i][j] == 2 :
                    self.queue.append((i, j))
                    
        if orgs == 0 :
            return 0
        
        return self.bfs(grid, orgs)
                    
            
