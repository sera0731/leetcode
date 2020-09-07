# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        self.ans = '~'
        
        def dfs(node, A) :
            
            if not node :
                return
            
            A.append(chr(node.val+ ord('a')))
            if not (node.left or node.right) :
                self.ans = min(self.ans, ''.join(reversed(A)))
            
            dfs(node.left, A)
            dfs(node.right, A)
            A.pop()
            
        dfs(root, [])
        return self.ans
        
