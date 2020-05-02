# Time complexity : O(n)
# Space complexity : O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      
      lastNonZero = 0
      
      for i in range(len(nums)) :
        if nums[i] != 0 :
          nums[i], nums[lastNonZero] = nums[lastNonZero], nums[i]
          lastNonZero += 1
          
