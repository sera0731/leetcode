class Node :
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(Node)
        total = 0
        
        for course in prerequisites :
            _next, prev = course
            graph[prev].outNodes.append(_next)
            graph[_next].inDegrees += 1
            total += 1
            
        nodes = []
        
        for i, node in graph.items() :
            if node.inDegrees == 0 :
                nodes.append(i)
        
        removed = 0
        
        while nodes :
            
            node = nodes.pop()
            
            for _next in graph[node].outNodes :
                graph[_next].inDegrees -= 1
                removed += 1
                
                if graph[_next].inDegrees == 0 :
                    nodes.append(_next)
                    
        return True if removed == total else False
            
