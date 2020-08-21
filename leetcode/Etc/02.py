# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        head = current = ListNode(0)
        
        while l1 or l2 or carry :
            
            total = 0
            
            if l1 :
                total += l1.val
                l1 = l1.next
            
            if l2 :
                total += l2.val
                l2 = l2.next
            
            total += carry
            total, carry = total%10, total//10
            
            current.next = ListNode(total)
            current = current.next
            
        return head.next
    