class LRUCache:

    def __init__(self, capacity: int):
        
        self.dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        
        if key not in self.dict :
            return -1
        
        value = self.dict.pop(key)
        self.dict[key] = value
        
        return value

    def put(self, key: int, value: int) -> None:
        
        if self.get(key) == -1 :
            
            self.dict[key] = value
            
            if len(self.dict) > self.capacity :
                self.dict.popitem(last=False)
            
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
