class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_seq_length = 0
        set1 = set(nums)
        for i in nums:
            # is it start of sequence
            if i-1 not in set1:
                seq_length = 1
                while i+1 in set1:
                    i += 1
                    seq_length += 1
                max_seq_length = max(max_seq_length, seq_length)
        return max_seq_length


nums = [0,3,7,2,5,8,4,6,0,1]
s = Solution()
print(s.longestConsecutive(nums))
