# Memoization
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def dfs(i=0) :
            
            if memo[i] != None :
                return memo[i]
            
            _next = min(len(nums), i+nums[i]+1)
            
            for j in range(i+1, _next) :
                if dfs(j) :
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False
            
        memo = [None]*len(nums)
        memo[-1] = True
        
        return dfs()

# Dynamic programming
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        memo = [False]*n
        memo[-1] = True
        
        for i in range(n-2, -1, -1) :
            _next = min(n, i+nums[i]+1)
            for j in range(i+1, _next) :
                if memo[j] == True :
                    memo[i] = True
                    break
        
        return memo[0]
    
# Greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = target = len(nums)-1
        
        for i in range(n-1, -1, -1) :
            if i + nums[i] >= target :
                target = i
        
        return target is 0
    
