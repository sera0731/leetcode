import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        output = 0
        events.sort()
        heap = []
        
        n = len(events)
        day = 0
        i = 0
        
        while heap or i < n :
            
            if not heap :
                day = events[i][0]
            
            while heap and heap[0] < day :
                heappop(heap)
                
            while i < n and events[i][0] == day :
                heappush(heap, events[i][1])
                i += 1
            
            if heap :
                heappop(heap)
                day += 1
                output += 1
                
        return output
    
        
