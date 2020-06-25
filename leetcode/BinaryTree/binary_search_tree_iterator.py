# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.q = queue.Queue()
        self.dfs(root)
        
    def dfs(self, node) :
        
        stack = []
        curr = node
        
        while True :
            
            if curr :
                stack.append(curr)
                curr = curr.left
            elif stack :
                curr = stack.pop()
                self.q.put(curr.val)
                curr = curr.right
            else :
                break

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.q.get()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.q.empty() == False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
