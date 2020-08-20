class Node :
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 1000
        self.buckets = [None]*(self.n)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        i = key % self.n
        
        if not self.buckets[i] :
            self.buckets[i] = Node(key, value)
            return
        
        curr = self.buckets[i]
        
        while True :
            
            if curr.key == key :
                curr.value = value
                return
            
            if curr.next == None :
                break
                
            curr = curr.next
                
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % self.n
        curr = self.buckets[i]
        
        while curr :
            if curr.key == key :
                return curr.value
            curr = curr.next
        
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % self.n
        
        if not self.buckets[i] :
            return
        
        curr = self.buckets[i]
        
        if curr.key == key :
            self.buckets[i] = curr.next
            return
        
        prev = curr
        
        while curr :
            if curr.key == key :
                prev.next = curr.next
                return
            else :
                prev = curr
                curr = curr.next
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
