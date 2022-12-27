class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)

        if length % 2 != 0:
            middle_char = length // 2
            s.pop(middle_char)


