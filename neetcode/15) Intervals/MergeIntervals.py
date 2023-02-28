class Solution:
    def merge(self, intervals):

        intervals = sorted(intervals)
        for i in range(len(intervals) - 1):
            if intervals[i][1] >= intervals[i + 1][0]:
                if intervals[i + 1][1] < intervals[i][1]:
                    intervals[i + 1] = intervals[i]
                    intervals[i] = [-1, -1]
                else:
                    intervals[i + 1][0] = intervals[i][0]
                    intervals[i] = [-1, -1]

        ans = []

        for i in intervals:
            if i != [-1, -1]:
                ans.append(i)
        return ans

input = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
print(s.merge(input))