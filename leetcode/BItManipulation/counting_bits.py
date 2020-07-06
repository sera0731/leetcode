class Solution:
    def countBits(self, num: int) -> List[int]:
        
        ans = [0]*(num+1)
        
        i = 0
        two = 1
        
        while two <= num :
            
            while i < two and two + i <= num :
                ans[two+i] = ans[i] + 1
                i += 1
            
            i = 0
            two <<= 1
        
        return ans
        
