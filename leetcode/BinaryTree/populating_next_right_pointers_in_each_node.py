"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Space complexity : O(N)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root :
            return
        
        q = collections.deque([root])
        
        while q :
            
            n = len(q)
            
            for i in range(n) :
                
                curr = q.popleft()
                
                if i < n-1 :
                    curr.next = q[0]
                
                if curr.left :
                    q.append(curr.left)
                if curr.right :
                    q.append(curr.right)
                
        return root
    
# Space complexity : O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root :
            return
        
        leftmost = root
        
        while leftmost.left :
            
            head = leftmost
            
            while head :
                
                head.left.next = head.right
                
                if head.next :
                    head.right.next = head.next.left
                
                head = head.next
                    
            leftmost = leftmost.left
                
        return root
