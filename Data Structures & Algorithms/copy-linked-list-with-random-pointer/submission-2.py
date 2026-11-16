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
        # create an empty dict to store the input
        copies = {None: None}
        # starts at the orginial node
        current = head 

        # keep runnning until linked link is empty
        while current:
            # create a new node holding 3; new_node points to the new node
            copy = Node(current.val)
            copies[current] = copy
            current = current.next
        current = head
        while current:
            copy = copies[current]
            copy.next = copies[current.next]
            copy.random = copies[current.random]
            current = current.next
        return copies[head]