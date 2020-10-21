class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        
        op = '+'
        curr = 0
        
        for i, ch in enumerate(s) :
            
            if ch.isnumeric() :
                curr = curr*10 + int(ch)
            
            if ch in '+-*/' or i == len(s)-1 :
                
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '/':
                    x = stack.pop()
                    res = abs(x)//curr*(1 if x>0 else -1)
                    stack.append(res)
                elif op == '*':
                    stack.append(stack.pop()*curr)
                    
                curr = 0
                op = ch
        
        return sum(stack)
        
