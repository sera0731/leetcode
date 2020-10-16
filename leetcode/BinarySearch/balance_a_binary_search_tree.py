# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, nodes) :
        
        if not node :
            return
        
        self.inorder(node.left, nodes)
        nodes.append(node.val)
        self.inorder(node.right, nodes)
        
    def buildTree(self, arr) :
        
        if not arr :
            return
        
        i = len(arr)//2
        node = TreeNode(arr[i])
        node.left = self.buildTree(arr[:i])
        node.right = self.buildTree(arr[i+1:])
        
        return node
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nodes = []
        self.inorder(root, nodes)
        return self.buildTree(nodes)
        
