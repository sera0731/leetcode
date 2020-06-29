class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        m = {}
        
        for word in words :
            m[word] = m.get(word, 0) + 1
        
        h = []
        
        for key, value in m.items() :
            heapq.heappush(h, (-value, key))
            
        ans = []
        
        for _ in range(k) :
            ans.append(heapq.heappop(h)[1])
            
        return ans
            
            
        
