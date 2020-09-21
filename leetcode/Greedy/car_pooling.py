class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        ts = []
        
        for num, start, end in trips :
            ts.append([start, num])
            ts.append([end, -num])
            
        ts.sort()
        current = 0
        
        for t, num in ts :
            current += num
            if current > capacity :
                return False
        
        return True
        
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        n = max(trips, key=lambda x : x[2])[2] + 1
        ts = [0] * n
        
        for num, start, end in trips :
            ts[start] += num
            ts[end] -= num
        
        curr = 0
        
        for t in ts :
            curr += t
            if curr > capacity :
                return False
        
        return True
    
