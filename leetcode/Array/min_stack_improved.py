ELEM = 0
NUM = 1
    
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        
        self.stack.append(x)
        
        if not self.min_stack :
            self.min_stack.append([x, 1])
            return
        
        _min = self.min_stack[-1]
        
        if _min[ELEM] == x :
            self.min_stack[-1][NUM] += 1
        elif _min[ELEM] > x :
            self.min_stack.append([x, 1])
        
    def pop(self) -> None:
        
        if not self.stack :
            return
        
        last = self.stack.pop()
        
        if self.min_stack[-1][ELEM] == last :
            self.min_stack[-1][NUM] -= 1
            
            if self.min_stack[-1][NUM] == 0 :
                self.min_stack.pop()
        
        return last

    def top(self) -> int:
        if self.stack :
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack :
            return self.min_stack[-1][ELEM]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
