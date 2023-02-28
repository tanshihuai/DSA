

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals) -> bool:
        # Write your code here
        end = 0
        intervals = sorted(intervals)
        for i in intervals:
            if end > i[0]:
                return False
            end = i[1]
        return True


input = [(1,3),(3,5)]
s = Solution()
print(s.can_attend_meetings(input))
