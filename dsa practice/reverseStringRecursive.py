class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return s
        else:
            left = s[:len(s)//2]
            right = s[len(s)//2:]
            return self.reverseString(right) + self.reverseString(left)


sa = ['h','e','l','l','o']

s = Solution()
print(s.reverseString(sa))