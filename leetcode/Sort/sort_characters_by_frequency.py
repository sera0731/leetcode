# Heap
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        
        heap = []
        freq = collections.Counter(s)
        
        for i, v in freq.items() :
            heappush(heap, (-v, i))
        
        ans = []
        
        while heap :
            f, ch = heappop(heap)
            ans.append(ch*-f)
            
        return "".join(ans)
        
# Built-in sort
class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = collections.Counter(s)
        sorted_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        return "".join([freq*ch for ch, freq in sorted_list])
        
