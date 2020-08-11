class Solution:
    def titleToNumber(self, s: str) -> int:
        
        m = { ch : ord(ch)-ord('A')+1 for ch in string.ascii_uppercase }
        num = 0
        
        for ch in s :
            num *= 26
            num += m[ch]
            
        return num
    
