class Node :
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0

    def getNode(self, index) :
        
        if index == -1 :
            return self.head
        if index >= self.size :
            return
        
        remain = self.size-index
        
        # Find from the beginning
        if remain > index :
            curr = self.head.next
            for i in range(index) :
                curr = curr.next
        # Find from the end
        else :
            curr = self.tail.prev
            for i in range(remain-1) :
                curr = curr.prev
                
        return curr
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        node = self.getNode(index)
        return node.val if node else -1
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        
        new_node = Node(val)
        
        _next = self.head.next
        _next.prev = new_node
        
        new_node.next = _next
        new_node.prev = self.head
        
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        
        prev = self.tail.prev
        prev.next = new_node
        
        new_node.next = self.tail
        new_node.prev = prev
        
        self.tail.prev = new_node
        
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        prev = self.getNode(index-1)
        new_node = Node(val)
        
        if prev :
            curr = prev.next
            
            curr.prev = new_node
            prev.next = new_node
            
            new_node.next = curr
            new_node.prev = prev
            
            self.size += 1
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr = self.getNode(index)
        
        if curr :
            prev = curr.prev
            _next = curr.next
            
            if prev :
                prev.next = _next
                _next.prev = prev
            
                self.size -= 1
            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
