# Time complexity : O(n)
# Space complexity : O(n)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        seen = set()
        
        while head :
            if head in seen :
                return True
            seen.add(head)
            head = head.next
            
        return False
        
