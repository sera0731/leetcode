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
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node :
            return node
        
        nodes = {}
        nodes[node] = Node(node.val)
        
        q = collections.deque([node])
        
        while q :
            curr = q.popleft()
            
            for child in curr.neighbors :
                if child not in nodes :
                    nodes[child] = Node(child.val)
                    q.append(child)
                nodes[curr].neighbors.append(nodes[child])
                
        return nodes[node]
            
