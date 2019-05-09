# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self) :
        self.ans = 0
        
    def helper(self, node, parent) :
        
        if not node :
            return True
        
        left = self.helper(node.left, node.val)
        right = self.helper(node.right, node.val)
        
        if left and right :
            self.ans += 1
        
        return left and right and node.val == parent 
            
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        if not root :
            return 0
        
        self.helper(root, None)
        return self.ans
        