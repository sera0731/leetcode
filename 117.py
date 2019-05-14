"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root :
            return
        
        Q = deque([root])
        
        while Q :
            
            before = Q.popleft()
            lenQ = len(Q)
            
            for child in [before.left, before.right] :
                if child :
                    Q.append(child)
                    
            for i in range(lenQ) :
                 
                current = Q.popleft()
                before.next = current
                
                for child in [current.left, current.right] :
                    if child :
                        Q.append(child)
                
                before = current
                
        return root
        