# Recursive
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        
        def helper(start, curr) :
        
            subsets.append(curr)
            
            for i in range(start, len(nums)) :
                helper(i+1, curr + [nums[i]])
            
        helper(0, [])
        return subsets
        
# Iterative
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = [[]]
        
        for i in nums :
            subsets += [ subset+[i] for subset in subsets ]
            
        return subsets
        
