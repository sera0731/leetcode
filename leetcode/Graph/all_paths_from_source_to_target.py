class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        output = []
        q = collections.deque([(0, [0])])
        n = len(graph)
        
        while q :
            
            i, path = q.popleft()
            
            if i == n-1 :
                output.append(path)
            else :
                for x in graph[i] :
                    q.append((x, path+[x]))
        
        return output
            
