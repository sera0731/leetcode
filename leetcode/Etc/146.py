# Time complexity : O(1)
# Space complexity : O(capacity)

class DNode() :
    def __init__(self) :
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
 
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.head = DNode()
        self.tail = DNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
		
	def add_node(self, node):
		node.prev = self.head
		node.next = self.head.next
		
		self.head.next.prev = node
		self.head.next = node
		
	def remove_node(self, node):
		_prev = node.prev
		_next = node.next
		
		_prev.next = _next
		_next.prev = _prev
		
	def move_to_head(self, node):
		self.remove_node(node)
		self.add_node(node)
		
	def pop_tail(self):
		_prev = self.tail.prev
		self.remove_node(_prev)
		return _prev
		
	def get(self, key) :
		node = self.cache.get(key, None)
		if not node :
			return -1
		
		self.move_to_head(node)
		return node.value
		
	def put(self, key, value) :
		node = self.cache.get(key, None)
		
		if not node :
			nnode = DNode()
			nnode.key = key
			nnode.value = value
			
			self.cache[key] = nnode
			self.add_node(nnode)
			
			if len(self.cache) > self.capacity :
				tail = self.pop_tail()
				del self.cache[tail.key]
		else :
			node.value = value
			self.move_to_head(node)
			
		
