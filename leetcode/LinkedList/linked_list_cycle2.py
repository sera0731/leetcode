# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def helper(self, head) :
        
        fast = slow = head
        
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast :
                return slow
        
        return
        
    def detectCycle(self, head: ListNode) -> ListNode:
        
        inter = self.helper(head)
        if not inter :
            return
        
        while head != inter :
            head = head.next
            inter = inter.next
            
        return head
    
