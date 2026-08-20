# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        #slow moves by one, fast moves by two
        slow = head
        fast = slow.next.next

        while (fast is not None):
            if slow == fast:
                return True
            if fast.next is not None:
                fast = fast.next.next
                slow = slow.next
            else:
                fast = fast.next
        
        return False
        

        