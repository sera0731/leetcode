# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root :
            return []
        
        queue = deque([root])
        rights = []
        
        while queue :
            
            n = len(queue)
            
            for i in range(n) :
                node = queue.popleft()
                
                if i == n-1 :
                    rights.append(node.val)
                
                if node.left :
                    queue.append(node.left)
                    
                if node.right :
                    queue.append(node.right)
                    
        return rights
                   
