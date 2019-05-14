# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root :
            return ""
        
        def helper(node) :
            
            if not node :
                output.append("X")
            else :
                output.append(str(node.val))
                helper(node.left)
                helper(node.right)
            
        output = []
        helper(root)
        
        return ",".join(output)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data :
            return
        
        def helper() :
            
            if not data :
                return
            
            node = data.popleft()
            
            if node == "X":
                return
            
            root = TreeNode(int(node))
            root.left = helper()
            root.right = helper()
            
            return root
        
        data = deque(data.split(","))
        return helper()
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))