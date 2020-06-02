# Time complexity : O(N+E)
# Space complexity : O(N)

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        degrees = [0]*(N+1)
        
        for x, y in trust :
            degrees[y] += 1
            degrees[x] -= 1
            
        for i in range(1, N+1) :
            if degrees[i] == N-1 :
                return i
        
        return -1
        
