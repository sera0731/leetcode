class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        output = 0
        prev = 0
        
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        for start, end in intervals :
            
            if end > prev :
                output += 1
                prev = end
                
        return output
    
