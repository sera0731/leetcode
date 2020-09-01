class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        output = -1
        
        def helper(start, curr) :
            
            nonlocal output
            
            if start == len(A) :
                h = curr[0]*10 + curr[1]
                m = curr[2]*10 + curr[3]
                
                if h <= 23 and m <= 59 :
                    output = max(output, h*60+m)
                return
            
            for i in range(start, len(A)) :
                A[i], A[start] = A[start], A[i]
                helper(start+1, A)
                A[i], A[start] = A[start], A[i]
         
        helper(0, A)
        return '' if output == -1 else '{:02d}:{:02d}'.format(output//60, output%60)
        
