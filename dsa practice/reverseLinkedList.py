'''
https://leetcode.com/problems/reverse-linked-list/
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev