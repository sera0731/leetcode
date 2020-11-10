# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def helper(node, _min, _max) :
            
            if not node :
                return _max - _min
            
            _min = min(_min, node.val)
            _max = max(_max, node.val)
            
            left = helper(node.left, _min, _max)
            right = helper(node.right, _min, _max)
            
            return max(left, right)
            
        if not root :
            return 0
        
        return helper(root, root.val, root.val)
        
