class Solution(object):
    def canJump(self, nums):
        goal = len(nums) -1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

s = Solution()
print(s.canJump([4,0,0,0,0,1]))