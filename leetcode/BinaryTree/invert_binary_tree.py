# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(node) :
            
            if not node :
                return
            
            right = dfs(node.right)
            left = dfs(node.left)
            
            node.left = right
            node.right = left
            
            return node
            
        return dfs(root)
# BFS     
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root :
            return
        
        queue = collections.deque([root])
        
        while queue :
            
            node = queue.popleft()
            
            left = node.left
            right = node.right
            
            node.right = left
            node.left = right
            
            if left :
                queue.append(node.right)
                
            if right :
                queue.append(node.left)
            
        return root
