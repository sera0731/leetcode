import collections
class Solution:
    def helper(self, v, visited, stack) :
        
        if visited[v] == 1 :
            return True
        if visited[v] == -1 :  # cycle detected
            return False
        
        visited[v] = -1
        
        for i in self.graph[v] :
            if not self.helper(i, visited, stack) :
                return False
            
        visited[v] = 1
        stack.append(v)
        
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if not numCourses :
            return []
        
        self.graph = defaultdict(list)
        
        for u, v in prerequisites :
            self.graph[u].append(v)
        
        stack = []
        visited = [0]*numCourses
        
        for i in range(numCourses) :
            if not self.helper(i, visited, stack) :
                return []
                
        return stack
        
        
        
