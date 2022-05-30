class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_water_level = max(height)
        head = 0
        tail = len(height) -1     # 6
        vol = 0

        for water_level in range(0, max_water_level+1):
            while height[head] < water_level:
                head += 1
            while height[tail] < water_level:
                tail -= 1
            curr_vol = water_level * (tail - head)
            if vol < curr_vol:
                vol = curr_vol

        return vol


arr = [1,8,6,2,5,4,8,3,7]

s = Solution()
print(s.maxArea(arr))





