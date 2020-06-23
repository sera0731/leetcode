# Time complexity : O(N^2)
# Space complexity : O(N)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums or len(nums) < 3 :
            return
        
        ans = []
        nums.sort()
        
        for i in range(len(nums)-2) :
            
            if i == 0 or nums[i-1] != nums[i] :
                
                l, r = i+1, len(nums)-1
                value = -nums[i]
                
                while l < r :
                    result = nums[l] + nums[r]
                    if result < value or (l-1> i and nums[l] == nums[l-1]) :
                        l += 1
                    elif result > value or (r+1 < len(nums) and nums[r] == nums[r+1]) :
                        r -= 1
                    elif result == value :
                        ans.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    
        return ans
                 
