class Solution:
    def maxProfit(self, prices):
        smallest = prices[0]
        highest_profit = 0
        for i in prices[1:]:
            if i < smallest:
                smallest = i
            if i - smallest > highest_profit:
                highest_profit = i - smallest
        return highest_profit

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
