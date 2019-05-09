# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive

class Solution:
    def helper(self, root, sum) :
        
        if not root :
            return False
        
        sum -= root.val
        
        if not root.left and not root.right :
            return sum == 0
        
        return self.helper(root.left, sum) or self.helper(root.right, sum)
        
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root and sum :
            return False
        
        return self.helper(root, sum)

# Iterative

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root :
            return False
        
        stack = [(root, sum)]
        
        while stack :
            
            node, current = stack.pop()
            current -= node.val
            
            if not any([node.left, node.right, current]) :
                return True
                
            if node.left :
                stack.append((node.left, current))
            
            if node.right :
                stack.append((node.right, current))
                
        return False
                