# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:

    @lru_cache(maxsize=None)
    def cachedKnows(self, a, b) :
        return knows(a, b)
    
    def findCelebrity(self, n: int) -> int:
        
        candidate = 0
        
        for i in range(1, n) :
            if self.cachedKnows(candidate, i) :
                candidate = i
                
        if self.isCelebrity(candidate, n) :
            return candidate
        
        return -1
        
    def isCelebrity(self, i, n) :
        
        for j in range(n) :
            if i == j : continue
            if self.cachedKnows(i, j) or not self.cachedKnows(j, i) :
                return False
        
        return True
        
