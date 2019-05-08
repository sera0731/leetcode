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
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root :
            return []
        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.ans.append(root.val)
        
        return self.ans
        
# Iterative      
class Solution:
    def postorderTraversal(self, root: TreeNode):
        
        if not root :
            return []
        
        postorder = []
        stack = [root]
        
        while stack :

            node = stack.pop()
            postorder.append(node.val)
            
            if node.left :
                stack.append(node.left)
                
            if node.right :
                stack.append(node.right)
                
        return postorder[::-1] 
    