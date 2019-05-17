# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        if not root or not p :
            return
        
        stack, curr = [], root
        found = False
        
        while stack or curr :
            
            if curr :
                stack.append(curr)
                curr = curr.left
            else :
                
                curr = stack.pop()
                
                if found :
                    return curr
                
                if p == curr :
                    found = True
                    
                curr = curr.right
                
        return

# Recursive

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        def helper(node) :
            
            if not node :
                return
            
            if node.val <= p.val :
                return helper(node.right)
            else :
                left = helper(node.left)
                return left if left else node
            
        return helper(root)
    

# Better way [O(h), where h is height of tree, O(1)]

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
       
        successor = None
    
        while root :
            if p.val < root.val :
                successor = root
                root = root.left
            else :
                root = root.right
            
        return successor
        