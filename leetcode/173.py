# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(N) space
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.nodes = []
        self.i = 0
        self.init_nodes(root)
        
    # Iterative
    def init_nodes(self, root) :
        
        stack = []
        curr = root
        
        # Inorder Traverse
        while stack or curr :
            
            if curr :
                stack.append(curr)
                curr = curr.left
            else :
                curr = stack.pop()
                self.nodes.append(curr.val)
                curr = curr.right

    # Recursive
     def init_nodes(self, root) :
        
        if not root :
            return
        
        self.init_nodes(root.left)
        self.nodes.append(root.val)
        self.init_nodes(root.right)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        if self.hasNext() :
            node = self.nodes[self.i]
            self.i += 1
            return node
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        
        return self.i < len(self.nodes)
        
# O(h) space

class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.nodes = []
        self.init_nodes(root)
        
    def init_nodes(self, root) :
        
        while root :
            self.nodes.append(root)
            root = root.left
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        if not self.hasNext() :
            return None
        
        curr = self.nodes.pop()
        self.init_nodes(curr.right)
            
        return curr.val
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        
        return len(self.nodes) > 0
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()