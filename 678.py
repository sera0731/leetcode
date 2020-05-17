# Time complexity : O(N)
# Space complexity : O(N)

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left = []
        star = []
        
        for i in range(len(s)) :
            if s[i] == '(' :
                left.append(i)
            elif s[i] == '*' :
                star.append(i)
            else :
                if left :
                    left.pop()
                elif star :
                    star.pop()
                else :
                    return False
        
        while left and star :
            
            x = left.pop()
            y = star.pop()
            
            if y < x :
                return False
            
        return not left
        
# Time complexity : O(N)
# Space complexity : O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        cmax = cmin = 0
        
        for ch in s :
            
            if ch == '(' :
                cmax += 1
                cmin += 1
            elif ch == '*' :
                cmax += 1
                cmin = max(0, cmin-1)
            elif ch == ')' :
                cmax -= 1
                cmin = max(0, cmin-1)
                
            if cmax < 0 :
                return False
            
        return cmin == 0
        
