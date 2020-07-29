# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        nodes = defaultdict(list)
        
        def build(parent, child) :
            
            if parent and child :
                nodes[parent.val].append(child.val)
                nodes[child.val].append(parent.val)
                
            if child.left :
                build(child, child.left)
            if child.right :
                build(child, child.right)
        
        build(None, root)
        
        queue = [target.val]
        seen = set(queue)
        
        for i in range(K) : 
            
            new_level = []
            
            for curr in queue :
                for j in nodes[curr] :
                    if j in seen :
                        continue
                    new_level.append(j)
            
            queue = new_level
            seen |= set(queue)
                
        return queue
        
