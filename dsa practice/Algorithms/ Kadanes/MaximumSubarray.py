class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        global_max = nums[0]

        for i in nums[1:]:
            if i > i + curr_max:
                curr_max = i
            else:
                curr_max = i + curr_max

            if curr_max > global_max:
                global_max = curr_max

        return global_max

nums = [-2,1,-3,4,-1,2,1,-5,4]

s = Solution()
x = s.maxSubArray(nums)
print(x)