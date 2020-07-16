class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
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
    
