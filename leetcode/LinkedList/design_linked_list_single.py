class Node :
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.size = 0
        
    def getNode(self, index: int) -> int:
        
        if index == -1 :
            return self.head
        
        if index >= self.size :
            return
        
        curr = self.head.next
        
        while index > 0 and curr :
            curr = curr.next
            index -= 1
            
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
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        prev = self.getNode(index-1)
        new_node = Node(val)
        
        if prev :
            curr = prev.next
            new_node.next = curr
            prev.next = new_node
            self.size += 1
            
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        prev = self.getNode(index-1)
        
        if prev :
            curr = prev.next
            if curr :
                prev.next = curr.next
                self.size -= 1
                

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
