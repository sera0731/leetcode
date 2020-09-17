class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        p = [0, 0]
        
        cd = 0
        
        for i in instructions :
            if i == "G":
                r, c = d[cd%4]
                p[0] += r
                p[1] += c
            elif i == "L":
                cd += 1
            else :
                cd -= 1
                
        if p[0] == 0 and p[1] == 0 :
            return True
        
        return cd%4 != 0
            
        
