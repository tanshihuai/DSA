class Solution(object):
    def minWindow(self, s, t):
        import math
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
        l = 0
        r = 0
        dict1 = {}
        dict2 = {}
        min_count = math.inf
        res = ""

        def is_in(dict1, dict2):
            for i in dict2:
                if dict1.get(i, 0) < dict2[i]:
                    return False
            return True

        for i in t:
            dict2[i] = dict2.get(i, 0) + 1

        while r < len(s):
            dict1[s[r]] = dict1.get(s[r], 0) + 1
            while is_in(dict1, dict2):
                if (r - l + 1) < min_count:
                    min_count = (r - l + 1)
                    res = s[l:r+1]
                dict1[s[l]] = dict1[s[l]] - 1
                l += 1
            r += 1
        return res

s = "ADOBECODEBANC"
t = "ABC"

ss = Solution()
print(ss.minWindow(s,t))