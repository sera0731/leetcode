class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        ni = newInterval
        
        for i, v in enumerate(intervals) :
            if v[1] < ni[0] :
                output.append(v)
            elif v[0] > ni[1] :
                output.append(ni)
                return output + intervals[i:]
            else :
                ni[0] = min(ni[0], v[0])
                ni[1] = max(ni[1], v[1])
        
        output.append(ni)
        return output
        
