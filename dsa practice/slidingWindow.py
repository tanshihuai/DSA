class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        answer = []
        window = [nums[i] for i in range(k)]
        m = max(window)
        answer.append(m)
        for i in range(len(nums) - k):
            if nums[i] == m:
                m = max(nums[i+1: i+k+1])
            elif nums[i+k] > m:
                m = nums[i+k]
            answer.append(m)

        return answer

nums = [1,3,1,2,0,5]
s = Solution()
print(s.maxSlidingWindow(nums, 3))