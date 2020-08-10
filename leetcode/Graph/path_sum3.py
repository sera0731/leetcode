# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, curr, target) :
            
        if not node :
            return
            
        curr += node.val
            
        if curr == target :
            self.count += 1
            
        self.count += self.m[curr-target]
        self.m[curr] += 1
            
        self.dfs(node.left, curr, target)
        self.dfs(node.right, curr, target)
            
        self.m[curr] -= 1
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        self.count = 0
        
        self.m = collections.defaultdict(int)
        self.dfs(root, 0, sum)
        
        return self.count
        
