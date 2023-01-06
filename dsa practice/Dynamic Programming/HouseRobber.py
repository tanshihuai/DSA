class Solution(object):
    def rob(self, nums):
        '''O(n) space complexity because store all values in memo array'''
        memo = [0] * (len(nums) + 3)
        nums.append(0)

        for i in range(len(nums)-2, -1, -1):
            memo[i] = max(nums[i] + memo[i+2], nums[i+1] + memo[i+3])
        print(memo)
        return memo[0]

    def improvedRob(self,nums):
        '''O(1) space complexity because store only needed varaibles'''
        prev1 = prev2 = maxRob = 0
        for i in range(len(nums)):
            maxRob = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = maxRob
        return maxRob


nums = [1,2,3,1]
s=Solution()
print(s.improvedRob(nums))