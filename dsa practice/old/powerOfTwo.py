import math

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n < 1:
            return False
        else:
            return self.isPowerOfTwo(n/2)



s = Solution()
print(s.isPowerOfTwo(6))
