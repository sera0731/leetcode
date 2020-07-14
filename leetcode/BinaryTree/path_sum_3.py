# Recursive
class Solution:
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        self.ans = 0
        
        def traverse(node, target) :
            
            if not node :
                return
            
            test(node, target)
            traverse(node.left, target)
            traverse(node.right, target)
            
        def test(node, target):
            
            if not node :
                return
            
            if node.val == target :
                self.ans += 1

            test(node.left, target-node.val)
            test(node.right, target-node.val)
            
        traverse(root, sum)
        return self.ans
        
# Optimized        
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        self.nop = 0
        cache = {0:1}
        
        self.dfs(root, sum, 0, cache)
        return self.nop
    
    def dfs(self, node, target, currPathSum, cache) :
        
        if not node :
            return
        
        currPathSum += node.val
        oldPathSum = currPathSum - target
        
        self.nop += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        self.dfs(node.left, target, currPathSum, cache)
        self.dfs(node.right, target, currPathSum, cache)
        
        cache[currPathSum] -= 1
        
