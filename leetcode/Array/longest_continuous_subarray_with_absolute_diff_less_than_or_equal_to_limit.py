import collections

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        l = longest = 0
        min_queue, max_queue = deque(), deque()
        
        for r in range(len(nums)) :
            
            while max_queue and max_queue[-1] < nums[r] :
                max_queue.pop()
            while min_queue and min_queue[-1] > nums[r] :
                min_queue.pop()
            
            max_queue.append(nums[r])
            min_queue.append(nums[r])
            
            while max_queue[0] - min_queue[0] > limit :
                if max_queue[0] == nums[l] :
                    max_queue.popleft()
                if min_queue[0] == nums[l] :
                    min_queue.popleft()
                
                l += 1
                
            longest = max(r-l+1, longest)
            
        return longest
    
