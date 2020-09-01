# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root :
            return
        
        if key > root.val :
            root.right = self.deleteNode(root.right, key)
        elif key < root.val :
            root.left = self.deleteNode(root.left, key)
        else :
            
            if not root.left :
                return root.right
            else :
                
                node = root.left
                
                while node.right :
                    node = node.right
                
                root.val = node.val
                root.left = self.deleteNode(root.left, node.val)
                
        return root
    
