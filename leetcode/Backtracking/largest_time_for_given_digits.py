class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        output = -1
        
        def helper(start=0) :
            
            nonlocal output
            
            if start == len(A) :
                h = A[0]*10 + A[1]
                m = A[2]*10 + A[3]
                
                if h <= 23 and m <= 59 :
                    output = max(output, h*60+m)
                return
            
            for i in range(start, len(A)) :
                A[i], A[start] = A[start], A[i]
                helper(start+1)
                A[i], A[start] = A[start], A[i]
         
        helper()
        return '' if output == -1 else '{:02d}:{:02d}'.format(output//60, output%60)
        
