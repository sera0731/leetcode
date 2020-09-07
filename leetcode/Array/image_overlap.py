class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        posa = []
        posb = []
        
        for i in range(len(A)) :
            for j in range(len(A[0])) :
                if A[i][j] == 1 :
                    posa.append((i, j))
                if B[i][j] == 1 :
                    posb.append((i, j))
                    
        output = 0
        count = collections.defaultdict(int)
        
        for a in posa :
            for b in posb :
                d = (a[0]-b[0], a[1]-b[1])
                count[d] += 1
                output = max(output, count[d])
                
        return output
        
