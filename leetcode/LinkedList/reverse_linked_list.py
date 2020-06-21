# Time complexity : O(n)
# Space complexity : O(n)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    
        if not head :
            return
        
        prev, curr = None, head
        
        while curr :
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
            
        return prev
            
