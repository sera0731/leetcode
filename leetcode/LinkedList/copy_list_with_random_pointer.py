"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head :
            return
        
        ohead = head
        nhead = Node(head.val)
        
        visited = {}
        visited[ohead] = nhead
        
        while ohead :
            
            if ohead.next :
                if ohead.next not in visited :
                    visited[ohead.next] = Node(ohead.next.val)
                nhead.next = visited[ohead.next] 
                
            if ohead.random :
                if ohead.random not in visited :
                    visited[ohead.random] = Node(ohead.random.val)
                nhead.random = visited[ohead.random]
            
            ohead = ohead.next
            nhead = nhead.next
        
        return visited[head]
            
