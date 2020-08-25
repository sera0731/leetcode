class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        heap = []
        
        for i in A :
            heapq.heappush(heap, i)

        while K :
            heapq.heappush(heap, -heapq.heappop(heap))
            K -= 1

        return sum(heap)
            
