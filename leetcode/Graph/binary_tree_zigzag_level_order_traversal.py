# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root :
            return []
        
        reverse = True
        q = deque([root])
        output = [[root.val]]
        
        while q :
            
            n = len(q)
            level = deque([])
            
            for _ in range(n) :
                node = q.popleft()
                for i in [node.left, node.right] :
                    if i :
                        q.append(i)
                        if reverse :
                            level.appendleft(i.val)
                        else :
                            level.append(i.val)
                            
            if level :
                output.append(level)
                
            reverse = not reverse
            
        return output
        
