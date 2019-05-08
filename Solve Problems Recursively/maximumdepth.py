# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root :
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right)+1
       
# Iterative
 
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root :
            return 0
        
        Q = deque([root])
        depth = 0
        
        while Q :
            
            for i in range(len(Q)) :
                node = Q.popleft()
                for child in [node.left, node.right] :
                    if child :
                        Q.append(child)
                        
            depth += 1
            
        return depth
