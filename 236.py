# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root, p, q) :
        
        if root == p or root == q :
            return root
        
        l = r = None
        
        if root.left :
            l = self.helper(root.left, p, q)
            
        if root.right :
            r = self.helper(root.right, p, q)
        
        if l and r :
            return root
        
        return l or r
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root :
            return
        
        return self.helper(root, p, q)
        