class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [0] * (len(nums) + 3)
        nums.append(0)

        for i in range(len(nums)-2, -1, -1):
            memo[i] = max(nums[i] + memo[i+2], nums[i+1] + memo[i+3])
        print(memo)
        return memo[0]


nums = [1,2,3,1]
s=Solution()
print(s.rob(nums))