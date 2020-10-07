# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive
class Solution:
    def dfs(self, node) :
        
        if not node :
            return TreeNode(self.val)
        
        if node.val < self.val :
            node.right = self.dfs(node.right)
        else :
            node.left = self.dfs(node.left)
            
        return node
        
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        self.val = val
        return self.dfs(root)

# Iterative
class Solution:
        
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root :
            return TreeNode(val)
        
        node = root
        
        while node :
            if node.val < val :
                if not node.right :
                    node.right = TreeNode(val)
                    break
                else :
                    node = node.right
            else :
                if not node.left :
                    node.left = TreeNode(val)
                    break
                else :
                    node = node.left
                
        return root
        
