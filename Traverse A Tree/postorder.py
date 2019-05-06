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
        
        stack, output = [root], []
        
        while stack :
            current = stack.pop()
            output.append(current.val)
            
            if current.left :
                stack.append(current.left)
            if current.right :
                stack.append(current.right)
                
        return output[::-1] 
    