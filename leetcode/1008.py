# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity : O(N)
# Space complexity : O(N)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        if not preorder:
            return []
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in range(1, len(preorder)) :
            
            node = stack[-1]
            child = TreeNode(preorder[i])            
            
            while stack and stack[-1].val < child.val :
                node = stack.pop()
                
            if child.val < node.val :
                node.left = child
            else :
                node.right = child
                
            stack.append(child)
            
        return root
            
            
        
