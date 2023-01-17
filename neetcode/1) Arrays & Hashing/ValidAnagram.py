class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        left = {}
        right = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if left.get(s[i]) is not None:
                left[s[i]] += 1
            else:
                left[s[i]] = 1

            if right.get(t[i]) is not None:
                right[t[i]] += 1
            else:
                right[t[i]] = 1

        print(left)
        print(right)
        return(left == right)

s = "anagram"
t = "nagaram"
so = Solution()
print( so.isAnagram(s,t) )

