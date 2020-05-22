# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root :
            return
        
        l = min(p.val, q.val)
        r = max(p.val, q.val)
        
        def helper(node) :
            
            if not node :
                return
            if node.val < l :
                return helper(node.right)
            if node.val > r :
                return helper(node.left)
            
            return node
            
        return helper(root)

# Iteration
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root :
            return
        
        l = min(p.val, q.val)
        r = max(p.val, q.val)
        
        while root :
            
            if root.val < l :
                root = root.right
            elif root.val > r :
                root = root.left
            else :
                return root
        
        return root
    
    