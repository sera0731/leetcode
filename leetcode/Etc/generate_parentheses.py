class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        total = n * 2
        
        def helper(curr='', left=0, right=0) :
            
            if len(curr) == total :
                ans.append(curr)
                return
            
            if left < n :
                helper(curr + '(', left+1, right)
            
            if left > right :
                helper(curr + ')', left, right+1)
                
            return
        
        helper()       
        return ans
        
