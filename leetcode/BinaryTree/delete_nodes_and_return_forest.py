# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, is_root=True) :
        
        if not node :
            return None
        
        deleted = True if node.val in self.nodes else False 
        
        if not deleted and is_root :
            self.forest.append(node)
                
        node.left = self.dfs(node.left, deleted)
        node.right = self.dfs(node.right, deleted)
        return None if deleted else node
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.forest = []
        self.nodes = set(to_delete)
        self.dfs(root)
        return self.forest
        
