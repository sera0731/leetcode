class Node :
    def __init__(self, key=0, value=0) :
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.cache = {}
        
        self.head = Node(0)
        self.tail = Node(0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        
        node = self.cache.get(key, None)
        
        if not node :
            return -1
        
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        
        node = self.cache.get(key, None)
        
        if not node :
            new_node = Node(key, value)
            self.add_head_node(new_node)
            self.cache[key] = new_node
            
            if len(self.cache) > self.capacity :
                tail = self.remove_tail_node()
                del self.cache[tail.key]
                
        else :
            node.value = value
            self.move_to_head(node)
            
    def add_head_node(self, node: Node) :
        
        prev = self.head.next
        prev.prev = node
        
        node.next = prev
        node.prev = self.head
        
        self.head.next = node
        
    def move_to_head(self, node: Node) :
        
        prev = node.prev
        _next = node.next
        
        prev.next = _next
        _next.prev = prev
        
        self.add_head_node(node)
        
    def remove_tail_node(self) :
        
        prev = self.tail.prev
        
        pprev = prev.prev
        pprev.next = self.tail
        
        self.tail.prev = pprev
        
        return prev
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
