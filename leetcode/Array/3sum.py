class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        if not nums :
            return output
        
        nums.sort()
        
        i = 0
        n = len(nums)
        
        for i in range(n-2) :
            
            if i != 0 and nums[i-1] == nums[i] :
                continue
            
            l = i+1
            r = n-1
            
            while l < r :
                
                res = nums[l] + nums[r] + nums[i]
                
                if res == 0 :
                    output.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1
                    
                    while l<r and nums[l] == nums[l-1] : l += 1
                    while l<r and nums[r] == nums[r+1] : r -= 1
                        
                elif res < 0 :
                    l += 1
                else :
                    r -= 1
                
        return output
                
