class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.range = 999
        self.buckets = [Bucket() for i in range(self.range)]
        
    def _hash(self, key) :
        return key % self.range

    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].insert(key)
        
    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = self._hash(key)
        return self.buckets[idx].exists(key)
    
class Node :
    def __init__(self, value, node=None):
        self.value = value
        self.next = node
        
class Bucket:
    def __init__(self):
        self.head = Node(0)
        
    def insert(self, value):
        if not self.exists(value) :
            node = Node(value, self.head.next)
            self.head.next = node
            
    def delete(self, value):
        
        prev = self.head
        curr = self.head.next
        
        while curr :
            if curr.value == value :
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
    
    def exists(self, value) :
        curr = self.head.next
        
        while curr :
            if curr.value == value :
                return True
            curr = curr.next
        
        return False
