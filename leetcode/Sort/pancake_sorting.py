class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        
        def flip(k) :
            i = 0
            while i < k // 2 :
                A[i], A[k-i-1] = A[k-i-1], A[i]
                i += 1
        
        output = []
        target = len(A)
        
        while target > 0 :
            
            i = A.index(target)
            
            if i != target - 1 :
                
                if i != 0 :
                    output.append(i+1)
                    flip(i+1)
                    
                output.append(target)
                flip(target)
                
            target -= 1
        
        return output
