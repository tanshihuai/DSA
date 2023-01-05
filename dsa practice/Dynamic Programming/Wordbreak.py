class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = [False] * (len(s) + 1)
        memo[-1] = True

        for i in range(len(s)-1, -1, -1):
            for j in wordDict:
                if i + len(j) > len(s):
                    continue
                if s[i:i+len(j)] == j:
                    memo[i] = memo[i+len(j)]
                if memo[i]:         # if you found a match then break
                    break
        print(memo)
        return memo[0]


s = "cars"
wordDict = ["car","ca","rs"]

s1= Solution()
print(s1.wordBreak(s,wordDict))
