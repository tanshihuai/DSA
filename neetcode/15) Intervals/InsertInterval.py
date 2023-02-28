class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        res = []
        for i in range(len(intervals)):
            # newnode is before i
            if newInterval[1] < intervals[i][0]:       # if newnode ends before i starts
                res.append(newInterval)
                return res + intervals[i:]

            # newnode is after i
            if intervals[i][1] < newInterval[0]:       # if i ends before newnode starts
                res.append(intervals[i])

            # newnode and interval intersects somewhere
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        res.append(newInterval)             # edgecase where newnode is the last element and has yet to be  added
        return res


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
n = [4,8]
s = Solution()
print(s.insert(intervals, n))