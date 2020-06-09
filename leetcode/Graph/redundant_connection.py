# Time complexity : O(N)
# Space complexity : O(N)

class Solution:
    def __init__(self) :
        self.parent = []
        
    def find(self, x) :
        
        while self.parent[x] != x :
            x = self.parent[x]
        return x
        
    def union(self, x, y) :
        
        x = self.find(x)
        y = self.find(y)
        
        if x == y :
            return False
        
        self.parent[y] = x
        return True
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        self.parent = [i for i in range(0, len(edges)+1)]
        
        for [u, v] in edges :
            if not self.union(u, v):
                return [u, v]
            
