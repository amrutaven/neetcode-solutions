"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {None : None}
        curr = head

        #first pass -> create all the new nodes
        while (curr != None):
            new_node = Node(curr.val)
            node_dict[curr] = new_node

            curr = curr.next

        
        #second pass -> connect the nodes together for the random part

        curr = head

        while (curr != None):
            node_dict[curr].next = node_dict[curr.next]
            if curr.random == None:
                node_dict[curr.random] = None

            else: 
                node_dict[curr].random = node_dict[curr.random]

            curr = curr.next
        
        return node_dict[head]




 
        

        