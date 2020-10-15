class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        self.graph = collections.defaultdict(list)
        self.visited = [0] * numCourses
        
        for u, v in prerequisites :
            self.graph[u].append(v)
            
        for i in range(numCourses) :
            if not self.dfs(i) :
                return False
        
        return True

    def dfs(self, node) :
        
        if self.visited[node] == -1 :
            return False
        if self.visited[node] == 1 :
            return True
        
        self.visited[node] = -1
        
        for i in self.graph[node] :
            if not self.dfs(i) :
                return False
            
        self.visited[node] = 1
        return True
        
