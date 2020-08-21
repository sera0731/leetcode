# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def helper(self, preorder, inorder) :
        
        if not preorder or not inorder :
            return
        
        root = TreeNode(preorder.popleft())
        i = inorder.index(root.val)
        
        root.left = self.helper(preorder, inorder[:i])
        root.right = self.helper(preorder, inorder[i+1:])
        
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder or not inorder :
            return
        
        return self.helper(deque(preorder), inorder)
        
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def helper(l, r) :
            
            nonlocal i
            
            if l == r :
                return
            
            root = TreeNode(preorder[i])
            mid = D[root.val]
            
            i += 1
            
            root.left = helper(l, mid)
            root.right = helper(mid+1, r)
            
            return root
        
        i = 0
        D = { v: idx for idx, v in enumerate(inorder) }
        
        return helper(0, len(inorder))
        