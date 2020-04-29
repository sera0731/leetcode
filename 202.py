class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n != 1 :
            res = 0
            while n > 0 :
                tmp = n % 10
                res += tmp ** 2
                n = n // 10
            if res in seen :
                return False
            n = res
            seen.add(n)
            
        return True
