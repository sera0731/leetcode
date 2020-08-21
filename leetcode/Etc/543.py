# Time complexity : O(N)
# Space complexity : O(N)

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.ans = 0
        
        def depth(node) :
            
            if not node :
                return 0
            
            L = depth(node.left)
            R = depth(node.right)
            
            self.ans = max(self.ans, L+R)
            return max(L, R)+1
            
        depth(root)
        return self.ans
            
