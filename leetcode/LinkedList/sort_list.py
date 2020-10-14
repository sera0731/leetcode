# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Space complexity : O(N)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        nodes = []
        
        while head :
            nodes.append(head)
            head = head.next
        
        if not nodes :
            return
        
        nodes.sort(key=lambda x: x.val)
        
        for i in range(len(nodes)-1) :
            nodes[i].next = nodes[i+1]
        
        nodes[-1].next = None
        
        return nodes[0]

# Space complexity : O(1)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next :
            return head
        
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
        
    def merge(self, left, right) :
        
        dummy = ListNode()
        tail = dummy
        
        while left and right :
            
            if left.val < right.val :
                tail.next = left
                left = left.next
            else :
                tail.next = right
                right = right.next
            
            tail = tail.next
        
        tail.next = left if left else right
        return dummy.next
        
    def getMid(self, node) :
        
        slow = node
        fast = node.next
        
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        
        head = slow.next
        slow.next = None
        
        return head
        
