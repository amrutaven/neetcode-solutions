# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        #now slow is the midpoint
        first = head
        second = slow.next
        slow.next = None

        #reverse second linked list
        prev = None
        curr = second
        if second is not None:
            later = second.next
        else:
            return None

        while later is not None:
            curr.next = prev
            prev = curr
            curr = later
            later = later.next
        
        curr.next = prev
        second = curr

        #now merge them

        while first is not None and second is not None:
            first_holder = first.next
            second_holder = second.next

            first.next = second
            first = first_holder

            second.next = first
            second = second_holder



            











        
        