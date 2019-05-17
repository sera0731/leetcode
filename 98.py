# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root :
            return True
        
        stack = []
        
        limit = float("-inf")
        curr = root
        
        while stack or curr :
            
            if curr :
                stack.append(curr)
                curr = curr.left
            else :
                curr = stack.pop()
                
                # 방문
                if limit >= curr.val :
                    return False
                
                limit = curr.val
                curr = curr.right
                
        return True
                
# Recursive

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root :
            return True
        
        def helper(node, lower=float("-inf"), upper=float("inf")) :
            
            if not node :
                return True
            
            val = node.val
            
            if lower >= val or upper <= val :
                return False
            
            isValid = helper(node.left, lower, val) and helper(node.right, val, upper)
            
            return isValid
    
        return helper(root)
        