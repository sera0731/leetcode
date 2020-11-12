# Recursive + Memoization
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def helper(curr, last) :
            
            if curr == len(nums) :
                return 0
            
            if memo[last][curr] != None :
                return memo[last][curr]
            
            include = 0
            if last < 0 or nums[curr] > nums[last] :
                include = 1 + helper(curr+1, curr)
                
            exclude = helper(curr+1, last)
            
            memo[last][curr] = max(include, exclude)
            return memo[last][curr]
            
        n = len(nums)
        memo = [[None]*n for i in range(n+1)]
        return helper(0, -1)
    
# DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums :
            return 0
        
        n = len(nums)
        output = 1
        
        dp = [0]*n
        dp[0] = 1
        
        for i in range(1, n) :
            
            curr = 0
            
            for j in range(i) :
                if nums[i] > nums[j] :
                    curr = max(curr, dp[j])
                    
            dp[i] = curr + 1
            output = max(output, dp[i])
                    
        return output

# DP + Binary Search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        size = 0
        n = len(nums)
        tail = [0]*n
        
        for x in nums :
            
            l, r = 0, size
            while l != r :
                m = (l+r)//2
                if tail[m] < x :
                    l = m+1
                else :
                    r = m
                    
            tail[l] = x
            size = max(size, l+1)
                
        return size
    
