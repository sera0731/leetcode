"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # DFS
    def __init__(self):
        self.nodes = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node :
            return node
        
        if node in self.nodes :
            return self.nodes[node]
        
        clone = Node(node.val, [])
        self.nodes[node] = clone
        
        if node.neighbors :
            clone.neighbors = [self.cloneGraph(i) for i in node.neighbors]
        
        return clone
    
    # BFS
    def cloneGraphBFS(self, node: 'Node') -> 'Node':
        
        if not node :
            return node
        
        nodes = {}
        nodes[node] = Node(node.val, [])
        
        queue = collections.deque([node])
        
        while queue :
            curr = queue.popleft()
            for i in curr.neighbors :
                if i not in nodes :
                    nodes[i] = Node(i.val, [])
                    queue.append(i)
                nodes[curr].neighbors.append(nodes[i])
                
        return nodes[node]
    
