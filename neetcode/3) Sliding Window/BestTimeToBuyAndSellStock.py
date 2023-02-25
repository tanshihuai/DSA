'''
more of snapping window instead of sliding window
new term - snapping window:
            one side of  the window snaps like a rubber band once something bigger/small is found
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        realprofit = 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > profit:
                profit = prices[i]
            else:
                realprofit = max(realprofit, profit - prices[i])
        return realprofit


input = [1,10,8,3, 5]
s = Solution()
print(s.maxProfit(input))