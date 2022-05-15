'''
https://leetcode.com/problems/valid-parentheses/32. Longest Valid Parentheses
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''


class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop(-1)

    def isEmpty(self):
        if len(self.list) != 0:
            return False
        return True

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = Stack()
        if len(s) <2:
            return False
        for i in s:
            if i == '[':
                stack.push(']')
            elif i == '{':
                stack.push('}')
            elif i == '(':
                stack.push(')')
            elif stack.isEmpty() or stack.pop() != i:
                return False
        return stack.isEmpty()


str = "((("
s = Solution()
s.isValid(str)
