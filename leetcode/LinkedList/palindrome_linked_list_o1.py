# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node) :
        
        prev = None
        
        while node :
            _next = node.next
            node.next = prev
            prev = node
            node = _next
            
        return prev
        
    def isPalindrome(self, head: ListNode) -> bool:
        
        fast = slow = head
        
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
            
        if fast :
            slow = slow.next
        
        rvsd_node = self.reverse(slow)
            
        while rvsd_node :
            
            if head.val != rvsd_node.val :
                return False
            
            rvsd_node = rvsd_node.next
            head = head.next
            
        return True
           
