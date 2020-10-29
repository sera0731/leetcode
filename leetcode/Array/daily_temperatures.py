class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        output = [0]*len(T)
        stack = []
        
        for i, x in enumerate(T) :
            
            while stack and T[stack[-1]] < x :
                ci = stack.pop()
                output[ci] = i-ci
                
            stack.append(i)
            
        return output
        
        
