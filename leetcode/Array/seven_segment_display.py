class Solution :
    def __init__(self) :
        self.segments = [6,2,5,5,4,5,6,3,7,5]
        
    def computeSegment(self, n) :
        
        if n == 0 :
            return self.segments[0]
        
        sgmt = 0
        
        while n > 0 :
            sgmt += self.segments[n%10]
            n //= 10
            
        return sgmt
        
    def elementMinSegment(self, input) :
        
        minSeg = float('inf')
        minIdx = float('inf')
        
        for i in input :
            curr = self.computeSegment(i)
            if minSeg > curr :
                minSeg = curr
                minIdx = i
            
        return minIdx
        
