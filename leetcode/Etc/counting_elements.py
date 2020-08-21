# Time complexity : O(N)
# Space complexity : O(N)

class Solution:
    def countElements(self, arr: List[int]) -> int:
       
       hashset = set(arr)
       answer = 0
       
       for num in arr :
          if num+1 in hashset :
              answer += 1
              
       return answer
