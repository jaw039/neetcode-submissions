# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        dummy = ListNode()
        tail = dummy

        curr1 = list1
        while curr1:
            result.append(curr1.val)
            curr1 = curr1.next
            
        curr2 = list2
        while curr2:
            result.append(curr2.val)
            curr2 = curr2.next

        result.sort()
        for value in result:
            tail.next = ListNode(value)
            tail = tail.next

        return dummy.next