class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        left = 0
        right = len(height)-1
        while True:
            vol = (right - left) * min(height[left], height[right])
            max_vol = vol if vol > max_vol else max_vol

            if right - 1 == left:
                return max_vol
            else:
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1



height = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(height))