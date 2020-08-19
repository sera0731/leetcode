class Solution:
    def reorganizeString(self, S: str) -> str:
        
        nums = collections.defaultdict(int)
        
        for ch in S :
            nums[ch] += 1
            
        n = len(S)
        if max(nums.values()) > (n+1)//2 :
            return ""
        
        heap = []
        output = []
        
        for ch, i in nums.items() :
            heapq.heappush(heap, (-i, ch))
            
        while len(heap) > 1 :
            
            fi, fch = heapq.heappop(heap)
            si, sch = heapq.heappop(heap)
            
            output.append(fch)
            output.append(sch)
                
            if fi+1 :
                heapq.heappush(heap, (fi+1, fch))
            if si+1 :
                heapq.heappush(heap, (si+1, sch))
                    
        if heap :
            li, lch = heapq.heappop(heap)
            output.append(lch)
            
        return ''.join(output)
            
