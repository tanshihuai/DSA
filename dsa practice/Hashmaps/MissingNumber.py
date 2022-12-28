class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        highest = max(nums)
        exist = set()
        for i in range(highest):
            exist.add(i)
        for i in nums:
            if i in exist:
                exist.remove(i)
        if exist:
            for i in exist: return i
        else:
            return highest + 1



nums = [9,6,4,2,3,5,7,0,1]
s = Solution()
print(s.missingNumber(nums))