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
        
        inorder = []
        stack = []
        
        node = root
        
        while stack or node :
            
            while node :
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
            
        return inorder
        