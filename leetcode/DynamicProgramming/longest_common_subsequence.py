class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if len(text1) < len(text2) :
            text1, text2 = text2, text1
        
        n = len(text2)
        prev = [0]*(n+1)
        
        for i in range(len(text1)) :
            
            current = [0]*(n+1)
            
            for j in range(len(text2)) :
                # The first letter of each string is the same
                if text1[i] == text2[j] :
                    current[j] = 1 + prev[j-1]
                # The first letter of each string is different
                else :
                    current[j] = max(current[j-1], prev[j])
                    
            prev = current
            
        return prev[n-1]
        
