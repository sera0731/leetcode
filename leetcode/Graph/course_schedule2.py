import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.graph = defaultdict(list)
        self.visited = [0]*numCourses # 0 = not visited, 1 = visited, -1 = visiting
        self.output = []
        
        for a, b in prerequisites :
            self.graph[a].append(b)
            
        for i in range(numCourses) :
            if not self.dfs(i) :
                return []
        
        return self.output
    
    def dfs(self, node) :
        
        if self.visited[node] == 1 :
            return True
        
        if self.visited[node] == -1 :
            return False
        
        self.visited[node] = -1
        
        for i in self.graph[node] :
            if not self.dfs(i) :
                return False
        
        self.visited[node] = 1
        self.output.append(node)
        
        return True
    
