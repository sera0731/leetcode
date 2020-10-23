# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def build(l, r):
            
            if l > r :
                return
            
            mid = (r-l)//2+l
            node = TreeNode(nums[mid])
            
            node.left = build(l, mid-1)
            node.right = build(mid+1, r)
            
            return node
        
        return build(0, len(nums)-1)
        
