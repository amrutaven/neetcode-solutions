# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # logic = find the size, size - n - 1 is the node before the one that needs to be removed

        size = 0

        mover = head

        while (mover is not None):
            mover = mover.next
            size += 1

        mover = head
        
        num_to_move = size - n - 1

        #if the head needs to be removed
        if num_to_move == -1:
            return head.next

        while (num_to_move != 0 and mover is not None):
            mover = mover.next
            num_to_move -= 1
        
        if mover is None:
            return None
        
        curr = mover
        target = mover.next
        later = target.next
        target.next = None
        curr.next = later


        return head

        