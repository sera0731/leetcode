# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class BSTIterator:
        
    def __init__(self, root: TreeNode):
        self.nodes = []
        self.left_most(root)
    
    def left_most(self, node) :
        
        while node :
            self.nodes.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        if not self.hasNext() :
            return
        
        curr = self.nodes.pop()
        self.left_most(curr.right)
        
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
