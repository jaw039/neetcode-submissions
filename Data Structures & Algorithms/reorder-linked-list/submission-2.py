# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # to find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # this disconnect our first half of the list and create a second linked list for us 
        # after we find the mid point and cut it in halves
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first,second = head, prev
        while second:  
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 
            first, second = tmp1, tmp2