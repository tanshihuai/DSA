class Solution(object):


    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob1(nums):
            if len(nums) == 1:
                return nums[0]
            memo = [0] * (len(nums))
            memo[0] = nums[0]
            memo[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                memo[i] = max(memo[i-1], nums[i] + memo[i-2])
            print(memo)
            return memo[-1]
        if len(nums) == 1:
            return nums[0]
        return max(rob1(nums[:-1]), rob1(nums[1:]))

nums = [1,3,1,3,100]
s = Solution()
print(s.rob(nums))
