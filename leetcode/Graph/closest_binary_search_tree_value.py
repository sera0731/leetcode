# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        if not root :
            return
        
        def dfs(node) :
            
            nonlocal ans
            
            if not node :
                return
            
            if abs(target-node.val) < abs(target-ans) :
                ans = node.val
                
            dfs(node.left)
            dfs(node.right)
        
        ans = root.val
        dfs(root)
        
        return ans
        
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
    
        if not root :
            return
            
        closest = root.val
        
        while root :
            closest = min(root.val, closest, key = lambda x: abs(target-x))
            root = root.left if target < root.val else root.right
            
        return closest
    
