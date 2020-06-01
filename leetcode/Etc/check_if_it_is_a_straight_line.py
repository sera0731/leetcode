# Time complexity : O(N)
# Space complexity : O(1)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        (x0, y0), (x1, y1) = coordinates[:2]
        
        for [x, y] in coordinates[2:] :
            if (x-x1)*(y1-y0) != (x1-x0)*(y-y1) :
                return False
        
        return True
      
