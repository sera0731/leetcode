class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        startColor = image[sr][sc]
        
        if startColor == newColor :
            return image
        
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = collections.deque([(sr, sc)])
        
        while q :
            
            r, c = q.popleft()
            image[r][c] = newColor
            
            for dr, dc in d :
                
                nr = r + dr
                nc = c + dc
                
                if nr < 0 or nr > len(image)-1 or nc < 0 or nc > len(image[0])-1 :
                    continue
                
                if image[nr][nc] == startColor :
                    q.append((nr, nc))
        
        return image
        
