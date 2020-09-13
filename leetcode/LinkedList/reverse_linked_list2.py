# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if m == n :
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        for _ in range(m-1) :
            prev = prev.next
            
        _head = None
        tail = prev.next
        
        for i in range(n-m+1) :
            _next = tail.next
            tail.next = _head
            _head = tail
            tail = _next
        
        prev.next.next = tail
        prev.next = _head
        
        return dummy.next
        
            
