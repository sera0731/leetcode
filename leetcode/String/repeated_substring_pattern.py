class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        n = len(s)
        gap = n // 2
        
        while gap > 0 :
            
            prev = s[:gap]
            success = True
            
            for j in range(gap, n, gap) :
                if prev != s[j:j+gap] :
                    success = False
                    break
                    
            if success :
                return True
                
            gap -= 1
        
        return False
            
