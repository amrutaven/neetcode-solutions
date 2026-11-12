# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        node1 = l1
        node2 = l2

        first = 0
        second = 0
        
        exponent = 0
        while (node1 != None):
            first += node1.val * pow(10, exponent)
            node1 = node1.next
            exponent += 1
        
        exponent = 0
        while (node2 != None):
            second += node2.val * pow(10, exponent)
            node2 = node2.next
            exponent += 1
        
        third = first + second

        new_head = ListNode((third % 10))
        copy = new_head
        digit = third % 10
        third = (third // 10)
        while (third > 0):
            copy.next = ListNode(third % 10)
            third = (third // 10)
            copy = copy.next
        
        return new_head

            


        