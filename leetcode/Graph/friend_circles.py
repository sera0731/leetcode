class Solution:
    def find(self, parent, i) :
        if parent[i] == -1 :
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, x, y) :
        
        xset = self.find(parent, x)
        yset = self.find(parent, y)
        
        if xset != yset :
            parent[xset] = yset
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        parent = [-1]*len(M)
        
        for i in range(len(M)) :
            for j in range(len(M)) :
                if M[i][j] == 1 and i != j :
                    self.union(parent, i, j)
        
        count = 0
        
        for i in parent :
            if i == -1 :
                count += 1
                
        return count
        
 
class Solution:
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        count = 0
        
        visited = [False]*len(M)
        queue = collections.deque([])
        
        for i in range(len(M)) :
            if not visited[i] :
                queue.append(i)
            
                while queue :
                    x = queue.popleft()
                    visited[x] = True
                    for j in range(len(M)) :
                        if M[x][j] == 1 and visited[j] == False :
                            queue.append(j)
                count += 1
                
        return count
        
