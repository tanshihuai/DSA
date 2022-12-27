class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        i = 0
        while i < len(s):
            if i == len(s)-1:
                sum += dict1[s[i]]
                return sum
            if dict1[s[i]] < dict1[s[i + 1]]:
                sum += dict1[s[i+1]] - dict1[s[i]]
                i += 1
            else:
                sum += dict1[s[i]]
            i += 1
        return sum

s = Solution()
print(s.romanToInt("LVIII"))