# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):

        second = first = head

        for i in range(n):
            first = first.next

        flag = False
        while first:
            if flag is False:
                first = first.next
            else:
                first = first.next
                second = second.next
                flag = True

        if second.next:
            second.next = second.next.next
            return head
        else:
            return None

