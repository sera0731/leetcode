import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = queue.Queue()
        self.qtop = -1

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.put(x)
        self.qtop = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        n = self.queue.qsize()
        
        if n == 0 :
            return
        
        if n == 1 :
            self.qtop = None
            return self.queue.get()
            
        for i in range(n-2) :
            self.queue.put(self.queue.get())
            
        self.qtop = self.queue.get()
        self.queue.put(self.qtop)
        
        return self.queue.get()
        
    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queue.qsize() > 0:
            return self.qtop
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
