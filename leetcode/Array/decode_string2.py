class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        num = 0
        encoded_str = ''
        
        for ch in s :
            if ch.isdigit() :
                num = num*10 + int(ch)
            elif ch == '[' :
                stack.append(encoded_str)
                stack.append(num)
                num = 0
                encoded_str = ''
            elif ch != ']' :
                encoded_str += ch
            else :
                last_num = stack.pop()
                last_str = stack.pop()
                
                encoded_str = last_str + encoded_str*last_num
                
        return encoded_str
    
