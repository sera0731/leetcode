# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root :
            return []
        
        Q = deque([root])
        output = []
        
        while Q :
            
            level = []
            
            for i in range(len(Q)) :
                
                node = Q.popleft()
                level.append(node.val)
                
                for child in [node.left, node.right] :
                    if child :
                        Q.append(child)
                        
            output.append(level)
            
        return output
                