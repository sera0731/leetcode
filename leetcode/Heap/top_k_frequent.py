# Heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        m = collections.Counter(nums)
        
        for i in m.keys() :
            heapq.heappush(heap, (-m[i], i))
        
        output = []
        
        for i in range(k) :
            a = heapq.heappop(heap)
            output.append(a[1])
            
        return output
            
# Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = collections.Counter(nums)
        n = max(count.values())
        
        bucket = [[] for i in range(n+1)]
        
        for i in count.keys() :
            bucket[count[i]].append(i)
        
        output = []
        
        for i in reversed(range(len(bucket))) :
            
            if len(output) == k :
                break
                
            current = bucket[i]
            
            for j in current :
                output.append(j)
                if len(output) == k :
                    break
            
        return output
            
