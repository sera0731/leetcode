class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        diff = float('inf')
        n = len(nums)
        
        nums.sort()
        
        for i in range(n-2) :
            
            l, r = i+1, n-1

            while l < r :
                
                curr = nums[i] + nums[l] + nums[r]
                
                if curr < target :
                    l += 1
                else :
                    r -= 1
                
                if abs(target-curr) < abs(diff) :
                    diff = target-curr
                    
            if diff == 0 :
                break
                    
        return target-diff
    
