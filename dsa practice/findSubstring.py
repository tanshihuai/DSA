class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        if len(needle) > len(haystack): return -1

        length = len(needle)
        needle = list(needle)
        window = [haystack[i] for i in range(length)]


        for i in range(len(haystack) - length + 1):
            if window == needle:
                return i
            elif i == len(haystack) - length:
                return -1
            else:
                window.pop(0)
                window.append(haystack[i+length])



haystack = "aaa"
needle = "v"
s = Solution()
print(s.strStr(haystack, needle))
