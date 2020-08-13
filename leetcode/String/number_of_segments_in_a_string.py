# Space complexity : O(N)  
class Solution:
    def countSegments(self, s: str) -> int:
        
        if not s :
            return 0
        
        return len(s.split())
  
# Space complexity : O(1)  
class Solution:
    def countSegments(self, s: str) -> int:
        
        sgmt = 0
        
        for i in range(len(s)) :
            if (i == 0 or s[i-1] == ' ') and (s[i] != ' ') :
                sgmt += 1
            
        return sgmt
        
