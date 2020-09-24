class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        n = len(arr)
        zeros = arr.count(0)
        
        for i in range(n-1, -1, -1) :
            
            if i + zeros < n :
                arr[i+zeros] = arr[i]
                
            if arr[i] == 0 :
                zeros -= 1
                if i + zeros < n :
                    arr[i+zeros] = arr[i]
                    
