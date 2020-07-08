class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for ch in s :
            
            if ch == ']' :
                
                word = ''
                
                while stack :
                    
                    x = stack.pop()
                    
                    if x == '[' :
                        
                        x = stack.pop()
                        
                        digit = x
                        
                        while stack and stack[-1].isdigit() :
                            digit = stack.pop() + digit
                        
                        word = word * int(digit)
                        stack.append(word)
                        break
                        
                    word = x + word
                
            else :
                stack.append(ch)
                
        return ''.join(stack)
        
