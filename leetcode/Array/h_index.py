# O(NlogN)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if not citations :
            return 0
        
        citations.sort()
        n = len(citations)
        
        for i in range(n) :
            # at least n-i citations
            if citations[i] >= n-i :
                return n-i
        
        return 0
    
# O(N)  
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        papers = [0]*(n+1) # i = 몇 번 참조, v = 몇 개
        
        for i in range(n) :
            papers[min(citations[i], n)] += 1
        
        # c => [1, 3, 2, 3, 100]
        # papers => [0, 1, 1, 2, 0, 1]
        
        h = n
        s = papers[h]
        
        while h > s :
            h -= 1
            s += papers[h]
            
        return h
        
