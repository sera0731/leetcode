# Space complexity : O(N)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head :
            return
        
        nodes = []
        curr = head
        
        while curr :
            nodes.append(curr)
            curr = curr.next
            
        n = len(nodes)
        curr = nodes[0]
        
        for i in range(1, n//2+1) :
            
            last = n-i
            
            curr.next = nodes[last]
            curr = curr.next
            
            curr.next = nodes[i]
            curr = curr.next
            
        curr.next = None
        
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head :
            return
        
        slow = fast = head
        
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        prev, curr = None, slow
        
        while curr :
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        
        first, second = head, prev
        
        while second.next :
            first.next, first = second, first.next
            second.next, second = first, second.next
            
