# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        if not root :
            return []
        
        output = []
        q = collections.deque([root])
        output.append([root.val])
        
        while q :
            
            n = len(q)
            level = []
            
            for _ in range(n) :
                
                node = q.popleft()
                
                for current in [node.left, node.right] :
                    if current :
                        q.append(current)
                        level.append(current.val)
            
            if level :
                output.append(level)
        
        return output[::-1]
        
