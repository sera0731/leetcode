class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        last = {}
        
        for i, ch in enumerate(S) :
            last[ch] = i
        
        output = []
        start = end = 0
        
        for i, ch in enumerate(S) :
            
            end = max(last[ch], end)
            
            if i == end :
                output.append(i-start+1)
                start = i+1
                
        return output
    
