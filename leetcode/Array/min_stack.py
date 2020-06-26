ELEM = 0 
MIN = 1
    
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        
        _min = x
        
        if self.stack :
            _min = min(self.stack[-1][MIN], x)
            
        self.stack.append([x, _min])

    def pop(self) -> None:
        if self.stack :
            self.stack.pop()

    def top(self) -> int:
        if self.stack :
            return self.stack[-1][ELEM]

    def getMin(self) -> int:
        if self.stack :
            return self.stack[-1][MIN]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
