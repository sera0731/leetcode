# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        stack = []
        fast = slow = head
        
        while fast and fast.next :
            
            stack.append(slow.val)
            
            fast = fast.next.next
            slow = slow.next
            
        if fast :
            slow = slow.next
            
        while slow :
            
            x = stack.pop()
            if x != slow.val :
                return False
            slow = slow.next
            
        return True
        
