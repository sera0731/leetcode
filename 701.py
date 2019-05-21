# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iteration

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        curr = root
        
        while curr :
            
            if curr.val < val :
                if not curr.right :
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right
            else :
                if not curr.left :
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left
                
        return TreeNode(root.val)

# Recursion

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
       
        if not root :
            return TreeNode(val)
        
        if root.val < val :
            root.right = self.insertIntoBST(root.right, val)
        else :
            root.left = self.insertIntoBST(root.left, val)
            
        return root
        