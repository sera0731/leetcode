# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        
        st = [root]
        lonely = []
        
        while st :
            
            node = st.pop()
            
            if node.left :
                st.append(node.left)
                if not node.right :
                    lonely.append(node.left.val)
                    
            if node.right :
                st.append(node.right)
                if not node.left :
                    lonely.append(node.right.val)
                    
        return lonely
    
