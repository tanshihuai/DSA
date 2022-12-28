class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0,1,2]
        for i in range(3, n+1):
            permutation = memo[i-1] + memo[i-2]
            memo.append(permutation)
        return memo[n]

s = Solution()
print(s.climbStairs(3))