class Solution:
    def longestMountain(self, A: List[int]) -> int:
        
        n = len(A)
        if n < 3 :
            return 0
        
        start = output = 0
        while start < n :
            
            end = start
            # increasing
            if end+1 < n and A[end] < A[end+1] :
                while end+1 < n and A[end] < A[end+1] : end += 1
            
                # decreasing
                if end+1 < n and A[end] > A[end+1] :
                    while end+1 < n and A[end] > A[end+1] : end += 1
                    output = max(output, end-start+1)
                    
                start = end
            else :
                start += 1
            
        return output
        
