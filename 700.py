# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root :
            return

        if root.val == val :
            return root
        elif root.val < val :
            return self.searchBST(root.right, val)
        
        return self.searchBST(root.left, val)

# Iterative

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        while root and root.val != val :
            
            if root.val < val :
                root = root.right
            else :
                root = root.left
                
        return root