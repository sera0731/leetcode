# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive

class Solution:
    
    def helper(self, n1, n2) :
        
        if not n1 and not n2 :
            return True
        
        if not n1 or not n2 :
            return False
        
        if n1.val != n2.val :
            return False
        
        return self.helper(n1.left, n2.right) and self.helper(n1.right, n2.left)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root :
            return True
        
        return self.helper(root.left, root.right)
        

# Iterative

from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root :
            return True
        
        Q = deque([root, root])
        
        while Q :
            
            n1 = Q.popleft()
            n2 = Q.popleft()
                
            if not n1 and not n2 :
                continue
            elif not n1 or not n2 :
                return False
            elif n1.val != n2.val :
                return False
            
            Q.append(n1.left)
            Q.append(n2.right)
            Q.append(n1.right)
            Q.append(n2.left)
            
        return True
        