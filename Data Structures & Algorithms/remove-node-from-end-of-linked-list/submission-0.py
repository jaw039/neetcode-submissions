# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = head

        while n > 0:
            right = right.next
            # we want to get the nodes before one we want to remove
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        
        # skips our nth node that we want to remove 
        left.next = left.next.next
        return dummy.next