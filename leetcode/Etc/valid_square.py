class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        length = lambda a, b : (a[1]-b[1])**2 + (a[0]-b[0])**2
        
        dist = collections.defaultdict(int)
        points = [p1, p2, p3, p4]
        
        for i in range(len(points)) :
            for j in range(i+1, len(points)) :
                dist[length(points[i], points[j])] += 1
                
        return 4 in dist.values() and 2 in dist.values()
    
