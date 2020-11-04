# Algorithm
# 1. Create a graph
# 2. Retrieve a graph from leaf nodes 
# 3. Trim the leaves until reaching the centroids (If the number of nodes is odd, 1 or else 2)

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2 :
            return [i for i in range(n)]
        
        graph = collections.defaultdict(set)
        
        for s, e in edges :
            graph[s].add(e)
            graph[e].add(s)
            
        q = collections.deque([])
        
        for i in range(n) :
            if len(graph[i]) == 1 :
                q.append(i)
        
        remaining = n
        while remaining > 2 :
            
            q_n = len(q)
            remaining -= q_n
            
            for _ in range(q_n) :
                
                curr = q.popleft()
                
                for neighbour in graph[curr] :
                    graph[neighbour].remove(curr)
                    if len(graph[neighbour]) == 1 :
                        q.append(neighbour)
                  
        return q
    
