class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def helper(start, remain, curr) :
            
            if len(curr) == k and remain == 0 :
                self.ans.append(curr)
                return
            
            for i in range(start, 10) :
                if remain-i >= 0 :
                    helper(i+1, remain-i, curr+[i])
        
        self.ans = []
        helper(1, n, [])
        
        return self.ans
        
