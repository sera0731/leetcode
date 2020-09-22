# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def helper(node, sum=0) :
            
            if not node :
                return sum
            
            node.val += helper(node.right, sum)
            return helper(node.left, node.val)
            
        helper(root)
        return root
        
