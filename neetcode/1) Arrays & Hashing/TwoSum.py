class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums)):
            toFind = target - nums[i]
            if dict1.get(toFind) is not None:
                return [i, dict1[toFind]]
            else:
                dict1[nums[i]] = i


nums = [3,3]
target = 6

s = Solution()
print(s.twoSum(nums, target))