class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
       
        D = {}
    
        for i in range(len(nums)) :
        
            diff = target - nums[i]
        
            if diff in D :
                return [i, D[diff]]
        
            D[nums[i]] = i
        
        return [0,0]
        
    