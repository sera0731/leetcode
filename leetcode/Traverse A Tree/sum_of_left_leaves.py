# Recursive
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def dfs(node, left) :
            
            if not node :
                return 0
            
            if left and not (node.left or node.right) :
                return node.val
            
            return dfs(node.left, True) + dfs(node.right, False)
           
        return dfs(root, False)
        
# Iterative
class Solution:
    def isLeafNode(self, node) :
        return node and not (node.left or node.right)
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if not root :
            return 0
        
        stack = [root]
        output = 0
        
        while stack :
            sub_root = stack.pop()
            
            if self.isLeafNode(sub_root.left) :
                output += sub_root.left.val
                
            if sub_root.right :
                stack.append(sub_root.right)
            
            if sub_root.left :
                stack.append(sub_root.left)
                
        return output
    
