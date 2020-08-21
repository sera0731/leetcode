#
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#

class Solution(object):
  def singleNumber(self, nums):
  
      a = 0
      for i in nums:
        a ^= i
        
      return a

# Bit Manipulation
# If we take XOR of zero and some bit, it will return that bit
#  ex. a ⊕ 0 = a
# If we take XOR of two same bits, it will return 0
#  ex. a ⊕ a = 0
# So we can XOR all bits together to find the unique number.
