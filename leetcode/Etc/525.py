# Time Complexity : O(N)
# Space Complexity : O(N)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        if not nums :
            return 0
        
        max_len, current = 0, 0
        counts = {0 : -1}
        
        for i in range(len(nums)) :
            current += 1 if nums[i] else -1
                
            if current in counts :
                max_len = max(max_len, i-counts[current])
            else :
                counts[current] = i
        
        return max_len
        
