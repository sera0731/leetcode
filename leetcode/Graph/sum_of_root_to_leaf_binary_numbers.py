# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        st = [(root, 0)]
        output = 0
        
        while st :
            
            node, curr = st.pop()
            curr = (curr << 1) | node.val
            
            if not (node.left or node.right) :
                output += curr
            
            if node.left :
                st.append((node.left, curr))
            
            if node.right :
                st.append((node.right, curr))
            
        return output
        
