# Time complexity : O(logN)
# Space complexity : O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2 :
            return True
        
        l, r = 2, num//2
        
        while l <= r :
            
            mid = l+(r-l)//2
            calculated = mid * mid
            
            if calculated == num :
                return True
            elif calculated < num :
                l = mid + 1
            else :
                r = mid - 1
            
        return False
        
