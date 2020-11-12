class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            
        def dfs(nums, i):
            
            if i == len(nums):
                output.append(nums[:])
                return
            
            seen = set()
            for j in range(i, len(nums)):
                
                if nums[j] in seen :
                    continue
                
                nums[i], nums[j] = nums[j], nums[i]
                dfs(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]
                seen.add(nums[j])
                
        output = []
        dfs(nums, 0)
        return output
    
