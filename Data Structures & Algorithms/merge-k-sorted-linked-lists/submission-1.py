# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]
        
        #keep merging the lists, 
        while (len(lists) > 1): 
            merged_lists = []
            #(start, stop, step)
            for i in range(0, len(lists), 2):
                first = lists[i]

                if i + 1 < len(lists):
                    second = lists[i + 1]
                else:
                    second = None

                combined = self.mergeTwoLists(first, second)
                merged_lists.append(combined)
            
            lists = merged_lists

    
        return lists[0]



    def mergeTwoLists (self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
            
        if list1 is not None:
                curr.next = list1
        else:
            curr.next = list2
            
        
        return dummy.next
        

    

        