class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        set1 = set()
        res = 0

        # right extends one by one, left snaps to no-repeat once right hits a repeat
        while right < len(s):
            while s[right] in set1:
                set1.remove(s[left])
                left += 1
            set1.add(s[right])
            res = max(len(set1), res)
            right += 1
        return res
