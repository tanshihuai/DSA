class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [1] * len(nums)
        for i in range(len(memo)-2, -1, -1):
            for j in range(i+1, len(memo)):
                memo[i] = max(memo[j]+1, memo[i]) if nums[i] < nums[j] else memo[i]
        print(memo)
        return max(memo)

nums = [10,9,2,5,3,7,101,18]

s = Solution()
print(s.lengthOfLIS(nums))


