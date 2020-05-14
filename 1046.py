# Time complexity : O(NlogN)
# Space complexity : O(1), in Python, converting a list to a heap is done in-place.

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
		for i in range(len(stones)) :
			stones[i] *= -1
        
		heapq.heapify(stones)
        
		while len(stones) > 1 :
			y = heapq.heappop(stones)
			x = heapq.heappop(stones)
            
            if y != x :
				heapq.heappush(stones, y-x)
				
		return -stones[0] if stones else 0
                
