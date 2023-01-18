class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(nums, target):
            l = 0
            r = len(nums)-1
            for i in range(len(nums)):
                if l >= r:
                    return[]
                if nums[l] + nums[r] == target:
                    return [nums[l], nums[r]]
                else:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1

        ans = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            target = 0 - sorted_nums[i]
            ts = twoSum(sorted_nums[:i] + sorted_nums[i+1:], target)
            if ts:
                ans.append( ts + [sorted_nums[i]])

        ans2 = []
        ans = sorted([sorted(i) for i in ans])
        for i in range(len(ans)):
            if i == 0 or ans[i] != ans[i-1]:
                ans2.append(ans[i])
        return ans2

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
s = Solution()
print(s.threeSum(nums))