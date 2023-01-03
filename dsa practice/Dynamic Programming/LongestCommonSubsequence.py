class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        memo = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]



        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    memo[i][j] = memo[i+1][j+1] + 1
                else:
                    memo[i][j] = max(memo[i][j+1], memo[i+1][j])
        return memo[0][0]

t1 = "abcde"
t2 = "ace"
s = Solution()
print(s.longestCommonSubsequence(t1, t2))

