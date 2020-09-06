# Time complexity : O(N+M)
# Space complexity : O(N+M)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        stack1, stack2 = [], []
        output = []
        
        while root1 or root2 or stack1 or stack2 :
            
            while root1 :
                stack1.append(root1)
                root1 = root1.left
                
            while root2 :
                stack2.append(root2)
                root2 = root2.left
                
            if not stack1 or stack2 and stack2[-1].val <= stack1[-1].val :
                root2 = stack2.pop()
                output.append(root2.val)
                root2 = root2.right
            else :
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
                
        return output
        
