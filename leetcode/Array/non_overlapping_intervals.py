class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals :
            return 0
        
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        
        end = intervals[0][1]
        valid = 1
        
        for i in range(1, n) :
            if intervals[i][0] >= end :
                end = intervals[i][1]
                valid += 1
                
        return n - valid
    
