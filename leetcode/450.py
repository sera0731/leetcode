# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSuccessor(self, node) :
        
        while node and node.left :
            node = node.left
            
        return node
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root :
            return
        
        if root.val == key :
            
            if not root.left :
                return root.right
            if not root.right :
                return root.left
            
            # find successor
            successor = self.findSuccessor(root.right)
            
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
            
            return root
        
        if root.val < key :
            root.right = self.deleteNode(root.right, key)
        else :
            root.left = self.deleteNode(root.left, key)
            
        return root