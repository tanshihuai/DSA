class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cleaned_s = "".join(i for i in s if i.isalnum()).lower()
        l = 0
        r = len(cleaned_s) - 1
        while l<r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l += 1
            r -= 1
        return True


string = "ra R"
s = Solution()
print(s.isPalindrome(string))