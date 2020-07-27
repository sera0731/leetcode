# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        self.sum = 0
        
        def dfs(node) :
            
            if not node :
                return 0
            
            if L <= node.val <= R :
                self.sum += node.val
            if L < node.val :
                dfs(node.left)
            if node.val < R :
                dfs(node.right)
        
        dfs(root)
        return self.sum
            
# Iterative
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        stack = [root]
        range_sum = 0
        
        while stack :
            
            node = stack.pop()
            
            if not node :
                continue
                
            if L <= node.val <= R :
                range_sum += node.val
            if L < node.val :
                stack.append(node.left)
            if node.val < R :
                stack.append(node.right)
        
        return range_sum
                
