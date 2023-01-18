class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict1 = {}
        ans = []

        for i in nums:
            if dict1.get(i):
                dict1[i] += 1
            else:
                dict1[i] = 1

        x = sorted(dict1.items(), key=lambda item: item[1])
        print(x)
        for i in range(len(x)-1, len(x)-k-1, -1):
            ans.append(x[i][0])
        return ans



nums = [1,1,1,2,2,3]
s = Solution()
print(s.topKFrequent(nums, 2))