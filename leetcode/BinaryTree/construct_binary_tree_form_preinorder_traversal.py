# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def helper(l, r) :
            
            nonlocal i
            
            if l > r or i == len(preorder) :
                return
            
            val = preorder[i]
            node = TreeNode(val)
            mid = idx[val]
            
            i += 1
            
            node.left = helper(l, mid-1)
            node.right = helper(mid+1, r)
            
            return node
        
        i = 0
        idx = { num: i for i, num in enumerate(inorder)}
        
        return helper(0, len(preorder)-1)
    
