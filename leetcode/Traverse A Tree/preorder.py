# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
class Solution:
    def __init__(self) :
        self.ans = []
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root :
            return []
        
        self.ans.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        
        return self.ans
        
# Iterative
class Solution:
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root :
            return []
        
        preorder = []
        stack = [root]
        
        while stack :
            
            node = stack.pop()
            preorder.append(node.val)
            
            if node.right :
                stack.append(node.right)
                
            if node.left :
                stack.append(node.left)
            
        return preorder
    