# Time complexity : O(logN)
# Space complexity : O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        l = 2
        r = x//2
        
        while l <= r :
            
            mid = l + (r-l)//2
            num = mid*mid
            
            if num == x :
                return mid
            elif num < x :
                l = mid+1
            else :
                r = mid-1
                
        return r
