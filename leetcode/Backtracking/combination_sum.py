class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(csum, t, i) :
            
            if t == 0 :
                ans.append(csum)
                return
            
            if i == len(candidates) :
                return
            
            for j in range(i, len(candidates)) :
                if candidates[j] <= t :
                    dfs(csum+[candidates[j]], t - candidates[j], j)
            
        ans = []
        dfs([], target, 0)
        return ans
        
