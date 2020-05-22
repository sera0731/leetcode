# 743. Network Delay Time

import heapq

class Solution : 
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
      
      graph = collections.defaultdict(list)
      
      # Create a graph
      for u, v, w in times :
        graph[u].append((v, w))
      
      pq = [(0, K)]
      
      # Assign to every node a tentative distance value
      dist = {i: float('inf') for i in range(1, N+1)}
      
      # Keep track of visited nodes
      visited = set()
      
      while pq :
      
        # Peak the node which has the smallest distance
        (d, node) = heapq.heappop(pq)
        
        # Skip if it is the visited node
        if node in visited :
          continue
          
        visited.add(node)
        dist[node] = d
        
        if len(visited) == N :
            return max(dist.values())
        
        # Visit neighbours of the current node
        for v, d2 in graph[node] :
          
          # If it is faster to visit the neighbour node through the current node, add newly calculated distance and the neighbour node to the heap.
          if dist[v] > d + de :
            heapq.heappush(pq, (d+d2, v))
            
      # Return the maximum value if we visited all nodes
      return max(dist.values()) if len(visited) == N else -1
