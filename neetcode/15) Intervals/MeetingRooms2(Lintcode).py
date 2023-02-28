class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals):
        # Write your code here
        open_room = sorted([i[0] for i in intervals])
        close_room = sorted([i[1] for i in intervals])

        count = 0
        maxcount = 0
        o_ptr = 0
        c_ptr = 0

        # go to the next event happening. If event is opening room, count + 1.
        # if event is closing room, count - 1.
        # you can return once all opening room events are over
        while o_ptr != len(open_room):
            if open_room[o_ptr] < close_room[c_ptr]:
                count += 1
                maxcount = max(maxcount, count)
                o_ptr += 1
            else:
                count -= 1
                c_ptr -= 1
        return maxcount



input = [(2,7),(7,10)]


s = Solution()
print(s.min_meeting_rooms(input))