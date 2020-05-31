# Time complexity : O(N)
# Space complexity : O(N)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = {}
        target = len(nums) // 2
        
        for n in nums :
            dic[n] = dic.get(n, 0) + 1
            if dic[n] > target:
                    return n
           
