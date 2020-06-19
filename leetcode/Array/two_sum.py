class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i in range(len(nums)) :
            
            delta = target - nums[i]
            
            if delta in dic :
                return [dic[delta], i]
            
            dic[nums[i]] = i
            
        return -1
