class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.store = collections.deque([])
        self.size = size
        self.window_sum = 0

    def next(self, val: int) -> float:
        
        tail = 0
        
        if len(self.store) == self.size :
            tail = self.store.popleft()
        
        self.store.append(val)
        self.window_sum = self.window_sum - tail + val
        
        return self.window_sum / len(self.store)
  
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
