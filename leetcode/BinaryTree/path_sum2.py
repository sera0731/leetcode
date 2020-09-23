# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        def helper(node, s, curr) :
            
            if not node :
                return
            
            s -= node.val
            curr.append(node.val)
            
            if s == 0 and not node.left and not node.right :
                self.ans.append(curr[:])
            else :
                helper(node.left, s, curr)
                helper(node.right, s, curr)
            
            curr.pop()
        
        self.ans = []
        helper(root, sum, [])
        return self.ans
        
