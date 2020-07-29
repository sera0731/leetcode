class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        last = [0]*26
        
        for i in range(len(S)) :
            last[ord(S[i]) - ord('a')] = i
        
        idx = last_idx = 0
        labels = []
        
        for i in range(len(S)) :
            
            ch = S[i]
            idx = max(idx, last[ord(ch)-ord('a')])
            
            if i == idx :
                labels.append(idx-last_idx+1)
                last_idx = idx + 1
                
        return labels

