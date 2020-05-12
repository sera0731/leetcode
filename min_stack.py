# Time complexity : O(1)
# Space complexity : O(N)

class MinStack:

    def __init__(self):
        self._data = []

    def push(self, x: int) -> None:
        if not self._data :
            self._data.append((x, x))
            return
        self._data.append((x, min(x, self._data[-1][1])))

    def pop(self) -> None:
        self._data.pop()

    def top(self) -> int:
        return self._data[-1][0]
        
    def getMin(self) -> int:
        return self._data[-1][1]
        
