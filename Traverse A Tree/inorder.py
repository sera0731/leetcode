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
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root :
            return []
        
        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.ans
        
# Iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root :
            return []
        
        stack = []
        inorder = []
        
        current = root
        
        while stack or current :
            
            while current :
                stack.append(current)
                current = current.left
                
            if stack :
                current = stack.pop()
                
            inorder.append(current.val)
            current = current.right
            
        return inorder
        