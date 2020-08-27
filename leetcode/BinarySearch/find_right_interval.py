class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        idx = {}
        n = len(intervals)
        
        for i in range(n) :
            idx[tuple(intervals[i])] = i
            
        intervals.sort()
        output = [0]*n
        
        for i in range(n):
            start, end = intervals[i]
            index = self.binarySearch(end, i+1, n, intervals)
            
            if index == n :
                output[idx[tuple(intervals[i])]] = -1
            else :
                output[idx[tuple(intervals[i])]] = idx[tuple(intervals[index])]
                
        return output
            
            
    def binarySearch(self, target, left, right, intervals) :
        
        while left < right :
            mid = left + (right-left)//2
            if intervals[mid][0] >= target :
                right = mid
            else :
                left = mid + 1
        return left
        
        
