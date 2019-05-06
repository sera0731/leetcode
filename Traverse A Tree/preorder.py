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
        stack = []
        
        current = root
        
        while stack or current :
            
            while current :
                stack.append(current)
                preorder.append(current.val)
                current = current.left
            
            if stack :
                current = stack.pop()
                
            current = current.right
            
        return preorder
