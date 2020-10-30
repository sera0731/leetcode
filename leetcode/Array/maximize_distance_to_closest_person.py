class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        output = 1
        prev = -1
        
        for i, s in enumerate(seats) :
            if s :
                if prev != -1 :
                    output = max(output, (i-prev)//2)
                else :
                    output = i
                prev = i
        
        output = max(output, len(seats)-1-prev)
        return output
        
